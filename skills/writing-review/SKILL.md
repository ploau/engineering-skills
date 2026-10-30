---
name: writing-review
description: Reviews or rewrites technical prose in the language of that prose. Portuguese text keeps one period per idea, with mechanism, limit, and exception in the same sentence. English text may close each function with a period. Also cuts empty openings, parenthetical restatement, slash or dash restatement, and contrast that denies a thing before affirming it. Use when the user says /writing-review or asks to fix choppy technical writing.
disable-model-invocation: true
---

## User language

Chat replies, and the prose of any report this skill writes, use the user's language. Infer that language from the conversation, or from the text after the command. Keep each paragraph of that output in one language. When this skill names a heading that another skill has to find, keep that heading text as specified and write the body in the user's language. The instructions outside the labeled language sections stay in English. Review the source text in the language of that text.

# Writing review

Read the text and name its language before marking passages. Apply the labeled section that matches the text. Preserve technical terms, numbers, and interface names. Do not invent a fact, a number, a name, or a cause to make the text feel concrete. If the original is vague and no detail exists, shorten it. Vary sentence length by content.

When the user asked for a review, return the passage, the problem, and a rewrite. When the user asked for a rewrite, return the text and a short note of what changed. The note follows the user-language directive. The rewrite stays in the language of the source text.

## Shared cuts

The first sentence delivers the fact. It does not announce that the fact comes later, and it does not repeat the title.

If the sentence already said the thing, do not say it again in parentheses, after a slash, or after a dash. Parentheses hold only a datum the sentence cannot carry, such as an acronym on first mention or a value. A slash stays in a path, a command, or a real product alternative. An em dash leaves the text. Use a comma, a colon, or a hyphen.

State the fact. Do not set it up by denying the opposite, by a frame of importance, or by a forced group of three when there are two or four.

Cut words that only announce. A precise technical term stays. Do not stack those terms. Do not swap the object's name for a synonym in every sentence.

Do not close with vague praise or a tagline. The last sentence carries the condition, the limit, or the next fact.

Bold marks an interface label or a term you are defining. It does not mark emphasis in the middle of a sentence. No decorative emoji. No chat frame around the deliverable when the deliverable is the text.

Active voice and present tense, except for what has not happened yet. Cut intensifiers and say the fact.

A step the reader runs in order becomes a numbered list, imperative, one action per line. Three or more items the reader compares become a list introduced by a complete sentence and a colon. Inside a sentence, a series uses commas and closes with a conjunction.

Name an interface, a path, or a command inside the sentence that already explains the mechanism.

## Portuguese

O ponto final fecha a ideia. Mecanismo, limite e exceção ficam no mesmo período, ligados por vírgula, ponto e vírgula ou conectivo, como que, pois, e, mas ou quando.

Não fragmente. Oração subordinada ou locução não recebe ponto próprio, porque ponto nesse lugar finge que o pedaço é uma frase completa.

Frase curta pede ordem direta e pouca intercalação. Não pede um ponto para cada oração.

O período seguinte só começa quando a ideia muda. Retome o que já foi dito com pronome ou com o nome do objeto, e ligue com conectivo se a relação for causa, contraste ou tempo.

Três ou mais itens que a pessoa compara viram lista, introduzida por uma frase completa com dois-pontos. Dentro do período, a série usa vírgula e fecha com conjunção.

O ponto e vírgula não substitui o ponto final por hábito. Use só quando as partes coordenadas já trazem vírgula interna. No restante, ligue com vírgula e conectivo.

Passo que a pessoa executa em ordem vira lista numerada, no imperativo, uma ação por linha.

Nome de interface, caminho e comando entram na oração que já explica o mecanismo.

Voz ativa e presente, salvo o que ainda vai acontecer. Corte fácil, simples, rápido, muito, apenas e realmente, e diga o fato.

A primeira frase entrega o fato. Corte a abertura que anuncia o fato, a reexplicação entre parênteses, depois de uma barra ou depois de um travessão, e o contraste que nega para depois afirmar. Parêntese só guarda um dado que a frase não comporta. Barra só fica em caminho, comando ou alternativa real. Travessão sai. No lugar, use vírgula, dois-pontos ou hífen.

Uma fila de pontos que ainda fala da mesma ideia vira um período só, com vírgula entre as ações e conjunção na ligação. O ponto fica no fim da ideia.

## English

The first sentence states the result. The next sentence starts when the function changes, whether that function is the mechanism, the limit, or the exception. Actions that belong to the same gesture may share one sentence, split by commas. Three or more parallel items become a list. Do not pile clauses into one period just to imitate the Portuguese section.

Apply the shared cuts in English wording. Do not apply the Portuguese one-period rule to English text.
