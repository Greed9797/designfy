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

## Checkout externo

Se o checkout é de terceiro, ele pode ignorar o desconto do carrinho e aplicar regras próprias.
Meça o valor final pelo endpoint do checkout (sem criar pedido) antes de exibir economia na sacola.
