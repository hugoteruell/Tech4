# Skills do projeto

## Próprias — versionadas aqui

| Skill | O que faz |
|---|---|
| `consistencia` | Cruza os `.md` e aponta contradição, dado vencido, referência quebrada e pendência órfã |
| `fecha-conversa` | Nota bruta de reunião vira ata com dono e prazo, atualiza o contexto e commita |
| `resumo-semanal` | Status da semana com evidência do git; alimenta o campo `MUDOU NA SEMANA` do V3 |

## De terceiros

### `lead-research-assistant` — versionada aqui

Origem: [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills), diretório `lead-research-assistant/`.
O repositório de origem não declara licença. Mantida aqui com atribuição; os direitos são de quem a escreveu.

### `docx` — **não** versionada

Licença proprietária da Anthropic, que proíbe redistribuição. Por isso está no `.gitignore` e não vem no clone.

Para instalar localmente:

```bash
git clone --depth 1 https://github.com/ComposioHQ/awesome-claude-skills.git /tmp/acs
cp -R /tmp/acs/document-skills/docx .claude/skills/
rm -rf /tmp/acs
```

Antes disso, verifique se você já não a tem nativamente — o Claude Code embarca uma skill `docx` equivalente, e nesse caso a cópia local é redundante.
