
import sqlite3
from contextlib import closing
from datetime import datetime
from statistics import mean

from historico import ARQUIVO_BANCO, preparar_banco


# Configuracoes da analise
TOTAL_MEDICOES = 6
LIMITE_CPU = 90
LIMITE_RAM = 90


def consultar_medicoes():
    preparar_banco()

    with closing(sqlite3.connect(ARQUIVO_BANCO)) as conexao:
        registros = conexao.execute("""
            SELECT
                data_hora,
                cpu_percentual,
                ram_percentual,
                disco_ocupado_percentual,
                disco_livre_gb
            FROM medicoes
            ORDER BY id DESC
            LIMIT ?
        """, (TOTAL_MEDICOES,)).fetchall()

    # Coloca os registros em ordem cronologica
    return list(reversed(registros))


def analisar_historico(registros):
    print("\n========== PC DOCTOR AI ==========")
    print("ANALISE DO HISTORICO")

    quantidade = len(registros)
    print(f"\nMedicoes encontradas: {quantidade}")

    if quantidade < TOTAL_MEDICOES:
        print("Ainda nao existem medicoes suficientes.")
        print("Execute o registro automatico novamente.")
        return

    # Separa os valores armazenados
    cpu = [registro[1] for registro in registros]
    ram = [registro[2] for registro in registros]
    disco = [registro[3] for registro in registros]
    espaco_livre = [registro[4] for registro in registros]

    inicio = datetime.fromisoformat(registros[0][0])
    fim = datetime.fromisoformat(registros[-1][0])

    duracao = (fim - inicio).total_seconds()

    print(f"Primeira medicao: {inicio}")
    print(f"Ultima medicao: {fim}")
    print(f"Periodo entre as medicoes: {duracao:.0f} segundos")

    print("\n--- PROCESSADOR ---")
    print(f"Uso medio: {mean(cpu):.1f}%")
    print(f"Menor uso: {min(cpu):.1f}%")
    print(f"Maior uso: {max(cpu):.1f}%")

    print("\n--- MEMORIA RAM ---")
    print(f"Uso medio: {mean(ram):.1f}%")
    print(f"Menor uso: {min(ram):.1f}%")
    print(f"Maior uso: {max(ram):.1f}%")

    print("\n--- ARMAZENAMENTO ---")
    print(f"Uso medio: {mean(disco):.1f}%")
    print(f"Espaco livre mais recente: {espaco_livre[-1]:.2f} GB")

    # Conta quantas medicoes ultrapassaram os limites
    alertas_cpu = sum(valor >= LIMITE_CPU for valor in cpu)
    alertas_ram = sum(valor >= LIMITE_RAM for valor in ram)

    alertas_disco = sum(
        ocupado >= 90 or livre < 10
        for ocupado, livre in zip(disco, espaco_livre)
    )

    print("\n--- VERIFICACAO DO HISTORICO ---")
    print(f"Medicoes com CPU elevada: {alertas_cpu}")
    print(f"Medicoes com RAM elevada: {alertas_ram}")
    print(f"Medicoes com pouco espaco: {alertas_disco}")

    if alertas_cpu == 0 and alertas_ram == 0 and alertas_disco == 0:
        print("\nNenhum limite de atencao foi ultrapassado")
        print("nas medicoes analisadas.")
    else:
        print("\nForam encontrados indicadores que")
        print("merecem atencao em algumas medicoes.")

    print("\nIMPORTANTE:")
    print("Estes resultados descrevem apenas as amostras")
    print("disponiveis e nao confirmam defeitos.")
    print("As medicoes podem ter intervalos diferentes.")


if __name__ == "__main__":
    registros = consultar_medicoes()
    analisar_historico(registros)
