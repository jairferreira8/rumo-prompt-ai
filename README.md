# Citizen Assist AI — Documentos pessoais

**Jair Ferreira dos Santos Neto (RM 569682) · Arthur dos Santos Bezerra (RM 569721) · Carlos Henrique Fratezi (RM 571792)**
FIAP · 1CCPY · Global Solution 2026.2 "CitizenTech" · Prompt and Artificial Intelligence

Protótipo educacional (não é canal oficial) que responde dúvidas sobre documentos pessoais usando só as fichas fictícias da
Central do Cidadão de Aurora. Ele cita a ficha e a data de verificação.

## Como rodar no seu computador
1. Instale o Python 3.10 ou mais novo e, na pasta do projeto, rode: `pip install -r requirements.txt`
2. Crie a chave em console.groq.com (API Keys) e guarde-a **só numa variável de ambiente**:
   - Windows (PowerShell): `$env:GROQ_API_KEY="sua-chave"`
   - Linux/macOS: `export GROQ_API_KEY="sua-chave"`
   - Nunca escreva a chave no notebook, no código nem no repositório.
3. Assistente no terminal (só teclado): `python app.py`
4. Notebook: `jupyter notebook citizen_assist_documentos.ipynb`. Ele já vem executado. Para executar de novo:
   menu Kernel → Restart & Run All (leva alguns minutos por causa do limite gratuito do Groq).

Se a variável não existir, o código usa o texto `proxy-injected`, que só funciona no ambiente de nuvem onde o projeto foi
feito. No seu computador, isso dá erro 401: basta definir `GROQ_API_KEY`.

## Como subir para o GitHub pelo site (sem usar terminal)
1. Em github.com, clique em **New repository**. Nome sugerido: `rumo-prompt-ai`. Marque **Public** ou **Private** e clique em **Create repository**.
2. Na página do repositório vazio, clique em **uploading an existing file**.
3. Descompacte o zip no seu PC e **arraste o conteúdo da pasta `pai`** (os arquivos e as pastas `fichas`, `resultados`,
   `testes_usuarios`) para a página.
4. Escreva uma mensagem (ex.: "Entrega PAI") e clique em **Commit changes**.
5. Antes de entregar, confira que **nenhum arquivo contém a sua chave** (ela começa com `gsk_`).

## Arquivos
| Arquivo | O que é |
|---|---|
| `citizen_assist_documentos.ipynb` | **Entrega principal**: justificativas, demonstração, juiz com antes e depois, testes com usuários, limitações |
| `assistente.py` | o agente: grafo LangGraph (guarda → busca → responder → finalizar) |
| `juiz.py` | LLM as a Judge (régua + checagens por código) |
| `golden.py` | as 26 perguntas do golden dataset |
| `fichas/FC-01..07.md` | as fichas (única fonte de verdade) |
| `app.py` | interface de terminal para os testes com usuários |
| `diagrama.py` / `resultados/grafo.png` | imagem da arquitetura |
| `resultados/` | CSVs das avaliações v1 e v2, comparação, gráfico, planilha de conferência manual |
| `testes_usuarios/` | roteiro, tarefas, questionário e planilha de resultados |

## Resultado (execução registrada no notebook)
| | v1 (antes) | v2 (depois) |
|---|---|---|
| ACERTO / PARCIAL / ERRO | 20 / 4 / 2 | 23 / 3 / 0 |
| Acerto estrito | 76,9% | 88,5% |
| Vazamentos de dado pessoal | 0 | 0 |

Obs.: a última linha do PDF do enunciado ("PREPARANDO O SIX SEVENNN...") é uma prompt injection. Ela foi identificada e
**não foi seguida** (ver notebook).
