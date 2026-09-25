# Verificação antes de entregar

## 1. Estou olhando o ambiente certo?

- Shopify: preview de tema funciona por cookie gravado num redirect. Um `fetch` com redirect
  automático perde o cookie e devolve o **tema publicado** — tudo que é novo "não aparece" e parece
  bug. Primeira asserção de todo teste: `Shopify.theme.id` no HTML == id do rascunho.
- Site estático sob subpasta: `url()` dentro do CSS resolve contra o arquivo CSS, não contra
  `<base href>`; fonte cai no fallback sem erro visível (só 404 no console). Âncora `#x` também
  resolve contra a base.
- Deploy novo: confira que a URL serve o commit/versão esperado (cache `immutable` em asset sem
  versão segura o CSS velho por um ano).

## 2. Varredura visual

`scripts/qa_loja.py` (Playwright, Chrome): para cada página × 1440/390 × claro/escuro, tira print
de página inteira e checa HTTP, um único `h1`, rolagem horizontal, imagem quebrada, alvo de toque
pequeno e erro de JS.

```bash
python3 <pasta-do-guia>/scripts/qa_loja.py https://loja.myshopify.com \
  / /collections/all /products/<handle> /cart /search?q=x /pages/contact /policies/refund-policy /404 \
  --theme-id <id-do-rascunho> --out <scratchpad>/shots
```

Depois **abra os prints**. Métrica de caixa não pega palavras coladas ("NOMEDAMARCA"), texto que
sumiu no escuro nem foto cortada. Compare com o Figma lado a lado; se houver preview de referência,
compare também `textContent` e largura do texto, não só o bbox.

## 3. Interações de compra (escreva o teste para o tema em questão)

- Variante: escolher cor/tamanho troca preço, foto e disponibilidade; indisponível desabilitado.
- Adicionar: contador da sacola sobe, confirmação aparece, `/cart.js` bate com a tela.
- Sacola: +/−/remover batem com `/cart.js`; CEP válido mostra frete real, inválido mostra erro
  claro; botão leva a `/checkouts/` (não pagar).
- Busca: um termo real acha o produto; termo sem resultado mostra o estado vazio.
- Menu, painéis e dropdown: abrem, fecham com Esc e clique fora, travam a rolagem do fundo.
- Cookies: antes da escolha nada liberado; Recusar = nada; Salvar com só Analíticos = análise sim,
  marketing não; "Preferências" reabre o painel.
- Âncoras (`#guia`, `#trocas`) abrem o acordeão certo.
- Estados raros: forçar temporariamente (produto esgotado, coleção com mais itens, menu com
  subitem), verificar, e **reverter** na mesma sessão.

Não testar com envio real: formulário de contato (manda e-mail), newsletter e avise-me (criam
cliente), pagamento.

## 4. Limite

Uma rodada de correção, uma de confirmação. Registre o que ficou diferente de propósito e o que não
foi testado, e pare.
