
import os
import time
import psutil
from datetime import datetime


def obter_processos():
    processos = []

    for processo in psutil.process_iter(
        ["pid", "name", "memory_info"]
    ):
        try:
            info = processo.info
            memoria = info["memory_info"]

            if memoria is None:
                continue

            memoria_mb = memoria.rss / (1024 ** 2)

            processos.append({
                "pid": info["pid"],
                "nome": info["name"] or "Desconhecido",
                "memoria": memoria_mb
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    processos.sort(
        key=lambda p: p["memoria"],
        reverse=True
    )

    return processos[:5]


def mostrar_monitoramento():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disco = psutil.disk_usage("C:\\")

    # Limpa a tela do terminal
    os.system("cls")

    print("========== PC DOCTOR AI ==========")
    print("MONITORAMENTO EM TEMPO REAL")
    print("Atualizado em:",
          datetime.now().strftime("%H:%M:%S"))

    print("\n--- DESEMPENHO ---")
    print(f"CPU: {cpu:.1f}%")
    print(f"RAM: {ram.percent:.1f}%")
    print(f"Armazenamento C: {disco.percent:.1f}%")

    print("\n--- TOP 5 PROCESSOS POR RAM ---")

    for processo in obter_processos():
        print(
            f"{processo['nome'][:25]:<25} "
            f"{processo['memoria']:.1f} MB"
        )

    print("\nAtualizando automaticamente...")
    print("Pressione Ctrl + C para encerrar.")


try:
    while True:
        mostrar_monitoramento()
        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")
