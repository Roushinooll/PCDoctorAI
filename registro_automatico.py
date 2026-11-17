
import time

from diagnostico_ia import coletar_dados
from historico import (
    preparar_banco,
    salvar_medicao,
    mostrar_historico
)


# Configuracoes do monitoramento
TOTAL_MEDICOES = 6
INTERVALO_SEGUNDOS = 5


def iniciar_monitoramento():
    preparar_banco()

    print("========== PC DOCTOR AI ==========")
    print("REGISTRO AUTOMATICO DO DESEMPENHO")
    print(f"Total programado: {TOTAL_MEDICOES} medicoes")
    print("Pressione Ctrl + C para interromper.\n")

    realizadas = 0

    try:
        for numero in range(1, TOTAL_MEDICOES + 1):

            # Coleta informacoes reais do Windows
            dados = coletar_dados()

            # Salva a medicao no banco SQLite
            salvar_medicao(dados)
            realizadas += 1

            print(
                f"\n--- MEDICAO {numero}/{TOTAL_MEDICOES} ---"
            )
            print("Data e hora:", dados["data_hora"])

            print(
                f"Processador: "
                f"{dados['cpu_percentual']:.1f}%"
            )

            print(
                f"Memoria RAM: "
                f"{dados['ram_percentual']:.1f}%"
            )

            print(
                f"Armazenamento ocupado: "
                f"{dados['disco_ocupado_percentual']:.1f}%"
            )

            print("Medicao salva no banco de dados.")

            # Aguarda antes de coletar novamente
            if numero < TOTAL_MEDICOES:
                time.sleep(INTERVALO_SEGUNDOS - 1)

    except KeyboardInterrupt:
        print("\nMonitoramento interrompido pelo usuario.")

    print("\n===== REGISTRO FINALIZADO =====")
    print(f"Novas medicoes salvas: {realizadas}")

    # Mostra o historico armazenado
    mostrar_historico()


if __name__ == "__main__":
    iniciar_monitoramento()
