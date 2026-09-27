---
name: atelie-de-vitrine
description: >
  Guia de processo e de padrões para desenhar e implementar loja virtual (e-commerce) com
  qualidade de estúdio em qualquer nicho: moda, beleza, casa, plantas, pet, esporte, eletrônicos,
  alimentos, joias, B2B. Cobre briefing de fatos reais, auditoria do site atual, referências
  (só estrutura), design system com variáveis e modo claro/escuro no Figma, todas as páginas da
  jornada (home, catálogo, produto, sacola, busca, páginas do rodapé, políticas, cookies LGPD,
  estados vazios e esgotado) em desktop 1440 e mobile 390, implementação em tema Shopify ou site
  estático, e verificação com evidência antes de entregar. Use sempre que o pedido envolver loja,
  e-commerce, Shopify, tema, vitrine, PDP, página de produto, coleção, catálogo, carrinho, checkout,
  redesign de loja, "clonar a estrutura de uma loja de referência", ou design de loja no Figma,
  e também para upsell, cross-sell, downsell, order bump, kit/quantidade com desconto, barra de
  frete grátis, brinde por faixa, cashback, assinatura e banners (hero, promoção, coleção),
  mesmo que o usuário não diga "guia" nem "design system". O passo a passo de Figma
  (references/processo-figma.md) também vale para qualquer tela no Figma: landing page,
  dashboard, app.
---

# Guia de design para e-commerce

> **Vai desenhar no Figma?** Leia [references/processo-figma.md](references/processo-figma.md)
> inteiro antes da primeira escrita e siga os passos na ordem, sem pular. Vale para qualquer
> modelo (Claude, Gemini, GPT) e qualquer ferramenta (script da Plugin API ou ferramentas
> granulares tipo talk-to-figma). É esse processo, e não o gosto do modelo, que separa tela de
> estúdio de tela de template.

Este guia descreve **como** chegar numa loja com cara de marca séria, e não **qual** estética usar.
A estética sai do nicho, da marca e das referências. O processo, as regras de honestidade e o nível
de acabamento são os mesmos em qualquer loja.

Ele nasceu de lojas reais: streetwear, skate shop, cactos colecionáveis, luvas de
luta, máquinas industriais B2B, marca de roupas com checkout externo. Em 2026-09 foi calibrado com
19 lojas de referência (moda, beleza, snacks, suplementos, esporte, casa, clube), medidas página a
página ([references/lojas-referencia.md](references/lojas-referencia.md)). O que se repetiu entre
elas virou regra aqui; o que foi específico de uma ficou de fora.

## Os princípios, com o motivo de cada um

1. **Fatos antes de pixels.** Preço, parcelamento, desconto no PIX, frete, prazos de troca, CNPJ,
   canais de contato e políticas vêm da loja, nunca da imaginação. Loja é lugar de dinheiro:
   um "frete grátis acima de R$ 299" inventado vira reclamação no Procon. Onde faltar dado,
   use um valor ilustrativo **marcado como tal** e ponha na lista "Validar com o cliente".
2. **Nada de prova social inventada.** Depoimento, avaliação, número de clientes, "mais vendido",
   desconto riscado, especificação técnica e estoque só entram se forem reais e autorizados.
   Sem eles, a seção não existe — o layout tem que ficar bom sem ela. Vale para gatilho de venda:
   "X pessoas vendo agora", "últimas unidades" e contagem regressiva só com dado real (analytics,
   estoque da variante, data de fim da campanha). Número que muda a cada recarga é enganação.
3. **Referência empresta estrutura, nunca identidade.** Da loja de referência se copia a ordem
   das seções, o ritmo, o grid, o comportamento e o movimento. Logo, texto, fotos e tipografia da
   referência não entram. Isso é ética e também é marca: a loja precisa parecer ela mesma.
4. **Sistema pequeno, uma assinatura.** Uma ou duas famílias tipográficas, paleta neutra, **um**
   acento usado só como sinal (foco, selecionado, novo, esgotado), um valor de raio, escala de
   espaço 4→128. Quanto menos peças, mais a loja parece desenhada e menos parece montada.
5. **O produto é o herói.** Foto consistente (mesmo fundo, mesma proporção, 2ª foto no hover),
   card com o mínimo (nome, preço, selo quando houver). Tudo em volta recua.
6. **A jornada inteira, não só a home.** Quem compra passa por catálogo, produto, sacola, frete,
   ajuda e política. Uma home linda com PDP genérica e rodapé do tema comprado parece golpe.
   Ver a lista mínima de telas abaixo.
7. **Desktop e mobile são duas telas, não uma esticada.** 1440 e 390, cada uma composta. No
   mobile a compra precisa caber no polegar (barra de compra fixa, filtros em painel).
8. **Acessível por padrão.** Contraste AA (texto 4,5:1). Se o acento for claro, o texto sobre ele
   é preto. Foco visível, alvo de toque ≥ 44px, `prefers-reduced-motion` respeitado.
9. **Implementar em camada limpa, não em remendo.** Tema comprado com anos de CSS empilhado não
   se "ajusta até ficar igual": seções próprias, CSS próprio com escopo, e a infraestrutura da
   plataforma (carrinho, busca, frete, checkout, formulários) reaproveitada.
10. **"Pronto" exige prova.** Print lado a lado, teste de interação e checagem de que você está
    olhando o ambiente certo. Nada é publicado sem OK humano explícito.

## Fluxo de trabalho

Siga as fases na ordem. Cada uma tem um entregável que o usuário consegue aprovar.

### Fase 0 — Fatos e auditoria

- Colete os fatos da loja numa lista curta. O que coletar está em
  [references/briefing-e-fatos.md](references/briefing-e-fatos.md).
- Se existe site atual: capture desktop e mobile e marque os problemas com pinos numerados
  (A1, A2…), cada um com problema, evidência medida e solução proposta. Auditoria sem medida
  ("fica feio") não convence cliente nenhum; "texto branco no laranja dá 2,98:1, reprova AA" convence.
- Mapeie o que a plataforma/tema já faz antes de desenhar algo que exige código novo
  (ex.: "avise-me quando voltar ao estoque" precisa de app; o formulário nativo não faz).
- Liste as mecânicas de venda que **rodam de verdade** hoje: regras de desconto, frete grátis,
  cashback, brinde, assinatura, app de recomendação, o que o checkout aceita (bump, pós-compra).
  É isso que o design pode mostrar. Mapa das mecânicas em
  [references/conversao.md](references/conversao.md).

### Fase 1 — Direção

- Escolha 2 a 4 referências e anote **o que** vai emprestar de cada uma (ex.: "header que encolhe
  ao rolar", "grid de 3 com a 2ª foto no hover", "PDP com galeria à esquerda e compra fixa").
  Comece pelo dossiê [references/lojas-referencia.md](references/lojas-referencia.md), que já diz o
  que emprestar de 19 lojas. Referência nova: `scripts/extrair_referencia.py` captura home,
  catálogo, PDP, sacola e política em 1440/390 com fontes, raios, cores, ordem das seções,
  mecânicas e apps.
- Adapte ao nicho com a tabela de [references/nichos.md](references/nichos.md): cada nicho tem um
  bloco decisivo diferente na PDP, atributos de filtro diferentes e um tipo de prova diferente.
- Defina a voz em uma frase e o mundo visual em três palavras. Se o usuário já trouxe marca,
  paleta ou fonte, isso manda; não redirecione para o seu gosto.

### Fase 2 — Design system

Tokens como variáveis (cores com papéis, não nomes de cor), estilos de texto, componentes com
variantes e estados. Detalhe, incluindo modo escuro por modo de variável e os tokens fixos e
inversos que evitam o bug clássico do "escuro que inverte a foto", em
[references/design-system.md](references/design-system.md).

### Fase 3 — Telas

Lista mínima (desktop 1440 + mobile 390; claro e escuro se o escuro fizer parte do pedido):

| Tela | Estados que precisam existir |
|---|---|
| Home | header em repouso e rolado, hero (desktop e arte mobile própria), vitrine, bloco de marca |
| Catálogo | com filtros abertos (mobile), vazio, paginação ou "carregar mais" |
| Produto (PDP) | variante selecionada, esgotado/avise-me, guia de medidas quando couber |
| Sacola (drawer) | vazia, com itens, barra de frete (faltando e atingido), recomendação, frete calculado, erro de CEP |
| Busca | sugestões, sem resultado |
| Páginas do rodapé | ajuda (medidas, trocas, contato) e políticas com texto real |
| Cookies (LGPD) | banner e painel de preferências |
| 404 | com saída para o catálogo |

Padrões de cada tela (ordem dos blocos, o que é obrigatório, erros comuns) em
[references/paginas.md](references/paginas.md). **Como** montar cada tela no Figma, passo a passo
(descoberta, dado real, moldura clonada, uma seção por chamada, print e checklist), está em
[references/processo-figma.md](references/processo-figma.md); é obrigatório. A estrutura do
arquivo, a receita de modo escuro e as armadilhas da Plugin API estão em
[references/figma.md](references/figma.md). Banners (tipos, medidas, arte mobile, geração com IA)
em [references/banners.md](references/banners.md); onde entra cada mecânica de venda (compre junto,
kits, brinde, cashback, recomendação na sacola) em [references/conversao.md](references/conversao.md).

### Fase 4 — Revisão com o cliente

Entregue o link do Figma (ou um preview navegável) **e** a lista "Validar com o cliente": preços
ilustrativos, medidas, prazos, textos jurídicos, fotos que faltam, qualquer suposição. Diga o que é
imagem gerada por IA. Feedback vira iteração; aprovação explícita libera a implementação.

### Fase 5 — Implementação

- **Shopify:** [references/shopify.md](references/shopify.md) — arquitetura de seções próprias,
  dados via Admin API, e as armadilhas que fazem o push "dar certo" sem subir nada.
- **Site estático / preview (Vercel etc.):** mesmo design system em `:root`, HTML semântico,
  JS mínimo. Formulário sem destino definido não finge que envia: ou liga num destino aprovado,
  ou abre o WhatsApp com a mensagem preenchida.

### Fase 6 — Verificação

Checklist e script em [references/qa.md](references/qa.md). Mínimo: provar que está olhando o
ambiente certo, prints nas 2 larguras (e 2 esquemas de cor), zero erro de console, zero rolagem
horizontal, e as interações de compra funcionando (variante, adicionar, sacola, frete).
Uma rodada de correção, uma de confirmação; depois pare de polir.

### Fase 7 — Entrega

Link do preview, prints, o que difere de propósito do design (e por quê), pendências do cliente, e o
que **não** foi testado (ex.: envio real do formulário de contato, pagamento). Publicar é decisão
humana.

## Regras de segurança da loja

Elas valem em qualquer projeto e não dependem do usuário lembrar:

- Nunca publicar tema, nunca mexer no tema principal nem no backup: trabalhe num tema de rascunho.
- Nunca apagar catálogo, nunca mudar preço em massa, nunca criar pedido real.
- Menus e páginas que o site no ar usa não mudam; crie menus novos para o tema novo.
- Não enviar formulários reais em teste (contato manda e-mail, newsletter cria cliente).
- Para mudança temporária de teste (zerar estoque para ver o esgotado), registre o valor original
  e reverta na mesma sessão.

## Quando o pedido é menor

- "Só a PDP" / "só o rodapé": pule para a Fase 3 daquela tela, mas ainda use os tokens existentes
  e ainda liste o que falta validar.
- "Deixa bonito" numa loja existente: faça a auditoria da Fase 0 primeiro; o problema costuma
  ser sistema (5 fontes, 4 azuis) e não uma tela.
- Sem Figma: desenhe direto em HTML com o mesmo design system e trate o preview como o Figma.

## Se você não é o Claude (Gemini, GPT, outro)

As regras são as mesmas; o que muda é o hábito de pular leitura. Então:

1. Leia `SKILL.md` e as references da fase em curso **antes** de agir. Não resuma nem adapte
   por conta própria: siga o texto.
2. No Figma, a ficha da seção 1 de `processo-figma.md` vem preenchida na sua primeira resposta
   de trabalho. Sem a ficha, não há escrita.
3. Depois de cada seção montada, mostre o print e o checklist da seção 5 marcado. "Ficou ótimo"
   sem print não conta.
4. Na dúvida entre inventar e perguntar, marque como ilustrativo e ponha na lista "Validar com o
   cliente". Nunca invente preço, prova social nem política.

