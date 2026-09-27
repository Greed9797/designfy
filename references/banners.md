# Banners: hero, promoção e coleção

Padrões medidos em 19 lojas (2026-09). Banner é a peça que mais envelhece e a que mais parece
"template" quando feita sem regra. As regras abaixo valem para desenhar no Figma, para gerar
imagem com IA e para implementar.

## Os tipos, e o que cada um precisa dizer

| Tipo | Mensagem | Estrutura | Visto em |
|---|---|---|---|
| Lançamento | o que é novo, em até 4 palavras | título grande + produto real + 1 CTA ("Experimente") + detalhe de versão em selo | Bold "Novo sabor Chocomalte", Pretorian "Core & Strike" |
| Oferta | o número da oferta | número gigante ("50% OFF + BRINDE", "+10% OFF com o cupom") + produto + microtexto legal | Boca Rosa, Decathlon, Amaro |
| Oferta progressiva | a escada | "+1 item 10% OFF · +2 itens 15% OFF" em caixas lado a lado | Bold |
| Brinde (GWP) | o limite e o brinde | "Nas compras acima de R$ 129,90 ganhe…" + foto do brinde | Boca Rosa |
| Collab / campanha | as duas marcas e uma frase | lockup "Marca × Parceira", foto de campanha, 1 CTA | Stanley × Farm Rio, Gymshark × Whitney |
| Editorial / marca | uma sensação | foto ou vídeo em tela cheia, texto mínimo ou nenhum | Mondepars, Modab (vídeo), Loft 111 |
| Sazonal | a data e o que comprar para ela | "Dia das Crianças", "Holiday gift sets", "App week" | Decathlon, Kylie, Amaro |
| Banner de coleção (catálogo) | o nome da coleção | faixa baixa com título sobre a foto, sem CTA (o grid é o CTA) | Kylie, Galeroca, Decathlon, Lavitan, Woly |
| Banner no meio do grid | uma história ou campanha | tile editorial do tamanho de 1–2 cards dentro do grid | Kylie (fragrância) |
| Chamada na PDP | a condição ativa | caixa discreta perto do preço ("Last chance sale: até 50% off") | Gymshark |

## Anatomia do hero de promoção

- **Um recado por slide.** Título ≤ 5 palavras, subtítulo de 1 linha, **1 CTA** (2 só quando a
  escolha é real, como "Feminino / Masculino" da Gymshark).
- **Texto no terço esquerdo, produto no direito** (Bold, Boca Rosa, Lavitan, Stanley).
  Nunca texto sobre a parte movimentada da foto.
- **Produto real recortado** (packshot) sobre fundo de cor da marca ou cena. É o que Bold, Boca
  Rosa, Lavitan e Embelleze fazem: a embalagem é a verdade do banner.
- **Cor do fundo vem da embalagem ou da campanha**, não do acento da UI. Bold: laranja da caixa;
  Boca Rosa: rosa/magenta da coleção; Lavitan: marrom do café.
- **Microtexto legal** no rodapé do banner, 10–11px, quando há condição: validade, não cumulativo,
  peças selecionadas. Condição que muda o preço também aparece na PDP e na sacola.

## Medidas observadas

- Hero de promoção no desktop (1440): **480–690px** de altura (Lavitan 483, Bold 514, Pretorian
  525, Embelleze 530, Shark 563, Boca Rosa 564, Stanley 577, Maxme 626, Woly 684). Deixa a faixa de
  benefícios ou o começo da vitrine aparecer na primeira dobra de 900px.
- Hero editorial: **tela cheia** (744–944px: Mondepars, Kylie, Modab com vídeo).
- Banner de coleção no catálogo: **200–320px**, título sobre a imagem.
- Mobile: **arte própria, não recorte do desktop.** Modab troca o enquadramento para um close
  vertical com o texto centralizado embaixo; a proporção de mobile fica entre 4:5 e 9:16. Peça as
  duas artes no Figma (1440 e 390) e implemente com `<picture>` + `media`, não com
  `object-position` torcendo a mesma foto.
- Área segura: nada importante nos 10% laterais (setas do carrossel) nem nos 60px de baixo
  (indicadores).

## Carrossel

- Até 3–4 slides, cada um uma oferta diferente; indicadores visíveis e setas no desktop.
- Botão de pausa acessível (Stanley tem, com texto para leitor de tela sobre a rotação). Rotação
  pausa no hover e no foco e não roda com `prefers-reduced-motion`.
- O primeiro slide é o único que a maioria vê: ele carrega a oferta principal e é o LCP da página
  (imagem com `fetchpriority="high"`, sem lazy-load).
- Loja pequena ou editorial: sem carrossel. Uma imagem forte (Mondepars) vence cinco fracas.

## Faixa de benefícios sob o hero

3–4 itens com ícone de traço e **número real**: "Frete grátis acima de R$ 199,99 · 5% de desconto
no Pix · 20% cashback" (Amaro), "Frete grátis acima de R$ 169 · 10% OFF PRIMEIRACOMPRA · até 4x sem
juros" (Boca Rosa), "Troca grátis · Parcele sem juros · Frete grátis acima de R$ 700 · Atendimento"
(Loft 111). Genérico sem número ("Compra segura", "Entrega rápida") não entra — regra do `SKILL.md`.

## Navegação visual que vive entre os banners

- **Círculos de categoria** (estilo stories) logo abaixo do hero: Decathlon (esportes), Woly
  (ambientes), Lavitan (objetivos com ícone), Bold (linhas com packshot). Com 6–10 itens, rolagem
  horizontal no mobile.
- **Tiles de coleção com foto** em fileira de 4 (Shark, Gymshark, Stanley "Compre por categorias").
- **Chips com foto no topo do catálogo** (Modab: Pantalona, Wide leg, Flare, Reta…): o banner de
  coleção vira navegação.
- **Por personagem / por objetivo / por ambiente**: a taxonomia do cliente, não a do estoque
  (Galeroca por personagem, Lavitan e Maxme por objetivo, Woly por ambiente).

## Gerar banner com IA

- **Nunca gere o produto.** IA distorce texto de rótulo e forma de embalagem. Use o packshot real
  (fundo removido) e gere só o fundo/cena, depois componha no Figma.
- Imagem gerada vai marcada como tal na lista "Validar com o cliente". Pessoa gerada não
  representa cliente real nem vira depoimento.
- Gere nas duas proporções de uma vez (desktop 16:6–16:7 e mobile 4:5), com a área do texto vazia
  e na cor que vai recebê-lo.
- Prompt em três partes: cena (luz, superfície, cor da marca), composição (onde fica o produto,
  onde fica o vazio do texto), restrições (sem texto, sem logos, sem mãos se não houver foto real).
- Texto do banner é camada editável no Figma e HTML no site, **nunca pixel dentro da imagem**: muda
  sem regerar, é lido pelo leitor de tela e não vira borrão no mobile.

## Erros que as lojas cometem (e você não)

- Banner com o texto chapado na imagem: não traduz, não atualiza, reprova acessibilidade.
- Cinco slides com a mesma oferta em cores diferentes.
- Oferta no banner que não aparece na PDP nem na sacola.
- Pop-up de notificação/cookies cobrindo o hero na primeira visita (visto em três lojas): o
  banner que custou caro some atrás de um diálogo.
