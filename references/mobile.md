# Mobile: o que as lojas fazem na tela de 390

Medido nas capturas 390×844 da primeira dobra (home e PDP) das 19 lojas de
[lojas-referencia.md](lojas-referencia.md), em 2026-09. Mobile não é o desktop encolhido: é onde
a maior parte da compra acontece, e onde os erros mais caros aparecem (coisa cobrindo a tela,
botão fora do alcance, preço abaixo da dobra).

## Primeira dobra da PDP: nome, preço e ação sem rolar

- **Preço visível sem rolar** em Amaro, Galeroca, Kylie, Loft 111, Maxme, Modab, Mondepars,
  PantryShop e Stanley; Boca Rosa e Bold resolvem com barra fixa (abaixo). Galeroca e Kylie põem
  quantidade e "Adicionar" na primeira dobra também.
- **Foto que empurra tudo para baixo:** Woly, Shark e Pretorian mostram foto + miniaturas e o
  nome só no pé da tela; o preço fica para depois da rolagem.
- Regra: foto em no máximo ~60% da altura (≈ 500px em 844), com nome, preço e parcelas visíveis;
  ou barra de compra fixa com preço.

## Barra de compra fixa

Boca Rosa (nome + preço + "Comprar"), Bold (preço + "Comprar"), Maxme ("Adicionar ao carrinho")
e Woly ("Comprar", acima do menu inferior).

- Aparece quando o botão principal sai da tela; some quando ele volta.
- Mostra o preço. Um botão sem preço obriga o cliente a rolar de volta para conferir.
- Produto com variante sem escolha: o toque rola até o seletor ou abre um painel de opções.
  Nunca adiciona uma variante padrão em silêncio.
- No Figma: desenhe o estado com a barra, não só o topo da PDP.

## Menu inferior fixo (tab bar)

Aparece em 7 das 19 lojas, **todas brasileiras**, nenhuma internacional:

| Loja | Itens |
|---|---|
| Bold | Início, Categorias, Compra rápida, Promos, Carrinho |
| Maxme | Home, Buscar, Compra rápida, Entrar, Carrinho |
| Woly | Home, Pesquisa, Compre pelo WhatsApp, Conta, Cashback |
| Shark | Início, Busca, Entrar, Carrinho |
| Mondepars | Home, Meu perfil, Sacola |
| Pretorian | Pesquisa, Minha conta, Carrinho |
| Embelleze | barra presente, parcialmente escondida pelo banner de cookies na captura |

- 3 a 5 itens, sempre com ícone **e** rótulo, alvo ≥ 44px, contador na sacola.
- Respeita a área segura do iPhone (`padding-bottom: env(safe-area-inset-bottom)`).
- Visível desde o primeiro acesso. Tema que só mostra a barra depois de rolar X px some com ela em
  página curta (sacola, conta, política) justamente onde ela ajuda a sair.
- O item do meio pode ser a ação da marca ("Compra rápida" na Bold e na Maxme, "Compre pelo
  WhatsApp" na Woly), não mais um link repetido do header.
- Barra fixa de compra + menu inferior empilhados (Woly) comem ~130px: some com um dos dois na
  PDP ou encolha o menu enquanto a barra de compra estiver visível.

## O que cobre a tela no primeiro acesso

6 das 19 lojas cobrem conteúdo com algo na primeira carga do celular:

- Pop-up de cupom do app cobrindo home e PDP (Decathlon).
- Pedido de permissão de notificação no topo da home (Boca Rosa).
- Formulário de cadastro com 5 campos logo ao abrir (Maxme).
- Pop-up "Are you in the right place?" de país (Gymshark).
- Banner de cookies tomando a metade inferior da tela (Real Madrid) ou somado a um pop-up de
  "clientes de olho" (Embelleze).

Regras:

- Cookies (LGPD): faixa no pé com no máximo ~25% da altura, "Aceitar" e "Recusar" com o mesmo
  peso visual, link para preferências.
- Cadastro/cupom: depois de interação (rolagem, 2ª página) ou por um botão na barra de anúncio;
  nunca na primeira dobra do primeiro acesso.
- País/idioma: detecte e ofereça numa faixa discreta; modal só se o preço ou o envio mudam.
- Uma interrupção por vez. Cookies + cadastro + chat abertos juntos = página ilegível.

## Header e navegação

- Padrão da maioria: menu à esquerda, logo ao centro, busca/conta/sacola à direita.
- **Campo de busca visível** sob o header em Amaro, Decathlon, Embelleze e Real Madrid, todas de
  catálogo grande. Com poucos SKUs, o ícone de lupa basta.
- **Navegação visual logo abaixo do header:** bolhas com foto (Loft 111: Bestsellers, Novidades,
  Sale, Vestidos, Saias) seguidas de faixa de benefícios com ícones; chips de categoria com foto
  (Bold: Combos, Wafer, Bold 210); círculos abaixo do hero (Woly); linha de categorias
  (Decathlon). É o que mais encurta o caminho até a vitrine no celular.
- Hero mobile com arte própria (texto grande, recorte vertical): ver [banners.md](banners.md).

## Botões flutuantes

WhatsApp flutuante em Amaro, Loft 111, Pretorian, Shark e Woly (no menu). Na PDP ele disputa
espaço com o seletor e com a barra de compra (Loft 111: ao lado do seletor de tamanho).

- Canto oposto ao chat, sempre **acima** da barra fixa de compra, nunca sobre o preço ou o botão.
- Some dentro da sacola e do checkout.
- Um flutuante só. WhatsApp + chat + "voltar ao topo" empilhados viram ruído.

## Contadores na primeira dobra

"331 clientes estão de olho neste produto agora" (Embelleze), "165 clientes estão visualizando
este produto" (Maxme), "5,3 mil pessoas viram isso nas últimas 24 horas" (Gymshark). No celular
eles ocupam espaço nobre. Mesmo com dado real, eles ficam abaixo de preço e botão; sem dado real,
não existem (ver [conversao.md](conversao.md), "Prova e urgência").

## Checklist mobile no Figma

- [ ] PDP 390 com nome, preço e parcelas acima de 844px, ou barra fixa com preço
- [ ] Estado da PDP rolada, com a barra de compra visível
- [ ] Menu inferior (se houver) com rótulos e área segura
- [ ] Filtros do catálogo em painel, com contagem de resultado no botão "Ver N produtos"
- [ ] Sacola aberta no celular (vazia, com itens, frete)
- [ ] Nenhum pop-up desenhado sobre a primeira dobra do primeiro acesso
- [ ] Flutuantes posicionados sem cobrir preço nem botão
