
from diagnostico_ia import coletar_dados


def analisar_indicadores(dados):
    alertas = []

    cpu = dados["cpu_percentual"]
    ram = dados["ram_percentual"]
    disco = dados["disco_ocupado_percentual"]
    livre = dados["disco_livre_gb"]

    # Verifica a utilizacao do processador
    if cpu >= 90:
        alertas.append(
            "O processador esta muito ocupado nesta medicao. "
            "Observe se isso continua acontecendo por varios minutos."
        )

    # Verifica a utilizacao da memoria RAM
    if ram >= 90:
        alertas.append(
            "A memoria RAM esta quase totalmente ocupada. "
            "Isso pode prejudicar o desempenho se continuar."
        )

    # Verifica o espaco de armazenamento
    if disco >= 90 or livre < 10:
        alertas.append(
            "O espaco para guardar arquivos esta ficando limitado. "
            "Verifique quanto armazenamento ainda esta disponivel."
        )

    return alertas


def mostrar_resultado(dados, titulo):
    print("\n========== PC DOCTOR AI ==========")
    print(titulo)

    print(f"\nProcessador: {dados['cpu_percentual']}%")
    print(f"Memoria RAM: {dados['ram_percentual']}%")
    print(f"Armazenamento ocupado: "
          f"{dados['disco_ocupado_percentual']}%")
    print(f"Espaco livre: {dados['disco_livre_gb']} GB")

    alertas = analisar_indicadores(dados)

    print("\n--- RESULTADO DA ANALISE ---")

    if not alertas:
        print(
            "Nenhum indicador ultrapassou os limites de "
            "atencao nesta medicao."
        )
        print(
            "Isso nao garante que o computador "
            "esteja livre de problemas."
        )
    else:
        for numero, alerta in enumerate(alertas, start=1):
            print(f"\nAtencao {numero}: {alerta}")


def main():
    print("Coletando informacoes reais do Windows...")

    dados_reais = coletar_dados()

    # Primeiro teste: computador real
    mostrar_resultado(
        dados_reais,
        "ANALISE DO COMPUTADOR REAL"
    )

    # Segundo teste: valores simulados
    # Nao altera o funcionamento do Windows
    dados_simulados = dados_reais.copy()

    dados_simulados.update({
        "cpu_percentual": 95.0,
        "ram_percentual": 93.0,
        "disco_ocupado_percentual": 96.0,
        "disco_livre_gb": 8.0
    })

    mostrar_resultado(
        dados_simulados,
        "TESTE COM VALORES SIMULADOS"
    )


if __name__ == "__main__":
    main()
