"""Captura uma loja de referência: home, catálogo, PDP, sacola e política, em 1440 e 390.

Uso:
  python3 extrair_referencia.py <apelido> <url> [--out refs] [--plp URL] [--pdp URL]

Saída em <out>/<apelido>/: dados.json (fontes, raios, cores, ordem das seções, textos de condição
por mecânica, apps detectados, texto da sacola) e prints *.jpg (página inteira até 9000px + dobra).
Só lê: adiciona um item ao carrinho para ver a sacola, nunca vai ao pagamento.
Requer: pip install playwright && Chrome instalado (usa channel='chrome').
"""
import argparse
import json
import os
import re
from urllib.parse import urljoin, urlparse

from playwright.sync_api import sync_playwright

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'
UA_M = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1'
MAX_H = 9000

# why: termos de mecânica comercial que queremos contar em texto visível, PT e EN
MECANICAS = {
    'frete_gratis': r'frete gr[aá]tis|free shipping|envio gr[aá]tis',
    'barra_progresso_frete': r'faltam\s*R\$|falta(m)? apenas|you.re \$?[\d.,]+ away|away from free|para ganhar frete|para frete gr[aá]tis',
    'pix': r'\bpix\b',
    'parcelamento': r'\d+\s*x\s*(de\s*)?R\$|sem juros|interest-free|installments|afterpay|klarna',
    'cashback': r'cashback',
    'cupom': r'cupom|coupon|c[oó]digo promocional|promo code|primeira compra|first order',
    'compre_junto': r'compre junto|frequently bought|bought together|combine com|complete (o|seu) look|complete the look|shop the look',
    'recomendacao': r'voc[eê] tamb[eé]m (pode )?gost|you may also like|recomendad|recommended|quem (viu|comprou)|people also|relacionad|related|pair it with|goes well',
    'kit_bundle': r'\bkits?\b|bundle|combo|leve \d|pague \d|buy \d|get \d|\d+\s*por\s*R\$|build (a|your) (box|bundle)|monte seu',
    'assinatura': r'assinatura|assine|subscribe (&|and) save|subscribe and|recorr[eê]ncia|subscription|clube',
    'brinde': r'brinde|gift with|free gift|mimo|amostra gr[aá]tis|free sample',
    'escassez_urgencia': r'[uú]ltimas? (unidades|pe[cç]as)|only \d+ left|restam|poucas unidades|low stock|acaba (hoje|em)|ends (in|tonight)|termina em|oferta rel[aâ]mpago|countdown',
    'selling_fast': r'mais vendid|best ?seller|top seller|selling fast|trending|queridinh',
    'avaliacoes': r'avalia[cç][oõ]es|reviews?\b|estrelas|stars|\d[.,]\d\s*\/\s*5',
    'avise_me': r'avise-me|avise me|notify me|me avise',
    'garantia_troca': r'troca gr[aá]tis|primeira troca|free returns|devolu[cç][aã]o gr[aá]tis|garantia|guarantee|satisfa[cç][aã]o',
    'guia_medidas': r'guia de (medidas|tamanhos)|tabela de medidas|size guide|size chart|find your size|qual (é o )?meu tamanho',
    'programa_fidelidade': r'pontos|points|rewards|fidelidade|loyalty|vip|membro|member',
    'ugc_social': r'#\w{3,}|instagram|tiktok|marque a gente|tag us|@\w{3,}',
    'app_download': r'baixe o app|download the app|app store|google play',
    'retire_loja': r'retire na loja|retirada|pick ?up in store|click (&|and) collect',
    'order_bump_checkbox': r'adicionar (tamb[eé]m|ao pedido)|add to (your )?order|proteja seu pedido|seguro (de envio|do pedido)|shipping protection|route|embalagem (para )?presente|gift ?wrap',
}

# why: assinatura exata no HTML; casar nome de classe dava falso positivo ("ocu" em "focus")
APPS = (r'zipify|rebuy|klaviyo|judge\.me|yotpo|loox|rechargeapps|skio|wheelio|upcart|kaching|tolstoy|selleasy'
        r'|frequently-bought|nosto|algolia|okendo|trustvox|cartpanda|yampi|appmax|pagaleve|smile\.io|aftersell'
        r'|reconvert|candyrack|intelligems|hextom|gorgias|blip|zendesk|octadesk|edrone|smarthint|pagefly'
        r'|gempages|shogun|replo|searchanise|boost-sd|findify|klevu|onetrust|cookiebot|privy|justuno|attentive'
        r'|growave|elevar|globo')

PROBE = r"""() => {
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
  const st = (e) => { if (!e) return null; const s = getComputedStyle(e);
    return { font: s.fontFamily.split(',')[0].replace(/["']/g,'').trim(), size: s.fontSize, weight: s.fontWeight,
      lh: s.lineHeight, ls: s.letterSpacing, tt: s.textTransform, color: s.color, bg: s.backgroundColor,
      radius: s.borderRadius, pad: s.padding, h: Math.round(e.getBoundingClientRect().height),
      text: (e.innerText || e.value || '').trim().replace(/\s+/g,' ').slice(0, 80) }; };
  const first = sel => [...document.querySelectorAll(sel)].find(vis);
  const btnRe = /adicionar|comprar|add to (cart|bag)|buy now|sacola|carrinho/i;
  const cta = [...document.querySelectorAll('button, a, input[type=submit]')].find(e => vis(e) && btnRe.test(e.innerText || e.value || ''));
  const header = first('header, [class*=header i]');
  const ann = first('[class*=announcement i], [class*=top-bar i], [class*=topbar i], [class*=marquee i], [class*=ticker i]');
  const main = document.querySelector('main') || document.body;
  // invariant: seções = filhos diretos do main (ou do body) com altura real, na ordem visual
  let blocks = [...main.children].filter(vis);
  if (blocks.length < 3) blocks = [...main.querySelectorAll(':scope > * > *')].filter(vis);
  const secs = blocks.slice(0, 40).map(e => { const r = e.getBoundingClientRect();
    const hd = e.querySelector('h1,h2,h3,[class*=title i],[class*=heading i]');
    return { top: Math.round(r.top + scrollY), h: Math.round(r.height), cls: (e.className && e.className.baseVal === undefined ? e.className : '').toString().slice(0, 70),
      heading: hd ? hd.innerText.trim().replace(/\s+/g,' ').slice(0, 70) : '',
      imgs: e.querySelectorAll('img,picture,video').length, videos: e.querySelectorAll('video,iframe[src*=youtube],iframe[src*=vimeo]').length,
      prods: e.querySelectorAll('a[href*="/products/"], a[href*="/produtos/"], a[href$="/p"], a[href*="/p?"]').length,
      btns: [...e.querySelectorAll('a,button')].filter(vis).map(b => b.innerText.trim()).filter(t => t && t.length < 30).slice(0, 4) }; });
  const bgs = {}; [...document.querySelectorAll('body, main > *, section, header, footer, button, a')].slice(0, 600).forEach(e => {
    const s = getComputedStyle(e); [s.backgroundColor, s.color].forEach(c => { if (c && c !== 'rgba(0, 0, 0, 0)') bgs[c] = (bgs[c] || 0) + 1; }); });
  const radii = {}; [...document.querySelectorAll('button, a[class*=btn i], a[class*=button i], img, [class*=card i]')].slice(0, 400)
    .forEach(e => { const r = getComputedStyle(e).borderTopLeftRadius; radii[r] = (radii[r] || 0) + 1; });
  const fonts = {}; [...document.querySelectorAll('h1,h2,h3,p,a,button,span')].slice(0, 800).forEach(e => {
    const f = getComputedStyle(e).fontFamily.split(',')[0].replace(/["']/g,'').trim(); fonts[f] = (fonts[f] || 0) + 1; });
  const links = [...document.querySelectorAll('a[href]')].map(a => ({ href: a.href, t: a.innerText.trim().replace(/\s+/g,' ').slice(0, 60) }));
  const navEl = first('header nav, nav, [class*=menu i]');
  return {
    title: document.title, url: location.href, h: document.documentElement.scrollHeight,
    shopify: !!window.Shopify, theme: window.Shopify && Shopify.theme ? Shopify.theme.name + ' / ' + (Shopify.theme.schema_name || '') : null,
    h1: st(first('h1')), h2: st(first('h2')), body: st(first('p')), cta: st(cta), header: st(header),
    headerSticky: header ? ['sticky','fixed'].includes(getComputedStyle(header).position) || ['sticky','fixed'].includes(getComputedStyle(header.parentElement).position) : null,
    announcement: ann ? ann.innerText.trim().replace(/\s+/g,' ').slice(0, 300) : null,
    nav: navEl ? [...navEl.querySelectorAll('a')].filter(vis).map(a => a.innerText.trim()).filter(Boolean).slice(0, 25) : [],
    sections: secs, colors: Object.entries(bgs).sort((a,b) => b[1]-a[1]).slice(0, 12),
    radii: Object.entries(radii).sort((a,b) => b[1]-a[1]).slice(0, 5), fonts: Object.entries(fonts).sort((a,b) => b[1]-a[1]).slice(0, 5),
    text: document.body.innerText.slice(0, 60000),
    links,
  };
}"""


def dismiss(page):
    page.keyboard.press('Escape')
    for rx in [r'^(aceitar|aceito|accept|accept all|allow all|concordo|ok|entendi|got it)', r'^(fechar|close|no,? thanks|não,? obrigad|agora não|x|×|✕)$',
               r'continuar (no|para o) site|stay on|continue to']:
        try:
            loc = page.get_by_role('button', name=re.compile(rx, re.I))
            for i in range(min(loc.count(), 3)):
                if loc.nth(i).is_visible():
                    loc.nth(i).click(timeout=1500)
        except Exception:
            pass
    page.keyboard.press('Escape')


def settle(page):
    # why: lazy-load e seções que montam no scroll só aparecem depois de rolar a página inteira
    for y in range(0, MAX_H, 700):
        page.evaluate(f'window.scrollTo(0, {y})')
        page.wait_for_timeout(120)
    page.evaluate('window.scrollTo(0, 0)')
    page.wait_for_timeout(800)


def mecanicas(txt):
    m = {}
    for k, rx in MECANICAS.items():
        hits = re.findall(rf'[^\n]{{0,50}}(?:{rx})[^\n]{{0,60}}', txt, re.I)
        if hits:
            m[k] = [' '.join(h.split())[:140] if isinstance(h, str) else '' for h in hits[:4]]
    return m


def pick(links, base, kinds):
    host = urlparse(base).netloc.replace('www.', '')
    for kind in kinds:
        for l in links:
            u = l['href']
            h = urlparse(u).netloc.replace('www.', '')
            if not (h == host or h.endswith('.' + host)) or '#' in u.split('/')[-1][:1]:
                continue
            if kind == 'pdp' and 'gift' not in u and (re.search(r'/kit/[^/]+/[^/?#]+', u) or re.search(r'/products?/[^/?#]+', u) or re.search(r'/produtos?/[^/?#]+', u) or re.search(r'/p(\?|$)', u)):
                return u
            if kind == 'plp' and re.search(r'/collections/(?!all$)[^/?#]+/?$|/categoria|/colecao|/colecoes/|/c/|/shop/?$|/collections/all', u) and '/products/' not in u:
                return u
            if kind == 'policy' and re.search(r'troca|devolu|reembolso|refund|return|policies|politica|pol%C3%ADtica|privacidade|shipping', u + ' ' + l['t'], re.I):
                return u
    return None


def shoot(page, path):
    h = min(page.evaluate('document.documentElement.scrollHeight'), MAX_H)
    page.screenshot(path=path, type='jpeg', quality=55, full_page=True, timeout=30000,
                    clip={'x': 0, 'y': 0, 'width': page.viewport_size['width'], 'height': h})


def visit(ctx, url, out, name, data, mobile=False):
    page = ctx.new_page()
    try:
        page.goto(url, wait_until='domcontentloaded', timeout=45000)
        page.wait_for_timeout(3500)
        dismiss(page)
        settle(page)
        dismiss(page)
        shoot(page, f'{out}/{name}.jpg')
        if mobile:
            page.screenshot(path=f'{out}/{name}-fold.jpg', type='jpeg', quality=60)
            return page
        p = page.evaluate(PROBE)
        p['mecanicas'] = mecanicas(p.pop('text'))
        p['apps'] = sorted({x.lower() for x in re.findall(APPS, page.content(), re.I)})
        data[name] = {k: v for k, v in p.items() if k != 'links'}
        page.screenshot(path=f'{out}/{name}-fold.jpg', type='jpeg', quality=60)
        return page, p['links']
    except Exception as e:
        data.setdefault('erros', []).append(f'{name}: {str(e)[:200]}')
        return (page, []) if not mobile else page


def try_cart(page, out, data):
    try:
        # why: o drawer/página de carrinho é onde moram upsell, barra de frete e order bump
        sizes = page.locator('input[type=radio] + label, [class*=swatch i] label, [class*=variant i] button, [class*=size i] button, fieldset label')
        for i in range(min(sizes.count(), 8)):
            el = sizes.nth(i)
            if el.is_visible() and 'disabled' not in (el.get_attribute('class') or '') and 'soldout' not in (el.get_attribute('class') or '').lower():
                try:
                    el.click(timeout=1500)
                    break
                except Exception:
                    continue
        # hazard: "comprar agora"/"buy it now" pula a sacola e abre o checkout; só CTA de adicionar ou "Comprar" puro
        btn = page.get_by_role('button', name=re.compile(r'adicionar|add to (cart|bag)|colocar na sacola|eu quero|^\s*comprar\s*$', re.I))
        for i in range(btn.count()):
            if re.search(r'agora|now|finalizar|checkout|pagar|express', btn.nth(i).inner_text(), re.I):
                continue
            if btn.nth(i).is_visible() and btn.nth(i).is_enabled():
                btn.nth(i).click(timeout=4000)
                break
        page.wait_for_timeout(3500)
        page.screenshot(path=f'{out}/cart-drawer.jpg', type='jpeg', quality=60)
        txt = page.evaluate('document.body.innerText')
        data['cart_drawer_mecanicas'] = mecanicas(txt)
        # invariant: drawer = painel à direita, alto, com preço, preso num ancestral fixed; nome de classe varia por tema
        drawer = page.evaluate(r"""() => {
          const fixed = e => { for (; e && e !== document.body; e = e.parentElement) if (getComputedStyle(e).position === 'fixed') return true; return false; };
          const c = [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect();
            return r.width > 240 && r.width < 760 && r.height > innerHeight * 0.6 && r.left > innerWidth * 0.4
              && getComputedStyle(e).visibility !== 'hidden' && /R?\$\s?\d/.test(e.innerText) && fixed(e); });
          const d = c.sort((a, b) => b.innerText.length - a.innerText.length)[0];
          return d ? d.innerText.replace(/\s+/g, ' ').slice(0, 1500) : null; }""")
        data['cart_drawer_texto'] = drawer
    except Exception as e:
        data.setdefault('erros', []).append(f'cart: {str(e)[:200]}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slug')
    ap.add_argument('url')
    ap.add_argument('--out', default='refs')
    ap.add_argument('--plp', help='catálogo, quando a descoberta pela home erra')
    ap.add_argument('--pdp', help='produto, quando a descoberta pela home erra')
    a = ap.parse_args()
    slug, url = a.slug, a.url
    out = os.path.join(a.out, slug)
    os.makedirs(out, exist_ok=True)
    data = {'slug': slug, 'base': url}
    pw = sync_playwright().start()
    # hazard: sem `with sync_playwright()`: fechar o Chrome trava em algumas lojas; ver os._exit no fim
    b = pw.chromium.launch(channel='chrome', headless=True, args=['--disable-blink-features=AutomationControlled'])
    ctx = b.new_context(viewport={'width': 1440, 'height': 900}, user_agent=UA, locale='pt-BR')
    page, links = visit(ctx, url, out, 'home', data)
    plp = a.plp or pick(links, url, ['plp'])
    pdp = a.pdp or pick(links, url, ['pdp'])
    pol = pick(links, url, ['policy'])
    if plp:
        p2, l2 = visit(ctx, plp, out, 'plp', data)
        pdp = a.pdp or pick(l2, url, ['pdp']) or pdp
        p2.close()
    if pdp:
        p3, _ = visit(ctx, pdp, out, 'pdp', data)
        try_cart(p3, out, data)
        p3.close()
    if pol:
        p4, _ = visit(ctx, pol, out, 'policy', data)
        p4.close()
    data['urls'] = {'plp': plp, 'pdp': pdp, 'policy': pol}
    mctx = b.new_context(viewport={'width': 390, 'height': 844}, user_agent=UA_M, is_mobile=True, has_touch=True, device_scale_factor=1, locale='pt-BR')
    with open(f'{out}/dados.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    for name, u in [('home-m', url), ('pdp-m', pdp)]:
        if u:
            visit(mctx, u, out, name, data, mobile=True)
    with open(f'{out}/dados.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(slug, 'ok', data['urls'], data.get('erros'), flush=True)
    # hazard: fechar o Chrome trava em algumas lojas (service worker/beforeunload); dados já estão no disco
    os._exit(0)


if __name__ == '__main__':
    main()
