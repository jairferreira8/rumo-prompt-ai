"""Desenha a arquitetura do grafo (LangGraph) com matplotlib, destacando IA x lógica."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def desenhar(caminho="resultados/grafo.png"):
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    ax.set_xlim(0, 11); ax.set_ylim(0, 6.2); ax.axis("off")
    LOG, IA, FIM = "#dbeafe", "#fde68a", "#e5e7eb"
    nos = {
        "inicio":   (0.3, 4.6, 1.5, 0.8, "Pergunta\ndo usuário", FIM),
        "guarda":   (2.4, 4.4, 2.3, 1.2, "guarda (lógica)\nvalida entrada · mascara\nCPF/tel/e-mail · detecta\ninjection", LOG),
        "busca":    (5.4, 4.4, 2.1, 1.2, "busca (lógica)\npalavras-chave →\nfichas + FC-07", LOG),
        "responder":(8.2, 4.4, 2.5, 1.2, "responder (IA)\nGroq gpt-oss-20b\nsó com as fichas,\ncita FC e data", IA),
        "fixa":     (2.4, 1.9, 2.3, 1.2, "resposta_fixa (lógica)\nentrada inválida →\nmenu + exemplo", LOG),
        "final":    (5.4, 1.9, 2.1, 1.2, "finalizar (lógica)\naviso de privacidade\n+ limpeza da saída\n+ aviso fixo", LOG),
        "fim":      (8.5, 2.1, 1.9, 0.8, "Resposta", FIM),
    }
    for x, y, w, h, txt, cor in nos.values():
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", fc=cor, ec="#334155", lw=1.2))
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=8.5)

    def seta(a, b, rot="", tracejada=False, dx=0, dy=0):
        ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="-|>", lw=1.3, color="#334155",
                    linestyle="--" if tracejada else "-"))
        if rot:
            ax.text((a[0] + b[0]) / 2 + dx, (a[1] + b[1]) / 2 + dy, rot, fontsize=8, color="#475569", ha="center")

    seta((1.8, 5.0), (2.4, 5.0))
    seta((4.7, 5.0), (5.4, 5.0), "válida", True, 0, 0.12)
    seta((3.55, 4.4), (3.55, 3.1), "inválida", True, 0.45, 0)
    seta((7.5, 5.0), (8.2, 5.0))
    seta((9.45, 4.4), (7.5, 3.0))
    seta((4.7, 2.5), (5.4, 2.5))
    seta((7.5, 2.5), (8.5, 2.5))
    ax.add_patch(FancyBboxPatch((0.3, 0.3), 0.35, 0.3, boxstyle="round,pad=0.02", fc=LOG, ec="#334155"))
    ax.text(0.8, 0.45, "lógica e algoritmos (sem IA)", va="center", fontsize=8.5)
    ax.add_patch(FancyBboxPatch((3.6, 0.3), 0.35, 0.3, boxstyle="round,pad=0.02", fc=IA, ec="#334155"))
    ax.text(4.1, 0.45, "IA generativa (LLM)", va="center", fontsize=8.5)
    ax.text(5.5, 6.0, "Citizen Assist AI — Documentos · grafo LangGraph (1 agente)",
            ha="center", fontsize=11, weight="bold")
    fig.savefig(caminho, bbox_inches="tight"); plt.close(fig)
    return caminho


if __name__ == "__main__":
    print(desenhar())
