# Padrões por página

## Globais

**Barra de anúncio / ticker.** 3–4 fatos reais (PIX X% off, até Nx sem juros, frete, cidade).
Pausa no hover e no foco; parado com reduced-motion.

**Header.** Logo, menu (3–5 itens; subitens viram dropdown só se existirem), busca, conta, sacola
com contador. Estados repouso e rolado. Sticky: numa plataforma que embrulha seções (Shopify), o
`position: sticky` vai no wrapper, não no filho.

**Rodapé.** Newsletter (se houver campanha de verdade), colunas Loja / Ajuda / Políticas / Contato
(no mobile, acordeão), "Preferências de cookies" como link, linha legal com razão social e CNPJ.

## Home

Hero (foto ou vídeo da marca, uma frase, um CTA) → vitrine do que vender agora → bloco que conta a
história (arte, processo, origem) → produtos em destaque em outro formato (duo, editorial) → marca
(quem, de onde, contato). Sem carrossel de hero de 5 slides; sem grade de ícones genéricos
("Frete rápido", "Compra segura") a menos que o dado seja real e específico.

A ordem acima é a da loja de marca/editorial. Loja de varejo com muitas linhas (snacks,
suplemento, cosmético, esporte) segue outra, medida nas lojas de
[lojas-referencia.md](lojas-referencia.md):

```
barra de anúncio → header → hero de promoção (1–3 slides) → faixa de 3–4 benefícios com número
→ navegação visual (círculos ou tiles: categoria, objetivo, ambiente, personagem)
→ mais vendidos → banner de lançamento/oferta → vitrine por linha (repetir 2–3x com banner entre)
→ prova (avaliações, UGC, imprensa) → conteúdo (guia, blog) → newsletter com incentivo → rodapé
```

- Alterne vitrine e banner: duas vitrines seguidas viram uma parede de cards.
- Cada vitrine tem nome que vende ("Muita proteína", "Queridinhos da semana"), não "Produtos".
- Loja pequena, de luxo ou de drop fica com 3–5 seções (Mondepars tem 3). Mais seções não é mais
  conversão; é mais rolagem.
- Banners, faixa de benefícios e navegação visual: [banners.md](banners.md).

## Catálogo

- Cabeçalho: breadcrumb, título, contagem real ("12 peças"), ordenar (usar a ordenação nativa).
- Filtros: no desktop, barra ou lateral; no mobile, painel com "Ver N resultados". Contagens reais
  por faceta; filtro sem resultado desabilitado, não escondido.
- Grid 3–4 no desktop, 2 no mobile. 2ª foto no hover (desktop).
- Adição rápida por tamanho no card é ótima para moda; indisponível aparece riscado/desabilitado.
- Estados: vazio (com saída), "mostrando X de Y" + paginação ou carregar mais.
- Topo da coleção: banner baixo (200–320px) com o título, **ou** fileira de subcategorias com foto
  (Modab, Kylie). Os dois juntos empurram o primeiro produto para fora da dobra.
- Filtros rápidos em chips acima do grid com o atributo que decide a compra no nicho: benefício da
  peça ("Não amassa", "Cós alto"), nível de jogo, necessidade do cabelo, "Desconto pix".
- Card: preço, parcelas e preço PIX quando há desconto real; um selo por vez (Lançamento, -X%,
  Frete grátis); estrelas só quando existe avaliação.
- Tile editorial no meio do grid (1 a cada 8–12 cards) quando há campanha que conte algo.

## Produto (PDP)

Desktop: galeria à esquerda, coluna de compra fixa à direita (sticky). Mobile: galeria em carrossel
com indicador, e barra de compra fixa embaixo quando o botão principal sai da tela.

Ordem da coluna de compra: breadcrumb → selo → nome → linha de atributos → preço + parcelamento +
PIX → variantes (cor com swatch só se houver mais de 1; tamanho em chips ou barra) → botão →
nota de frete/prazo → descrição → acordeões (Detalhes aberto; Guia de medidas; Trocas) → contato.

- Botão comunica o estado: "Escolha o tamanho" → "Adicionar" → "Adicionado".
- Esgotado: troca o botão por "avise-me". Formulário nativo de cliente com tag só **capta** o
  e-mail; aviso automático de volta ao estoque por variante exige app. Não prometa o que não roda.
- Âncoras `#guia` e `#trocas` abrem o acordeão correspondente (links do rodapé apontam para elas).
- O bloco decisivo do nicho recebe mais espaço (ver [nichos.md](nichos.md)).
- **CEP logo abaixo do botão** ("Consulte prazo e valores"), com o frete real. Visto em 7 das
  lojas brasileiras analisadas (ver [lojas-referencia.md](lojas-referencia.md)).
- **Irmãos como variantes**: sabor, tamanho ou cor que são produtos separados aparecem como amostras
  com foto que levam ao outro produto (Bold, Gymshark, Real Madrid).
- **Faixa de fatos** com 3 ícones e números logo abaixo da galeria ou do preço (21g proteína · 0
  açúcar · 12 unidades; 11 horas · 2 dias · garantia vitalícia).
- **Linha de valor sob o preço**, uma por vez: cashback em R$, preço de membro, preço no PIX.
- Abaixo da dobra, nesta ordem: conteúdo do produto (por que, como usar, ciência, composição) →
  compre junto / combina com → avaliações → FAQ → recomendados → vistos recentemente.
- Mecânicas de ticket médio (kits, compre junto, brinde): [conversao.md](conversao.md).

## Sacola (drawer)

Itens com variante, +/−, remover; subtotal; calculadora de CEP com frete **real** da plataforma
(com mensagem clara quando falha); condições (PIX, parcelas); botão para o checkout. Nunca somar um
frete fixo chumbado no tema. Se há desconto automático, mostre o valor que a plataforma calculou
(`total_discount`), nunca recalcule — o total já vem líquido e recalcular desconta duas vezes.

Ordem que as melhores sacolas seguem (Kylie, Stanley, Bold, Modab):

```
título + contagem → barra de frete grátis (ou brinde por faixa) → itens → brinde escolhido
→ recomendação com variante inline → cupom → CEP → subtotal + parcelas → Finalizar
→ Continuar comprando
```

- A barra usa o total real do carrinho e mostra o estado atingido ("Você desbloqueou frete grátis").
- Recomendação na sacola adiciona sem sair dela; item com variante tem seletor no próprio card.
- "Salvar para mais tarde" no lugar de só remover, quando a plataforma guarda a lista.
- Detalhe e honestidade de cada mecânica: [conversao.md](conversao.md).

## Busca

Painel com sugestões ao digitar (busca preditiva nativa), produtos com foto e preço, estado "nada
encontrado" com sugestão de categorias.

## Páginas do rodapé (ajuda e políticas)

Um template de documento para todas: cabeçalho com título e coluna lateral com o resumo; abas
entre páginas irmãs (Ajuda: Guia de medidas · Envio · Trocas · Contato; Políticas: Privacidade ·
Reembolso · Frete · Termos · Preferências de cookies); corpo em linhas de duas colunas (rótulo
numerado 01, 02… à esquerda, conteúdo à direita).

- **Guia de medidas:** tabela editável, "como medir" com marcas A/B sobre a foto, caimento, CTA de
  ajuda. Medidas reais ou marcadas como ilustrativas.
- **Trocas:** 3 passos, prazos (7 dias de arrependimento; tamanho; defeito), condições, contato.
- **Contato:** canais (WhatsApp, e-mail, cidade, empresa), formulário nativo (nome, e-mail,
  telefone opcional, nº do pedido opcional, mensagem) com estados de sucesso e erro, e atalhos
  "talvez já esteja aqui".
- **Políticas:** o texto vem da plataforma (o lojista edita no admin). Divida pelo `<h2>` para
  aplicar o layout de linhas; não reescreva o texto jurídico no tema.
- **Regulamentos** de cada mecânica ativa (cashback, assinatura, clube, brinde, cupom) ganham página
  própria no mesmo template (Bold tem o da assinatura). Oferta que depende de regra aponta para ela.
- **FAQ como porta de entrada**: perguntas agrupadas (Pagamentos e cashback, Trocas, Entregas) com
  âncoras que os links do rodapé e da PDP usam (Amaro). Política de 25 mil pixels de texto corrido
  (visto numa loja grande) é o que não fazer: índice lateral e seções recolhíveis.
- **Acompanhar pedido** como link no topo ou no rodapé (Stanley), não escondido dentro da conta.

## Cookies (LGPD)

- Banner: Aceitar todos · Recusar · Preferências. Os três com o mesmo peso de escolha.
- Painel: Necessários (sempre ativos, sem interruptor), Analíticos e Marketing **desligados por
  padrão** (consentimento é opt-in), Recusar · Salvar escolhas · Aceitar todos.
- Nada de script de análise/marketing antes da escolha. Teste: antes da escolha nada liberado;
  Recusar = nada; Salvar só com Analíticos = análise sim, marketing não.
- Link "Preferências de cookies" no rodapé e na aba de políticas reabre o painel.

## 404

Título humano, busca, link para o catálogo. Mesmo header e rodapé.
