# Implementação em tema Shopify

## Arquitetura

- Trabalhe **sempre** num tema de rascunho (`--theme <id>` em todo comando). Tema principal e
  backup não são tocados. `theme publish` é do humano.
- Tema comprado com CSS empilhado: não reestilize o markup dele. Crie seções OS 2.0 próprias com
  prefixo (`xx-hero`, `xx-product`…), um CSS e um JS próprios carregados depois do CSS do tema.
- Reset e estilos com escopo numa raiz (`.xx`), para não quebrar páginas internas do tema
  (conta, carrinho, busca). Liste as classes que colidem com o tema e prefixe só essas.
- Reaproveite a plataforma: templates JSON, section groups, `schema` com settings e blocks
  (tudo editável no personalizador), `image_url`/`image_tag` com `widths`/`sizes`,
  `{% form 'contact' %}`/`{% form 'customer' %}`, `routes`, AJAX Cart API (`/cart.js`,
  `/cart/add.js`, `/cart/change.js`), busca preditiva (`/search/suggest.json`), frete
  (`/cart/prepare_shipping_rates.json` + `async_shipping_rates.json`).
- Arquivos antigos ficam; só saem dos templates e grupos. Nada é apagado.
- Texto de marca vira `default` no schema, não string chumbada no Liquid.

## Páginas do rodapé

- Ajuda: templates de página com sufixo (`page.guia.json`, `page.trocas.json`) e o
  `page.contact.json` para a página de contato existente.
- Políticas não têm template editável. No layout, quando `request.page_type == 'policy'`,
  renderize um snippet próprio no lugar de `content_for_layout`, identificando a política pelo
  último segmento de `request.path` (`privacy-policy`, `refund-policy`, `shipping-policy`,
  `terms-of-service`), e divida `policy.body` em `<h2`.

## Dados via Admin API (`shopify store execute`, `--allow-mutations` para escrever)

- Scripts idempotentes (buscar por handle antes de criar).
- `productSet`: produto existente vai no argumento `identifier: {id}` ou `{handle}`; o input não
  tem mais `id`.
- `inventorySetQuantities` exige `@idempotent(key: "<uuid>")` e compare-and-set por item
  (`changeFromQuantity`).
- A publicação "Online Store" se chama "Loja virtual" em admin pt-BR; filtre pelos dois nomes.
- `files(query: "filename:xx-*")` pega arquivos antigos com o mesmo prefixo; busque por nome exato.
- Menus novos para o tema novo (itens tipo HTTP); os menus que o tema no ar usa não mudam.
- Zona de envio sem nenhuma taxa faz `/cart/add.js` responder 422 "esgotado" para tudo. Parece
  estoque e é frete. Teste de 1 requisição: `POST /cart/add.js` com uma variante.

## Armadilhas de tema

- **Push "com sucesso" que não subiu.** Redirecione a saída para arquivo e procure
  `error|warning|pushed with errors`. O sinal de upload real é a barra "Uploading files". Uma flag
  `--only` por arquivo (lista por vírgula não casa nada).
- **Setting `url` com default `https://…` derruba a seção inteira** e todo template que a usa; o
  storefront segue servindo o antigo. Link externo com default vai em `"type": "text"`.
- **Comparação com texto em inglês** (`filter.label == 'Size'`, `"color, colour"`) nunca casa em
  loja pt-BR e nada acusa. Compare nomes de opção aceitando os dois idiomas, com `strip` em listas
  separadas por vírgula.
- **Bloco Liquid só com espaço some.** `{% unless forloop.last %} {% endunless %}` não imprime o
  espaço; use `{{ ' ' }}`.
- **`fetch('/cart?view=x', {headers:{Accept:'application/json'}})` ignora o `view`** e devolve o
  `/cart.js` padrão.
- **Id duplicado pode ser proposital** (o tema lê com `querySelectorAll`). Antes de "corrigir",
  procure como o JS lê o id.
- **`close` de `<dialog>` não dispara** quando abrir e fechar ocorrem em tarefas diferentes;
  desfaça efeitos observando o atributo `open` com `MutationObserver`.
- `data-sizes` colide com lazysizes; use outro nome.

## Tema com mapa

Se o tema traz um mapa gerado do código (ex.: `docs/MAPA-DO-TEMA.md`, `AGENTS.md`), ele manda
sobre as regras genéricas deste arquivo:

1. Leia o mapa e o `AGENTS.md` **antes da Fase 3**. Para cada componente do Figma (barra de
   frete, compre junto, kit, barra de anúncio com cupom, menu inferior…), anote a section, o
   bloco e os settings que já o implementam. Nomeie o frame do Figma com esse nome.
2. Só desenhe componente sem par no mapa se ele for necessário; ele vira section nova no padrão
   do tema, não CSS por cima.
3. Antes de ligar um bloco de urgência, prova ou pagamento, leia o código dele (ver
   [conversao.md](conversao.md), "Prova e urgência"). Tema pronto costuma ter contador sorteado.
4. Rode os gates do próprio tema (validador, selfcheck, `shopify theme check`, verificação do
   mapa) antes de dizer "pronto".

## Checkout, página de obrigado e pós-compra

A análise das 19 lojas parou na sacola: nenhum checkout foi aberto nem pedido criado. O que
segue é a regra da plataforma, não padrão observado. **Confira a documentação da Shopify na data
do projeto**; os limites por plano mudaram várias vezes desde 2023.

- **Checkout nativo:** marca (logo, cores, fontes, botões) pelo editor de checkout. Bloco ou campo
  novo nas etapas de informação, entrega e pagamento (order bump, seguro de envio, brinde) é
  extensão de checkout e depende do plano. Não desenhe checkout customizado sem confirmar o plano;
  onde não der, o bump vai para o "compre junto" da PDP ou para a sacola.
- **Página de obrigado e status do pedido:** personalizáveis por extensão de app. Lugar de
  cashback que o pedido rendeu, cupom da próxima compra, convite para avaliar e para o programa.
- **Oferta pós-compra de 1 clique** (entre o pagamento e o obrigado): só por app com extensão de
  pós-compra (Woly tem o ReConvert). Um item, preço visível, "Adicionar ao pedido" e "Não,
  obrigado" com o mesmo peso.
- **Checkout externo brasileiro** (Yampi, Appmax, CartPanda): o layout mora no painel do checkout,
  não no tema. O Figma entrega tokens (logo, cor, fonte), textos e a lista de bumps/brindes que o
  painel suporta. Esse checkout pode ignorar o desconto do carrinho e aplicar regras próprias: meça
  o valor final pelo endpoint dele (sem criar pedido) antes de exibir economia na sacola.
- **E-mails transacionais e carrinho abandonado:** templates de notificação da Shopify (ou da
  ferramenta de e-mail). Mesmo logo, cor de acento e tom de voz da loja; foto do item, preço, um
  botão. Cupom no e-mail de abandono só se a regra existir no desconto.
