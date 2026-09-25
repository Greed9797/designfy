"""Varredura visual de loja: 1440 e 390, claro e escuro, prints e checagens que não dependem do tema.

Uso:
  python3 qa_loja.py https://loja.myshopify.com / /collections/all /products/x --theme-id 123 --out shots
  python3 qa_loja.py https://preview.vercel.app / /produto.html --out shots

Com --theme-id, a URL ganha ?preview_theme_id=<id> e a primeira checagem é Shopify.theme.id == id
(sem isso você pode estar olhando o tema publicado). Sai com código 1 se alguma checagem falhar.
Requer: pip install playwright && Chrome instalado (usa channel='chrome').
"""
import argparse
import os
import sys

from playwright.sync_api import sync_playwright

VIEWPORTS = (('desktop', {'width': 1440, 'height': 900}, False), ('mobile', {'width': 390, 'height': 844}, True))
PROBE = """() => ({
  h1: [...document.querySelectorAll('h1')].map(e => e.textContent.trim()).filter(Boolean),
  overflowX: document.documentElement.scrollWidth > innerWidth + 1,
  brokenImgs: [...document.images].filter(i => i.complete && i.currentSrc && !i.naturalWidth).map(i => i.currentSrc).slice(0, 5),
  // WCAG 2.5.8 (AA): alvo < 24x24 passa se o círculo de 24px centrado nele não cruza outro alvo
  // nem o círculo de outro alvo pequeno. Exceção: link inline dentro de frase.
  smallTaps: (() => {
    // <details> fechado, display/visibility, inert e pointer-events:none não são tocáveis.
    // opacity:0 e aria-hidden continuam clicáveis: seguem contando.
    const shown = e => e.checkVisibility({ visibilityProperty: true }) && !e.closest('[inert]')
      && getComputedStyle(e).pointerEvents !== 'none';
    const inline = e => getComputedStyle(e).display === 'inline' && e.parentElement
      && e.parentElement.textContent.trim().length > e.textContent.trim().length + 20;
    const t = [...document.querySelectorAll('a[href],button,input:not([type=hidden]),select')].map(e => [e, e.getBoundingClientRect()])
      .filter(([e, r]) => r.width && r.height && shown(e));
    const c = r => [r.x + r.width / 2, r.y + r.height / 2];
    const small = r => r.width < 24 || r.height < 24;
    const hits = ([e, r], [o, q]) => {
      if (o === e || o.contains(e) || e.contains(o)) return false;
      const [x, y] = c(r);
      if (Math.hypot(x - Math.max(q.left, Math.min(x, q.right)), y - Math.max(q.top, Math.min(y, q.bottom))) < 12) return true;
      return small(q) && Math.hypot(x - c(q)[0], y - c(q)[1]) < 24;
    };
    return t.filter(a => small(a[1]) && !inline(a[0]) && t.some(b => hits(a, b)))
      .map(([e]) => (e.textContent.trim() || e.getAttribute('aria-label') || e.tagName).slice(0, 30)).slice(0, 10);
  })(),
  noName: [...document.querySelectorAll('a[href],button')].filter(e => e.checkVisibility({ visibilityProperty: true })
    && !(e.getAttribute('aria-label') || e.textContent.trim() || e.querySelector('img[alt]:not([alt=""])') || e.getAttribute('title'))).length,
  theme: document.documentElement.dataset.theme || null,
})"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('base')
    ap.add_argument('paths', nargs='+')
    ap.add_argument('--theme-id', type=int)
    ap.add_argument('--out', default='shots')
    ap.add_argument('--schemes', default='light,dark')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    q = f'?preview_theme_id={a.theme_id}&pb=0' if a.theme_id else ''
    fails = []
    with sync_playwright() as pw:
        br = pw.chromium.launch(channel='chrome', headless=True)
        for scheme in a.schemes.split(','):
            for vname, vp, mob in VIEWPORTS:
                ctx = br.new_context(viewport=vp, is_mobile=mob, has_touch=mob, color_scheme=scheme)
                pg = ctx.new_page()
                errs = []
                pg.on('pageerror', lambda e: errs.append(str(e)))
                for i, path in enumerate(a.paths):
                    url = a.base.rstrip('/') + path + (q.replace('?', '&') if '?' in path else q)
                    resp = pg.goto(url)
                    pg.wait_for_load_state('load')
                    pg.wait_for_timeout(800)
                    if a.theme_id and i == 0:
                        got = pg.evaluate('window.Shopify && Shopify.theme && Shopify.theme.id')
                        if got != a.theme_id:
                            sys.exit(f'ABORTADO: tema servido {got} != {a.theme_id} (olhando o tema errado)')
                    st = pg.evaluate(PROBE)
                    tag = f'{scheme}/{vname}{path}'
                    problems = []
                    if resp and resp.status >= 400: problems.append(f'HTTP {resp.status}')
                    if len(st['h1']) != 1: problems.append(f"h1={st['h1']}")
                    if st['overflowX']: problems.append('rolagem horizontal')
                    if st['brokenImgs']: problems.append(f"imagem quebrada {st['brokenImgs']}")
                    if st['smallTaps']: problems.append(f"alvo < 24px encostado em outro {st['smallTaps']}")
                    if st['noName']: problems.append(f"{st['noName']} botão/link sem nome acessível")
                    if errs: problems.append(f'erros JS {errs[:3]}'); errs.clear()
                    print(('FALHA ' if problems else 'ok    ') + tag, '; '.join(problems))
                    if problems: fails.append(tag)
                    name = f"{scheme}-{vname}-{path.strip('/').replace('/', '_') or 'home'}.png"
                    pg.screenshot(path=os.path.join(a.out, name), full_page=True)
                ctx.close()
        br.close()
    print(f'\n{len(fails)} falha(s). Prints em {a.out}/ — olhe os prints: métrica não pega texto colado nem cor errada.')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
