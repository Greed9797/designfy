# Lojas de referência — o que emprestar de cada uma

Análise de 2026-09-27: home, catálogo, PDP, sacola e política de cada loja, em 1440 e 390, com
extração de fonte, raio, cor, ordem das seções, textos de condição e apps. **Empreste estrutura,
nunca identidade** (princípio 3 do `SKILL.md`): o que está aqui é ordem, comportamento e mecânica,
não logo, foto ou fonte proprietária. Lojas mudam; confira a página antes de citar um detalhe
ao cliente.

Duas não entraram: Nestlé (as três lojas oficiais — institucional, Dolce Gusto, Health Science —
bloqueiam navegador automatizado) e Budweiser (o endereço de loja é um widget de "onde comprar").

## Cobertura da sacola (rodada final, 2026-09-27)

O extrator adiciona 1 item e lê a sacola. Resultado por loja, para não tomar ausência de achado
como ausência de mecânica:

| Status | Lojas |
|---|---|
| Drawer lido | Boca Rosa, Bold, Decathlon, Embelleze, Kylie, Loft 111, Modab, Real Madrid, Shark, Stanley |
| Adicionou, sem drawer (confirmação em popover/toast) | Amaro, Galeroca |
| Não existe sacola ("Onde comprar") | Lavitan |
| Não testada: produto amostrado esgotado | Mondepars, PantryShop, Pretorian |
| Falhou: pop-up de país na frente do botão | Gymshark |
| Falhou: o clique marcou o favorito, nada foi adicionado | Maxme, Woly |

Nas lojas "não testada" e "falhou", o que este arquivo diz da sacola vem dos prints da primeira
rodada ou não é dito.

## O que se repete (e vira padrão da skill)

- **Barra de anúncio** em 17 de 19, com 2–3 fatos rotativos (frete, parcelas, cupom, cashback).
- **Sacola em drawer** com barra de frete grátis ou recomendação, e campo de cupom/CEP, nas 7
  lojas Shopify brasileiras em que a sacola foi lida (Boca Rosa, Bold, Embelleze, Loft 111, Modab,
  Shark, Stanley). Ver [conversao.md](conversao.md) e a tabela de cobertura acima.
- **CEP na PDP**, logo abaixo do botão ("Consulte prazo e valores", "Simule seu frete"): Modab,
  Loft 111, Mondepars, Woly, Embelleze, Pretorian, Shark. A Amaro pede o endereço no header.
  Prazo e frete antes da sacola reduzem abandono.
- **WhatsApp flutuante** no canto inferior direito nas brasileiras. Não pode cobrir a barra de
  compra fixa no mobile.
- **Tema de agência em série.** Bold, Modab, Mondepars, Pretorian, Shark, Loft 111 e Embelleze
  rodam o mesmo "Tema Base" de uma agência (Alfinet): mesma sacola, mesmo ticker, mesmo bloco de
  CEP. É o piso de mercado para Shopify Plus no Brasil; o diferencial vem de tipografia, foto e do
  bloco decisivo do nicho, não da estrutura.
- **Raio**: 0px é o valor mais usado em 17 de 19; pílula (999px) só no botão ou no chip. Raio
  arredondado como regra aparece em Real Madrid (8–16px), Amaro (8px) e Kylie (4px).
- **Tipografia**: uma família de marca + uma de apoio; display condensado em caixa-alta para
  esporte e snacks (Bold, Pretorian, Gymshark, Shark), serifa ou grotesca fina para moda premium
  (Modab, Mondepars, Loft 111).

## Moda

**Modab** (modab.com.br, Shopify) — moda feminina premium, jeans modelador.
Sistema: serifa display fina (títulos) + grotesca condensada caixa-alta (UI); raio 0; preto, branco,
creme. Emprestar: hero em vídeo tela cheia com arte vertical própria no mobile; chips com foto no
topo do catálogo (Pantalona, Wide leg, Flare…) + chips de benefício como filtro rápido ("Não
desbota", "Não amassa", "Cós alto"); PDP com duas fotos lado a lado, cashback em R$ sob o preço,
"Guia de medidas" e "Experimente com IA" lado a lado, abas "Sobre a peça · Modelagem e tecnologias ·
Cuidados"; sacola com barra "Faltam R$ 100 para frete grátis" e carrossel de recomendados.

**Loft 111** (loft111.com.br, Shopify) — multimarca feminina.
Sistema: Inter, raio 0, preto e branco; a cor vem da foto. Emprestar: faixa de 4 benefícios sob o
header (troca grátis, parcele, frete acima de R$ 700, atendimento); catálogo em grid de 4 sem
margem, foto de corpo inteiro; bloco "Compre junto" com duas peças, checkbox, total e "Adicionar
tudo"; sacola com recomendados que têm seletor de tamanho inline. Item de menu com a embaixadora
(nome de pessoa como coleção).

**Amaro** (amaro.com, Nuvemshop) — moda feminina, grande catálogo.
Sistema: Nunito, raio 8px, preto, acento vermelho só no "Outlet". Emprestar: faixa de benefícios com
números logo abaixo do hero; tamanhos indisponíveis riscados, não escondidos; "Guia de medidas"
sob os tamanhos; botão verde que confirma "Você já adicionou este produto · Ver carrinho" sem abrir
drawer; campanha "App week" (oferta exclusiva do app); FAQ como hub de políticas com âncoras
("#devolucoes").

**Gymshark** (gymshark.com, headless sobre Shopify) — fitness.
Sistema: display condensado próprio + grotesca de texto, raio 0, preto/branco, campanha colorida.
Emprestar: hero de oferta com duas saídas ("Feminino / Masculino"); catálogo que abre com filtro de
tamanho em chips e contagem ("1127 produtos"); PDP com grid de 2 fotos, variações de cor como fotos
do produto, variante de comprimento, selo de economia em R$ ("Save $2.60"), caixa da campanha ativa
perto do preço. Ressalva: o contador "5,3 mil viram nas últimas 24h" só vale com dado real.

**Mondepars** (mondepars.com, Shopify) — moda e perfumaria autoral, luxo.
Sistema: condensada estreita no logo, grotesca 13px caixa-alta com tracking na UI; raio 0; sem cor.
Emprestar: home curtíssima (vídeo, novidades, marca) — loja de luxo não precisa de 12 seções;
catálogo com seletor de densidade (1–4 colunas) e foto grande com fundo de cor por produto; PDP com
"Avise-me quando chegar" no lugar do botão, abas "Composição · Medidas · Política de devolução",
compartilhar no WhatsApp. Sem barra de anúncio: silêncio é posicionamento.

## Beleza e cabelo

**Kylie Cosmetics** (kyliecosmetics.com, Shopify) — maquiagem e fragrância.
Sistema: grotesca bold caixa-alta nos títulos + fonte de texto em minúsculas; raio 4px; rosa pálido
+ vinho. Emprestar: nav em minúsculas com "best sellers" e "rewards" como itens; catálogo com
subcategorias em miniatura e tiles editoriais dentro do grid; PDP com selo de prêmio na foto, ícones
de atributo (todos os tipos de pele, clean, vegan), "real results" em números, "build a routine",
UGC "on social", avaliações longas; sacola-modelo: barra de frete, brinde por faixa com escolha,
brinde automático declarado, pontos do pedido, "before you go…".

**Boca Rosa** (bocarosa.com.br, Shopify) — maquiagem.
Sistema: Roobert, raio 0, magenta sobre off-white. Emprestar: hero de brinde com o limite em valor;
faixa de 3 benefícios; PDP com seletor de tom em duas camadas (faixa Claro/Médio/Escuro + swatches
circulares de 50 tons), "Provador virtual", "Quer ajuda para encontrar seu tom?", preço riscado com
% real; modal "Escolha qual você quer ganhar de brinde!" após adicionar.

**Embelleze / Novex** (embelleze.com, Shopify) — cabelo, várias marcas.
Sistema: Archivo caixa-alta nos títulos, pílula nos botões, roxo de ação + rosa na compra.
Emprestar: **abas de marca no topo do header** (Embelleze · Novex · Maxton · e-sential) para loja
multimarca; catálogo com filtro por necessidade do cabelo, card com selo "NO PIX" e botão
"Adicionar" no próprio card; PDP com "Leve junto com desconto"; seção B2B "Tenha sua loja" para
revenda.

## Suplementos, alimentos e bebidas

**Bold Snacks** (boldsnacks.com.br, Shopify) — barras de proteína.
Sistema: display extra-bold condensado caixa-alta, pílula no CTA, teal + laranja das embalagens.
Emprestar: círculos/tiles de linha com packshot logo abaixo do hero; banner de oferta progressiva
("+1 item 10% · +2 itens 15%"); PDP com tiles de número (21g proteína · 0 açúcar · 12 unidades),
"Outros tamanhos" e "Outros sabores" como amostras que levam ao produto irmão, tabela nutricional em
acordeão, FAQ longa ("Saiba mais"); sacola com barra "Você desbloqueou frete grátis" e faixa "Leve
junto!"; conteúdo (guia de proteína) na home; programa de assinatura com regulamento próprio.

**Maxme Bio** (maxme.bio, Shopify) — suplementos.
Sistema: mono display (Antikor Mono) + grotesca; raio 0; cinza-grafite com cores vivas da embalagem.
Emprestar: "Comprar por objetivo" no menu; seletor de kits na PDP (1 / 3 / 4 / 5 unidades, % por
kit, preço por unidade, "Mais vendido"); "Combina com este produto" e "Leve no protocolo completo";
seções de ciência (por que, diferenciais, tabela) antes das avaliações e da FAQ; escada de benefício
na barra (frete a partir de R$ 249, brinde a partir de R$ 450).

**Lavitan / Cimed** (lavitan.com.br, Shopify, sem checkout) — vitaminas.
Emprestar: marca que vende no varejo: CTA "Onde comprar" abre painel com farmácias; "Faça o quiz"
fixo no header; home por objetivo com ícones (Imunidade, Sono, Performance…); PDP de conteúdo
(Características, Modo de uso, Precauções, Alegações) em acordeão.

**PantryShop / PepsiCo** (pantryshop.com, própria) — snacks e bebidas nos EUA.
Emprestar: catálogo só de kits; seletor "Compra única / Assinar" acima do botão; "Deliver to"
(CEP) no header porque o frete restringe o que aparece; "Out of stock" que não esconde o produto.

## Esporte, casa e licenciados

**Decathlon** (decathlon.com.br, VTEX) — esporte, catálogo enorme.
Sistema: Inter + fonte de marca, pílula nos botões, azul de marca, barra amarela. Emprestar:
"Entrega ou retirada? Adicione seu CEP" no header e "Retire na loja em até 2 horas"; círculos de
esporte; catálogo com banner de coleção + cards de esporte + chips (Mulher, Homem, Desconto pix);
PDP com "Vendido e entregue por", ícones de benefício técnico (leveza, secagem rápida), medidas do
modelo sobre a foto, "Saiba como medir"; cashback que o pedido gera, mostrado no mini-carrinho ("Você já tem R$ 3,99 de cashback no
carrinho!") e de novo no checkout.

**Pretorian** (pretorian.com, Shopify) — artes marciais.
Sistema: display ultra-condensado (Thunder) + Sora; amarelo total no header. Emprestar: menu por
modalidade (Jiu-jitsu, Muay thai, Boxe); card com faixa "Comprar agora" e selo "Frete grátis"
individual; preço com "5% OFF no PIX" em todos os cards; filtros com contagem ("Em estoque (12)",
tamanho em oz); esgotado com "Avise-me" inline por e-mail.

**Shark Beach Tennis** (sharkbeachtennis.com.br, Shopify) — raquetes.
Sistema: Eurostile estendida caixa-alta, verde-limão + roxo. Emprestar: filtro por **nível de
jogo** e composição (o atributo que o cliente usa para escolher raquete); selo de nível no card
("AVANÇADO"); PDP com assinatura do atleta; convite "Seja Shark Member" em pílula flutuante; CTA com
voz de marca ("Eu quero"); sacola com "Compre também" de acessórios (sapatilha, munhequeira) abaixo
do item.

**Stanley** (stanley1913.com.br, Shopify/Dawn) — copos e garrafas.
Sistema: fonte própria, raio 0–4px, verde-oliva no botão. Emprestar: PDP com todas as cores como
grade de miniaturas do produto; faixa de 3 fatos técnicos com ícone (11 horas · 2 dias ·
garantia vitalícia); sacola-modelo brasileira: brinde por faixa, "Aproveite também!" com cor inline,
"Salvar para mais tarde", CEP, parcelas no total; carrossel com pausa acessível; "Acompanhar
pedido" e clube no topo.

**Woly Casa** (wolycasa.com.br, Shopify/Dawn) — utensílios e mesa posta.
Emprestar: navegação por **ambiente** (Mesa posta, Bar & cia, Café & cia) em círculos; catálogo com
filtros por linha, material e submarca; PDP com resumo de condições em caixa (frete, troca, cupom
com botão de copiar), cashback em R$, "Compre junto" com item atual marcado.

**Real Madrid** (shop.realmadrid.com, Shopify/Horizon) — loja oficial de clube.
Sistema: fonte do clube, raio 8–16px, azul-violeta de ação. Emprestar: "Shop by player"; PDP com
"Choose your kit" (Home/Away/Third como fotos), guia de tamanho ao lado do rótulo, preço de membro;
seção de personalização ("Make it yours!"); banner de sócio na barra.

**Galeroca** (galeroca.com.br, VTEX) — brinquedos e personagens.
Sistema: display arredondado (Chomp) + Nunito, pílula, fundo creme e cores primárias. Emprestar:
"compre por personagens" como navegação principal; cards e galeria com moldura arredondada;
selos de segurança e garantia de satisfação na PDP. Ressalva: esconder estrelas quando não há
avaliação.
