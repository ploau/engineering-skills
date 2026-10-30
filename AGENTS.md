# Guia do agente

Guia curto deste repositório. Não é uma segunda especificação. No máximo 15 conceitos. Ao mudar uma regra, edite ou una uma linha. Não copie o chat para cá.

1. Skills ficam em `skills/<nome>/SKILL.md`. O corpo das instruções permanece em inglês. Respostas e relatórios seguem a língua do usuário.
2. Todo commit deste repositório segue Conventional Commits: `type(scope): resumo no imperativo`. O scope é opcional e sai da mudança. Título só, em inglês técnico, até 72 caracteres. Um domínio por commit.
3. Types: `feat`, `fix`, `refactor`, `perf`, `chore`, `docs`, `test`.
4. Não faça commit nem push sem pedido explícito. Não altere git config. Não use `--force`. `--force-with-lease` só quando o usuário autorizar a reescrita daquele branch.
5. Autor e committer: Paulo Serpa `<pauloserpa.r@gmail.com>`. Passe os dois com `git -c` no comando. Não grave isso na config.
6. Não cite projeto, repositório ou marca externa no texto dos skills.
7. Não reintroduza harnesses removidos, OpenCode, hooks ou plugin-bootstrap.
8. O gerador copia só o que existe em `templates/harness/` e `templates/plugin/`. Não invente outro layout de manifesto.
9. Evidência: `test-it` em `.tests/`, `record-it` em `.recordings/`, `stress-it` em `.stress/`. O arquivo de tarefas do `auto-task` continua em `.tasks/`.
10. Ao adicionar, remover ou renomear um skill, atualize na mesma mudança a tabela de skills e a lista de invocação no `README.md`.
11. Versão e changelog saem do Changesets, em `.changeset/`. Não crie arquivo de version bump.
