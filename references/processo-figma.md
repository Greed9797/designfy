# Processo de desenho no Figma — o passo a passo exato

Leia este arquivo **inteiro** antes da primeira escrita no Figma. Não é sugestão de estilo: é a
sequência que produz tela de estúdio. Pular etapa é o que faz o resultado parecer template de 2014.

A regra que resume tudo: **montar, não desenhar.** Tela boa sai de peças que já existem no arquivo
(componentes, variáveis, estilos de texto, molduras de página já aprovadas) encaixadas em
auto-layout, com dado real, conferida por print. Tela ruim sai de retângulos soltos com cor em hex,
fonte padrão e texto inventado.

## 0. Descubra que ferramenta você tem

| Modo | Como reconhecer | Como trabalhar |
|---|---|---|
| **A — script** | existe uma ferramenta que executa JavaScript da Plugin API (`use_figma` do MCP oficial, ou parecida) | um script por seção, seguindo a seção 4A |
| **B — ferramentas granulares** | ferramentas separadas tipo `create_frame`, `create_text`, `clone_node`, `set_fill_color`, `set_layout_mode` (talk-to-figma / cursor-talk-to-figma) | **clonar e editar**, seguindo a seção 4B |
| **Só leitura** | só há `get_design_context`, `get_screenshot`, Framelink e similares | não desenhe; descreva a tela e peça uma ferramenta de escrita |

No modo B há duas armadilhas que sozinhas explicam a maior parte do resultado feio:
`create_text` cria o texto **sempre em Inter**, sem estilo de texto, e `set_fill_color` grava cor
crua, sem variável. Por isso no modo B quase nada se cria do zero: clona-se um nó que já tem a
fonte, o estilo e a cor certos, e só se troca o conteúdo.

## 1. Portão de descoberta (só leitura, antes de qualquer escrita)

Preencha esta ficha antes de criar qualquer nó. Sem ela, **não escreva**.

```
Arquivo: <fileKey>        Páginas: <nome → id>
Moldura existente: header <id>, rodapé <id>, página modelo <id> (slot de conteúdo <id>)
Componentes: <nome> <id/key> — propriedades: {"Rótulo#12:3": TEXT, "Ícone#12:5": BOOLEAN, "Estado": VARIANT[a|b]}
Variáveis de cor: <coleção> — <nome> <id> (papel: fundo, superfície, tinta, tinta-suave, borda, acento…)
Variáveis de espaço/raio: <nome> <valor>
Estilos de texto: <nome> <id> (família, estilo, tamanho)
Fontes da marca: <família> <estilos exatos, ex.: "Semi Bold" e não "SemiBold">
Imagens já no arquivo: <nó> <imageHash> (página 99 Assets)
```

- Modo A: um script de leitura que devolve páginas, `getLocalVariablesAsync()`,
  `getLocalTextStylesAsync()`, componentes com `componentPropertyDefinitions` (lidas do
  COMPONENT_SET ou do componente solto, nunca de uma variante) e as instâncias de uma tela já
  pronta. Variável de biblioteca remota não aparece em `getLocalVariablesAsync`; procure também
  pelas instâncias de uma tela existente.
- Modo B: `get_document_info`, `get_local_components`, `get_styles`,
  `scan_nodes_by_types` (TEXT e INSTANCE numa tela pronta), `get_instance_overrides`.
- **Anote o tipo de cada propriedade.** Mandar texto para uma propriedade BOOLEAN dá
  "incompatible type"; a chave inclui o sufixo (`Ver mais#15:6`), e o nome sem sufixo não funciona.
- Se o arquivo não tem design system, pare aqui e faça a Fase 2 do `SKILL.md` primeiro.
  Tela sem sistema é justamente o que se quer evitar.

## 2. Dados reais antes da tela

- Tire os dados da loja de verdade: nome, preço, parcelamento, desconto no PIX, variantes,
  fotos, textos de política. Dá para ler do site no ar (Playwright ou navegador), da API da
  plataforma ou de um export. Guarde num JSON; é ele que alimenta os scripts.
- Imagens: suba **uma vez** (JPG ou PNG; WebP ganha hash mas não renderiza) em retângulos na
  página `99 Assets`. Depois reaproveite o `imageHash` (modo A) ou chame `set_image_fill` com o
  caminho do arquivo local (modo B).
- Dado que falta ganha valor ilustrativo **marcado** e vai para a lista "Validar com o cliente".
  Nunca "Produto 1 · R$ 99,90", nunca lorem ipsum, nunca estrelas ou depoimentos inventados.

## 3. Moldura antes do conteúdo

- Página nova = **clone** da moldura aprovada (header + slot + rodapé) e esvaziamento do slot.
  Refazer header e rodapé à mão gera um terceiro header ligeiramente diferente dos outros dois.
- Desktop 1440 e mobile 390, cada um com auto-layout vertical e nome legível
  (`Catálogo — Desktop`, `Catálogo — Mobile`).
- Nó novo no topo da página vai à direita do que já existe, nunca em (0,0) por cima de outro.
- Estados (drawer aberto, vazio, esgotado, filtro aberto) ficam **ao lado** da tela principal,
  como frames próprios com o mesmo nome e um sufixo.

## 4. Construir uma seção por vez

Regras de layout, que valem nos dois modos:

1. **Auto-layout em tudo que tem filhos relacionados.** Posição absoluta só para sobreposição
   real (selo sobre a foto, botão fechar do drawer).
2. **Anexe primeiro, depois defina FILL/HUG.** Nó fora de um pai com auto-layout recusa FILL.
3. **`resize()` antes de `layoutSizing*`**: o `resize` volta os dois eixos para FIXED.
4. **Texto que quebra linha** = largura FILL (ou fixa) **e** `textAutoResize = 'HEIGHT'`.
   Só FILL com o modo padrão encolhe o texto até virar um fio.
5. **Larguras calculadas, não chutadas.** Conteúdo = 1440 − 2 × margem. Coluna de grade =
   (conteúdo − (n − 1) × gap) / n. Mobile: 390 − 2 × 16.
6. **Coluna de leitura com limite** (~720–760 px) em texto longo: políticas, sobre, guia de medidas.
7. **Tabela com coluna de largura fixa** (quantidade, preço, total) envolvida num frame fixo, para
   o cabeçalho não quebrar.
8. **Cards da mesma linha com a mesma altura**: linha HORIZONTAL e cada card com
   `layoutSizingVertical = 'FILL'`.
9. **Cor sempre ligada a variável e texto sempre com estilo de texto.** Hex solto só em
   `99 Assets`.
10. **Componente em vez de cópia.** Botão, card de produto, campo, selo e chip são instâncias
    configuradas com as chaves exatas da ficha.
11. **Filho de instância não aceita `resize`, `x` nem `appendChild`.** Se a instância precisa
    esticar, o erro está no componente principal (filho FIXED que devia ser FILL): corrija o
    principal e todas as instâncias se ajustam. Não desanexe instância para contornar.

### 4A. Modo script

Uma chamada por seção (ou por página, quando ela é simples). Cada chamada precisa ser **segura
para repetir**: se já rodou, ela recusa em vez de duplicar. E toda chamada devolve os ids que criou.

```js
// Seção "Grade" do catálogo desktop. Segura para repetir.
const SLOT = '<id do slot, copiado da ficha>';
const slot = await figma.getNodeByIdAsync(SLOT);
if (!slot) throw new Error('slot não encontrado');
if (slot.findOne(n => n.name === 'Grade')) throw new Error('Grade já existe: leia o canvas antes de repetir');

const estilos = await figma.getLocalTextStylesAsync();
const S = Object.fromEntries(estilos.map(s => [s.name, s]));
await figma.loadFontAsync({ family: 'Inter', style: 'Regular' }); // fonte de nascença do createText
await Promise.all(estilos.map(s => figma.loadFontAsync(s.fontName)));

const cores = await figma.variables.getLocalVariablesAsync('COLOR');
const V = Object.fromEntries(cores.map(v => [v.name, v]));
const tinta = nome => {
  if (!V[nome]) throw new Error('variável inexistente: ' + nome);
  return [figma.variables.setBoundVariableForPaint({ type: 'SOLID', color: { r: 0, g: 0, b: 0 } }, 'color', V[nome])];
};

const caixa = (nome, dir, gap = 0, pad = 0) => {
  const f = figma.createFrame();
  f.name = nome; f.layoutMode = dir; f.itemSpacing = gap;
  f.paddingTop = f.paddingBottom = f.paddingLeft = f.paddingRight = pad;
  f.primaryAxisSizingMode = 'AUTO'; f.counterAxisSizingMode = 'AUTO'; f.fills = [];
  return f;
};
const texto = async (conteudo, estilo, cor) => {
  const t = figma.createText();
  await t.setTextStyleIdAsync(S[estilo].id);
  t.characters = conteudo; t.fills = tinta(cor);
  return t;
};
const poe = (pai, filho, h, v) => {
  pai.appendChild(filho);
  if (h) filho.layoutSizingHorizontal = h;
  if (v) filho.layoutSizingVertical = v;
  return filho;
};

const criados = [];
const grade = poe(slot, caixa('Grade', 'VERTICAL', 24), 'FILL');
criados.push(grade.id);
// ... linhas HORIZONTAL com instâncias do card, dados vindos do JSON colado aqui ...
// texto que quebra: const p = poe(linha, await texto(d.nome, 'Corpo/M', 'tinta'), 'FILL'); p.textAutoResize = 'HEIGHT';
return { criados, slot: SLOT };
```

- Se a chamada der erro, **leia o canvas** antes de tentar de novo, a não ser que o erro diga que
  nada foi escrito. Repetir às cegas cria duplicata.
- Script gigante que monta a página inteira e quebra no meio deixa a tela pela metade e
  impossível de repetir. Divida por seção.

### 4B. Modo ferramentas granulares (talk-to-figma e afins)

1. **Monte um kit.** Da ficha, separe um nó de cada peça que já existe com fonte, estilo e cor
   certos: título de seção, parágrafo, preço, rótulo pequeno, botão, card de produto, chip,
   divisória. Esses são os moldes.
2. **Texto novo = `clone_node` de um texto do kit** + `set_parent` no lugar certo +
   `set_text_content`. Várias trocas de uma vez: `set_multiple_text_contents`.
   Não use `create_text`: ele sai em Inter e sem estilo.
3. **Peça repetida = `create_component_instance`** (id local ou key publicada) +
   `set_instance_overrides` ou `set_text_content` nos textos da instância.
4. **Contêiner novo**: `create_frame` + `set_layout_mode` + `set_padding` + `set_item_spacing` +
   `set_axis_align`, e só depois `set_layout_sizing` nos filhos (FILL só dentro de pai com
   auto-layout). Melhor ainda: clone uma seção parecida já pronta e troque o conteúdo.
5. **Cor**: herde clonando um nó que já tem a cor vinculada. Se não houver jeito e precisar usar
   `set_fill_color`, use o valor exato da tabela de tokens (nunca um tom "parecido") e anote o nó
   na lista "Débito de token", para alguém religar à variável depois.
6. **Imagem**: `set_image_fill` com `imagePath` do arquivo local (JPG/PNG).
7. **Print**: `export_node_as_image` na seção inteira depois de montar (seção 5).

## 5. Olhe o que fez — print depois de cada composição

Tire um print da seção ou da tela (modo A: `get_screenshot`; modo B: `export_node_as_image`) e
procure, nesta ordem:

- [ ] Rótulo curto quebrando em duas linhas ou cortado ("Quantida-de", "Frete grá…").
- [ ] Texto padrão do componente sobrando ("Title", "Button", "Label").
- [ ] Fonte errada: Inter ou Roboto onde a marca usa outra.
- [ ] Imagem cinza ou vazia.
- [ ] Cards da mesma linha com alturas diferentes; preço desalinhado entre cards.
- [ ] Conteúdo saindo do frame (1440 ou 390) ou rolagem horizontal no mobile.
- [ ] Elementos colados sem respiro, ou buracos enormes porque um filho ficou FIXED.
- [ ] Bordas das seções desalinhadas (cada seção com uma margem diferente).
- [ ] Contraste: texto sobre o acento, texto cinza-claro sobre branco.
- [ ] Hierarquia: dá para achar em 2 segundos o nome, o preço e o botão de compra?

Corrigiu, tire **um** print de confirmação e pare. Polir sem fim também é defeito.

## 6. Uma página validada, depois em lote

Monte a primeira página completa, passe pelo checklist da seção 5 e só então transforme o
script numa função que recebe os dados (título, blocos, textos) e rode uma chamada por página.
Nove páginas feitas de uma vez sem a primeira validada viram nove páginas com o mesmo defeito.

## 7. Padrões que se repetem

- **Mobile não é o desktop espremido**: menu lateral vira fila de chips com rolagem horizontal,
  grade de 4 vira 2, filtro vira painel que sobe de baixo, barra de compra fixa no pé da PDP
  (desenhada ao lado do frame, com nota "fixa ao rolar"), blocos longos viram acordeão.
- **Estados como frames irmãos**: sacola vazia, sacola com itens, drawer aberto, esgotado com
  "avise-me", sem resultado de busca, erro de CEP.
- **Nota ao lado de cada tela**, fora do frame:
  - *Origem dos dados*: de onde veio cada número (site no ar, API, cliente).
  - *Validar com o cliente*: o que é ilustrativo ou suposto.
  - *Comportamento*: o que é fixo, o que anima, o que some quando o dado está vazio.

## 8. Antes de dizer "pronto"

Responda sim a tudo, com o print na mão:

1. Toda cor da tela está ligada a variável (ou listada em "Débito de token")?
2. Todo texto usa um estilo de texto da marca?
3. Botão, card, campo e chip são instâncias de componente?
4. Todo número e todo texto vêm de fonte real ou estão marcados como ilustrativos?
5. Existem desktop 1440 **e** mobile 390, cada um composto para a sua largura?
6. O checklist da seção 5 passou no último print?
7. Estão entregues os ids ou links dos frames e a lista "Validar com o cliente"?

## Por que outros modelos geram tela feia

| Sintoma | Causa | Regra que evita |
|---|---|---|
| Tudo em Inter, tamanhos aleatórios | texto criado do zero, sem estilo | 4.9, 4B.2 |
| Cores "quase" da marca, cinco cinzas | hex digitado a olho | 4.9, 4B.5 |
| Elementos sobrepostos ou tortos | posição absoluta em vez de auto-layout | 4.1 |
| Texto virou um fio vertical | FILL sem `textAutoResize = 'HEIGHT'` | 4.4 |
| Header diferente em cada página | moldura redesenhada à mão | 3 |
| "Produto 1 · R$ 99,90", lorem, 5 estrelas | dado inventado | 2 |
| Ícone de emoji, degradê e sombra em tudo | enfeite no lugar de sistema | `SKILL.md`, princípio 4 |
| Tela pela metade e duplicatas | um script gigante repetido às cegas | 4A |
| Mobile ilegível | desktop encolhido para 390 | 7 |
| Defeito visível entregue | ninguém olhou o print | 5 |
