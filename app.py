"""
Citizen Assist AI — Documentos · versão de terminal (para os testes com usuários).
Uso:  python app.py
Funciona só com o teclado. Não grava nada: nenhuma pergunta ou resposta vai para arquivo ou log.
"""
import assistente

BOAS_VINDAS = """
==============================================
 Citizen Assist AI · Documentos (protótipo)
 Central do Cidadão de Aurora · material fictício
==============================================
Não digite CPF, RG, endereço ou telefone.
Comandos: "menu" mostra os assuntos · "sair" encerra.
"""


def main():
    print(BOAS_VINDAS)
    print(assistente.texto_menu())
    while True:
        try:
            texto = input("\nSua pergunta > ")
        except (EOFError, KeyboardInterrupt):
            break
        comando = texto.strip().lower()
        if comando in ("sair", "fim", "tchau"):
            break
        if comando == "menu":
            print(assistente.texto_menu())
            continue
        print("\n" + assistente.perguntar(texto)["resposta"])
    print("\nAté logo! Lembre-se de confirmar tudo no órgão oficial.")


if __name__ == "__main__":
    main()
