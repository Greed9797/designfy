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

## Catálogo

- Cabeçalho: breadcrumb, título, contagem real ("12 peças"), ordenar (usar a ordenação nativa).
- Filtros: no desktop, barra ou lateral; no mobile, painel com "Ver N resultados". Contagens reais
  por faceta; filtro sem resultado desabilitado, não escondido.
- Grid 3–4 no desktop, 2 no mobile. 2ª foto no hover (desktop).
- Adição rápida por tamanho no card é ótima para moda; indisponível aparece riscado/desabilitado.
- Estados: vazio (com saída), "mostrando X de Y" + paginação ou carregar mais.

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

## Sacola (drawer)

Itens com variante, +/−, remover; subtotal; calculadora de CEP com frete **real** da plataforma
(com mensagem clara quando falha); condições (PIX, parcelas); botão para o checkout. Nunca somar um
frete fixo chumbado no tema. Se há desconto automático, mostre o valor que a plataforma calculou
(`total_discount`), nunca recalcule — o total já vem líquido e recalcular desconta duas vezes.

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

## Cookies (LGPD)

- Banner: Aceitar todos · Recusar · Preferências. Os três com o mesmo peso de escolha.
- Painel: Necessários (sempre ativos, sem interruptor), Analíticos e Marketing **desligados por
  padrão** (consentimento é opt-in), Recusar · Salvar escolhas · Aceitar todos.
- Nada de script de análise/marketing antes da escolha. Teste: antes da escolha nada liberado;
  Recusar = nada; Salvar só com Analíticos = análise sim, marketing não.
- Link "Preferências de cookies" no rodapé e na aba de políticas reabre o painel.

## 404

Título humano, busca, link para o catálogo. Mesmo header e rodapé.
