
import time
import requests

from diagnostico_ia import coletar_dados
from analise_regras import analisar_indicadores


URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2:3b"


def mostrar_analise(dados, alertas):
    print("\n========== PC DOCTOR AI ==========")
    print("ANALISE DO COMPUTADOR")

    print(f"\nProcessador: {dados['cpu_percentual']:.1f}%")
    print(f"Memoria RAM: {dados['ram_percentual']:.1f}%")
    print(f"Armazenamento ocupado: {dados['disco_ocupado_percentual']:.1f}%")
    print(f"Espaco livre: {dados['disco_livre_gb']:.2f} GB")

    print("\n--- RESULTADO DAS VERIFICACOES ---")

    if not alertas:
        print(
            "Nenhum indicador ultrapassou os limites nesta medicao."
        )
    else:
        for numero, alerta in enumerate(alertas, start=1):
            print(f"Aviso {numero}: {alerta}")


def explicar_com_ia(dados, alertas):

    # Quando nao existem alertas, o Python explica
    if not alertas:
        print("\n--- DIAGNOSTICO DO PC DOCTOR AI ---")

        print(
            "Nenhum indicador ultrapassou os limites de atencao."
        )
        print(
            "Nenhuma correcao e indicada por esta medicao isolada."
        )
        print(
            "Isso nao garante que o computador esteja livre de problemas."
        )
        return

    # A IA recebe apenas os alertas identificados

    instrucoes = (
        "Voce e um assistente de informatica para iniciantes. "
        "Explique os avisos recebidos em portugues brasileiro. "
        "Escreva um unico paragrafo com no maximo 3 frases. "
        "Explique o significado do aviso e sugira um cuidado simples. "
        "Use apenas os problemas identificados pelo programa. "
        "Nao acrescente outros problemas ou informacoes. "
        "Nao use listas, titulos ou numeracao."
    )

    pergunta = (
        "Explique estes avisos do computador: "
        + " ".join(alertas)
    )

    requisicao = {
        "model": MODELO,
        "system": instrucoes,
        "prompt": pergunta,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 250
        }
    }

    print("\nConsultando a inteligencia artificial...")
    inicio = time.perf_counter()

    try:
        resposta = requests.post(
            URL,
            json=requisicao,
            timeout=(5, 180)
        )

        resposta.raise_for_status()

        explicacao = resposta.json().get(
            "response", ""
        ).strip()

        if not explicacao:
            print("A IA nao retornou uma explicacao.")
            return

        print("\n--- EXPLICACAO DA IA ---")
        print(explicacao.replace("**", ""))

        tempo = time.perf_counter() - inicio
        print(f"\nTempo da IA: {tempo:.2f} segundos")

    except (
        requests.exceptions.RequestException,
        ValueError
    ) as erro:
        print("Nao foi possivel consultar a IA.")
        print(
            "Os avisos calculados pelo Python continuam disponiveis."
        )
        print("Detalhes:", erro)


def main():
    print("Coletando dados do computador...")

    dados = coletar_dados()
    alertas = analisar_indicadores(dados)

    mostrar_analise(dados, alertas)
    explicar_com_ia(dados, alertas)


if __name__ == "__main__":
    main()
