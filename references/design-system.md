# Design system de loja

## Cores: papéis, não nomes

Nomeie pelo papel. "azul-500" não diz onde usar; `ink` diz.

| Papel | Uso | Exemplo (streetwear claro) |
|---|---|---|
| `ink` | texto principal, botão primário, fundos escuros | #111111 |
| `paper` | fundo da página | #F5F5F5 |
| `stone` | fundo atrás da foto do produto | #EDEDED |
| `line` | bordas, divisores, inputs | #D6D6D6 |
| `mute` | texto secundário (conferir 4,5:1 sobre `paper`) | #6B6B6B |
| `accent` | **só sinal**: foco, selecionado, selo "novo", progresso | um tom da marca |
| `white` | texto sobre `ink` | #FFFFFF |

- Um acento. Se ele aparece em título, botão, ícone e fundo ao mesmo tempo, deixou de sinalizar.
- Acento claro (laranja, amarelo, azul-gelo): texto sobre ele em preto. Branco sobre laranja
  #F76B00 dá 2,98:1 e reprova.
- Translucidez (scrim, linha sobre escuro) vira token sólido próprio (`on-dark-line` #3F3F3B em vez
  de "branco a 30%") — é mais previsível no Figma e no CSS.

## Modo claro e escuro

Faça o escuro como **modo** da mesma coleção de variáveis (Claro / Escuro), não como cópia pintada
à mão. Aí aparece o problema: algumas áreas **não podem** inverter.

- Sobre foto, sobre scrim escuro e dentro de faixas já escuras (rodapé preto, barra de anúncio), o
  texto precisa continuar claro nos dois modos. Crie tokens **fixos** (`cor/fixo/ink`,
  `cor/fixo/paper`, …) que têm o mesmo valor nos dois modos, e use-os nesses contextos.
- Faixas que são "o contrário da página" (rodapé, sacola, painel de cookies) usam um token
  **inverso** (`superficie-inversa`): escuro no claro, e um cinza-escuro distinto do fundo no
  escuro, para não sumirem.
- O acento raramente muda entre modos; confira contraste nos dois.
- No site: `prefers-color-scheme` define o inicial, um botão sol/lua alterna, a escolha fica em
  `localStorage`, e o atributo é aplicado no `<html>` **antes** da primeira pintura (script inline
  no `<head>`) para não piscar.

## Tipografia

- 1 família (2 no máximo: display + texto). Carregue só os pesos usados — e confirme que o peso do
  display (ex.: 900) está de fato carregado; a falta dele cai no 700 sem erro.
- Estilos de texto nomeados por função: `Display/Hero`, `Título/Seção`, `Título/Produto`,
  `Card/Nome`, `Preço`, `UI/Rótulo` (caixa-alta, 11–12px, tracking), `Corpo`, `Pequeno`.
- Números de preço com `font-variant-numeric: tabular-nums` quando alinhados em coluna.

## Espaço, raio, grid

- Escala 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128. Nada fora dela.
- Um raio (0 para marca seca, 8–16 para marca amigável). Raio diferente = componente diferente.
- Desktop 1440: margem 40–64, grid de 12. Mobile 390: margem 16–20, grid de 4.
- Alvo de toque ≥ 44px no mobile.

## Componentes mínimos

Botão (primário, secundário, inverso, link × tamanhos × estados), campo (padrão, foco, erro),
chip de variante (disponível, selecionado, indisponível), card de produto (com 2ª foto, selo,
esgotado), selo, header (desktop/mobile × repouso/rolado), ticker/barra de anúncio, rodapé,
painel (menu, busca, sacola), acordeão, banner e painel de cookies.

Componente com texto editável usa **propriedades de texto** (Nome, Preço, Selo…), para as telas
serem instâncias e não cópias soltas. Mudou o componente, mudou tudo.

## Movimento

Pouco e com função: header que encolhe ao rolar, 2ª foto no hover, painel que desliza, confirmação
de "adicionado". 150–250ms, easing de saída. Tudo desliga com `prefers-reduced-motion`.
Vídeo que avança com a rolagem é sequência de frames em `<canvas>`, não `<video>` com
`currentTime` (engasga); e a página precisa estar completa com um pôster estático se o vídeo faltar.
