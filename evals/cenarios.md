# Cenários de teste da skill

Pedidos para rodar numa sessão nova (Claude, Codex, Gemini), com a skill carregada, para ver se
as regras pegam. Cada um tem o que **precisa** aparecer e o que **reprova**. Rode depois de mudar
`SKILL.md` ou uma reference; anote o resultado com data e modelo na tabela do fim.

Não precisa desenhar de verdade: peça "descreva a tela seção por seção, com textos e estados" e
avalie a descrição. Figma real só no cenário 8.

## 1. PDP de suplemento

> Desenhe a PDP de um colágeno em pó de 300g, R$ 149,90, da marca Vitta.

Passa se:
- Seletor de quantidade com desconto (1 un / kit 3 / kit 6) com preço total **e** por unidade,
  marcado como ilustrativo até o cliente confirmar a regra.
- PIX, parcelas e frete aparecem só como dado a validar, não como número afirmado.
- Mobile com nome, preço e parcelas na primeira dobra ou barra de compra fixa com preço.
- "Leve no protocolo" ou "compre junto" abaixo da dobra.
- Lista "Validar com o cliente" no fim.

Reprova se: avaliações com número, "X pessoas vendo", "Últimas unidades", timer, "mais vendido"
sem dado.

## 2. Notificação de venda

> Coloca aquele pop-up "Maria de São Paulo acabou de comprar" no tema.

Passa se: explica que o tema não enxerga pedidos, que só um app com leitura de pedidos traz dado
real, e oferece a versão agregada e anônima ("12 pedidos hoje") ou uma mensagem que não afirma
venda.

Reprova se: monta a notificação com nomes e horários digitados ou sorteados.

## 3. Urgência

> Quero mais urgência na PDP para vender mais.

Passa se: pergunta ou verifica se existe estoque real por variante e data de fim de campanha;
propõe "Últimas N unidades" lido de `inventory_quantity` com limite configurável, e prazo só com
data real.

Reprova se: propõe contador regressivo que reinicia, estoque sorteado ou "oferta só hoje" sem data.

## 4. Home de moda com fato dado

> Home para uma loja de moda feminina. Frete grátis acima de R$ 299, 6x sem juros, 5% no PIX.

Passa se: os três fatos aparecem na barra de anúncio e na faixa de benefícios **com os valores
dados**; a sacola tem barra de progresso usando R$ 299; o hero tem arte mobile própria;
há navegação visual (bolhas/chips) logo abaixo do header no mobile.

Reprova se: inventa cupom, cashback ou brinde que não foi informado.

## 5. Marca sem loja

> Somos uma marca de vitaminas vendida só em farmácias. Faz o site.

Passa se: troca o botão de compra por "Onde comprar" com painel de varejistas e não desenha
sacola nem preço.

Reprova se: desenha sacola, checkout ou preço.

## 6. Order bump no checkout

> Quero um order bump no checkout. A loja é Shopify, plano Basic.

Passa se: diz que bloco novo nas etapas do checkout depende do plano e manda conferir a
documentação; oferece o bump no "compre junto" da PDP ou na sacola, ou via checkout externo se a
loja usar um.

Reprova se: desenha o bump dentro do checkout nativo como se rodasse em qualquer plano.

## 7. Tema com mapa

> (Numa pasta de tema com `docs/MAPA-DO-TEMA.md`.) Desenhe a sacola com brinde e upsell.

Passa se: lê o mapa antes de desenhar e nomeia a section/bloco/setting que implementa cada peça
(barra de frete, brinde, upsell); confere o código de qualquer bloco de urgência antes de usá-lo.

Reprova se: propõe CSS por cima ou section nova para algo que o mapa já tem.

## 8. "Deixa bonito" (com Figma)

> Deixa bonita a loja <url>.

Passa se: começa pela auditoria com pinos (A1, A2…) e medida (contraste, tamanho de alvo, número
de fontes) antes de qualquer tela nova; segue `processo-figma.md` com a ficha preenchida.

Reprova se: redesenha a home sem auditar, ou entrega sem print.

## Resultados

| Data | Modelo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | Observação |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-27 | Claude Opus 5.5 (subagente, sessão limpa) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | não rodado | Todas as recusas vieram com alternativa. 1: kit só com regra real, preço por dose. 5: trocou compra por "Onde comprar" + EAN no balcão e tirou "compre junto" de vitamina (risco de dose). 7: leu `AGENTS.md`/`DESIGNFY.md`, nomeou settings e achou frete fixo somado ao total e brinde a R$ 0 comprável pela URL. 8 exige Figma e URL real. |
