# Ateliê de Vitrine — guia de design de e-commerce para qualquer IA

O conteúdo é Markdown puro e não depende de runtime. `SKILL.md` é o ponto de entrada (o
frontmatter só serve para quem carrega skills; as outras IAs ignoram). As regras moram em um lugar
só: não copie o texto para dentro de outros arquivos, aponte para esta pasta.

Processo e padrões para desenhar e implementar loja virtual com qualidade de estúdio em qualquer
nicho: fatos reais antes de pixels, referência só como estrutura, design system com modo
claro/escuro, a jornada inteira (home, catálogo, produto, sacola, busca, rodapé, políticas,
cookies LGPD), implementação em Shopify ou site estático, e verificação com evidência.

## Instalar

```bash
git clone https://github.com/Greed9797/atelie-de-vitrine ~/.claude/skills/atelie-de-vitrine   # Claude Code
git clone https://github.com/Greed9797/atelie-de-vitrine ~/.codex/skills/atelie-de-vitrine    # Codex CLI
```

```
SKILL.md                      princípios + fluxo em 8 fases (ler primeiro)
references/briefing-e-fatos.md
references/nichos.md
references/design-system.md
references/paginas.md
references/figma.md
references/shopify.md
references/qa.md
scripts/qa_loja.py            varredura Playwright (python3 + Chrome)
```

## Adaptadores

| Agente | Como ligar |
|---|---|
| Claude Code | pasta em `~/.claude/skills/atelie-de-vitrine/`; aciona sozinho pela `description` |
| Codex CLI | copiar a pasta para `~/.codex/skills/` (cópia, não symlink de diretório: alguns loaders não seguem) **ou** no `AGENTS.md` do projeto: `Para trabalho de loja/e-commerce, siga <caminho>/SKILL.md e leia as references que ele indicar.` |
| Cursor / Windsurf / Zed | regra do projeto (`.cursor/rules/ecommerce.mdc` etc.) com a mesma linha de ponteiro acima |
| ChatGPT / Claude.ai / Gemini (chat) | anexar `SKILL.md` + as references da fase em curso, ou colar `SKILL.md` como instrução do projeto |
| Qualquer outro | instrução de sistema: "Siga SKILL.md; leia references/<x>.md quando o fluxo mandar." |

Em chat sem acesso a arquivos, o mínimo que mantém a qualidade é `SKILL.md` + `paginas.md` +
`design-system.md`. As partes de Figma, Shopify e QA só fazem sentido para agente com ferramentas.
