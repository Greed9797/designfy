# Figma para loja

O passo a passo de montagem de tela (descoberta, dado real, moldura, uma seção por chamada,
print e checklist) está em [processo-figma.md](processo-figma.md). Leia ele primeiro; este
arquivo complementa com a estrutura do arquivo e as armadilhas.

Antes de escrever na Plugin API, leia a documentação de Plugin API do seu agente (no Claude Code, as skills `figma-use` e `figma-generate-design` para
telas inteiras). Este arquivo traz só o que é específico de loja e as armadilhas que já custaram
rodadas.

## Estrutura do arquivo

| Página | Conteúdo |
|---|---|
| 00 Capa & Auditoria | fatos, achados A1…Dn (problema · evidência medida · solução), lista "Validar com o cliente" |
| 01 Site atual | capturas desktop e mobile do site no ar, com pinos numerados ligados aos achados |
| 02 Referências | capturas das referências com nota do que se empresta de cada uma (só estrutura) |
| 03 Design System | coleção de variáveis (modos Claro/Escuro), estilos de texto, componentes |
| 04 Desktop 1440 | uma seção por página da jornada, estados ao lado |
| 05 Mobile 390 | idem, + protótipo do fluxo Home → Catálogo → Filtro → Produto → Sacola |
| 99 Assets | fotos e imagens usadas (JPG/PNG) |

Nas telas, uma nota de comportamento ao lado (o que anima, o que é sticky, o que some quando o dado
está vazio) vale mais que dez frames de estado.

Versões alternativas (V1, V2, V3) em páginas próprias; a rejeitada fica com opacidade reduzida em
vez de apagada, para a conversa com o cliente ter histórico.

## Receita: versão escura por modo de variável

1. Clone a seção clara e defina o modo Escuro na coleção — numa chamada.
2. Em **outra** chamada, remapeie o contexto. Para cada nó não-texto, classifique:
   - `foto` (fill de imagem), `acento`, `scrim` (fill `ink` com opacidade < 1 e largura ≥ 300),
     `inversa` (fill `ink` grande, ≥ 300×120).
   - Descendentes e irmãos posteriores sobrepostos a esses nós passam a usar os tokens **fixos**
     (o texto sobre a foto continua claro).
   - Fills `inversa` passam para `superficie-inversa`.
3. Screenshot das duas versões lado a lado; procure texto que sumiu.

## Armadilhas da Plugin API

- **Paint vinculada a variável perde a opacidade.** Atribuir `opacity` antes, depois ou via spread
  não funciona: lê de volta 1. Scrim = fill sólido vinculado + `node.opacity`; linha translúcida =
  token sólido dedicado.
- **Filho de instância não aceita `x`** ("relative-transform"). Se o ajuste é estrutural, corrija
  o componente principal e reaplique as instâncias. **Não** desanexe as instâncias para contornar:
  isso congela a divergência e o próximo ajuste do componente não chega nelas.
- **WebP enviado ganha hash mas não renderiza.** Suba JPG/PNG.
- Fonte precisa estar carregada antes de qualquer mudança em nó de texto (inclusive trocar modo).
- Captura do site ao vivo pode não reproduzir `background-blend-mode` e afins; anote na auditoria
  em vez de "corrigir" a captura.

## Handoff para código

Um mapa Figma → código com uma linha por componente: nó do Figma, arquivo de destino, status
(✅ já existe e só configura · 🟡 base existe, adaptar · 🔴 código novo · ⚙️ dado na loja, não é
código). Esse mapa é o que impede de reimplementar algo que o tema já faz, e é o que mostra ao
cliente o tamanho real do trabalho.
