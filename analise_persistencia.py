
from datetime import datetime, timedelta

from analise_historico import consultar_medicoes


TOTAL_MEDICOES = 6
LIMITE_CPU = 90
LIMITE_RAM = 90
MINIMO_CONSECUTIVAS = 4
INTERVALO_MAXIMO = 10


def maior_sequencia(valores, limite):
    atual = 0
    maior = 0

    for valor in valores:
        if valor >= limite:
            atual += 1
            maior = max(maior, atual)
        else:
            atual = 0

    return maior


def analisar_persistencia(registros, titulo):
    print("\n========== PC DOCTOR AI ==========")
    print(titulo)

    if len(registros) < TOTAL_MEDICOES:
        print("Historico insuficiente para esta analise.")
        return

    horarios = [
        datetime.fromisoformat(registro[0])
        for registro in registros
    ]

    intervalos = [
        (horarios[i] - horarios[i - 1]).total_seconds()
        for i in range(1, len(horarios))
    ]

    # Verifica se as medicoes estao proximas
    if any(
        intervalo < 1 or intervalo > INTERVALO_MAXIMO
        for intervalo in intervalos
    ):
        print("As medicoes possuem intervalos irregulares.")
        print("Nao podemos avaliar uma sequencia continua.")
        print("Execute registro_automatico.py novamente.")
        return

    cpu = [registro[1] for registro in registros]
    ram = [registro[2] for registro in registros]

    sequencia_cpu = maior_sequencia(cpu, LIMITE_CPU)
    sequencia_ram = maior_sequencia(ram, LIMITE_RAM)

    print("\n--- RESULTADOS ---")
    print(f"Medicoes analisadas: {len(registros)}")
    print(f"CPU media: {sum(cpu) / len(cpu):.1f}%")
    print(f"RAM media: {sum(ram) / len(ram):.1f}%")

    print(
        f"Maior sequencia de CPU elevada: "
        f"{sequencia_cpu} medicoes"
    )
    print(
        f"Maior sequencia de RAM elevada: "
        f"{sequencia_ram} medicoes"
    )

    alertas = []

    if sequencia_cpu >= MINIMO_CONSECUTIVAS:
        alertas.append(
            "O processador apresentou uso elevado "
            "em varias medicoes seguidas."
        )

    if sequencia_ram >= MINIMO_CONSECUTIVAS:
        alertas.append(
            "A memoria RAM apresentou uso elevado "
            "em varias medicoes seguidas."
        )

    # O espaco de armazenamento e avaliado
    # pela medicao mais recente
    ultimo = registros[-1]

    if ultimo[3] >= 90 or ultimo[4] < 10:
        alertas.append(
            "O espaco disponivel no armazenamento "
            "merece atencao."
        )

    print("\n--- DIAGNOSTICO ---")

    if alertas:
        for alerta in alertas:
            print("ATENCAO:", alerta)
    else:
        print(
            "Nenhum uso elevado repetido foi "
            "identificado nesta janela."
        )

    print(
        "\nEstes avisos nao confirmam "
        "defeitos no computador."
    )


def testar_simulacao():
    inicio = datetime.now().replace(microsecond=0)

    cpu = [95, 96, 94, 92, 15, 10]
    ram = [40, 40, 93, 94, 96, 95]
    disco = [73, 73, 95, 95, 95, 95]
    livre = [58, 58, 8, 8, 8, 8]

    registros = []

    for i in range(TOTAL_MEDICOES):
        horario = inicio + timedelta(seconds=i * 5)

        registros.append((
            horario.isoformat(timespec="seconds"),
            cpu[i],
            ram[i],
            disco[i],
            livre[i]
        ))

    analisar_persistencia(
        registros,
        "TESTE COM DADOS SIMULADOS"
    )


if __name__ == "__main__":
    registros = consultar_medicoes()

    analisar_persistencia(
        registros,
        "ANALISE DO HISTORICO REAL"
    )

    testar_simulacao()
