# Roteiro do teste com usuários — Citizen Assist AI · Documentos

Jair Ferreira dos Santos Neto (RM 569682) · Arthur dos Santos Bezerra (RM 569721) · Carlos Henrique Fratezi (RM 571792)
FIAP · 1CCPY · Global Solution 2026.2 · Prompt and Artificial Intelligence

## Regras de privacidade do teste
- Participantes de **fora da equipe**, no mínimo **5**.
- **Não anotar nome, idade exata, contato nem nenhum dado pessoal.** Use apenas um código: P1, P2, P3...
- Avisar antes: "Não digite nenhum dado seu de verdade. Tudo aqui é fictício."
- O app não grava nada: as perguntas e respostas não vão para nenhum arquivo.

## Preparação
1. Abrir o terminal na pasta do projeto e rodar `python app.py`.
2. Ter um cronômetro (celular).
3. Ler para o participante: "Este é um assistente sobre documentos de uma cidade fictícia. Vou pedir 3 tarefas. Use só o teclado. Pode usar o menu ou escrever do seu jeito. Não existe resposta errada da sua parte: quem está sendo testado é o sistema."

## As 3 tarefas (ler uma de cada vez)
Comece a cronometrar quando terminar de ler a tarefa. Pare quando a pessoa disser a resposta em voz alta.

| Tarefa | O que ler ao participante | Resposta certa |
|---|---|---|
| T1 | "Descubra quanto custa a segunda via do RG." | R$ 38,00 (FC-01) |
| T2 | "Descubra se a Central atende aos sábados." | Não; segunda a sexta, 8h às 17h (FC-07) |
| T3 | "Você tem 55 anos. Descubra por quanto tempo vale a CNH renovada." | 5 anos (FC-06) |

Anote: tempo em segundos, se concluiu (sim ou não) e se a resposta dita estava certa.

## Questionário de facilidade (de 1 a 5)
1 = discordo totalmente · 5 = concordo totalmente

1. Foi fácil encontrar a informação que eu precisava.
2. As respostas foram claras e curtas.
3. Eu soube o que fazer em cada passo (menu ou pergunta livre).
4. Confiei que a informação veio de uma fonte indicada (a ficha citada).
5. Eu usaria este assistente de novo.

Pergunta aberta (opcional, sem dados pessoais): "O que você mudaria?"

## Onde anotar
Preencha `resultados_testes.csv`, uma linha por participante. Depois rode a seção 9 do notebook, que calcula as médias.
