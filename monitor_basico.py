
import psutil
from datetime import datetime

# Converte bytes para gigabytes
def converter_gb(valor):
    return valor / (1024 ** 3)


# Coleta informacoes do computador
def monitorar_computador():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disco = psutil.disk_usage("C:\\")

    print("\n========== PC DOCTOR AI ==========")
    print("Data:", datetime.now().strftime("%d/%m/%Y"))
    print("Hora:", datetime.now().strftime("%H:%M:%S"))

    print("\n--- PROCESSADOR ---")
    print(f"Uso da CPU: {cpu:.1f}%")

    print("\n--- MEMORIA RAM ---")
    print(f"Uso da RAM: {ram.percent:.1f}%")
    print(f"RAM total: {converter_gb(ram.total):.2f} GB")
    print(f"RAM disponivel: {converter_gb(ram.available):.2f} GB")

    print("\n--- ARMAZENAMENTO C: ---")
    print(f"Uso do disco: {disco.percent:.1f}%")
    print(f"Espaco total: {converter_gb(disco.total):.2f} GB")
    print(f"Espaco livre: {converter_gb(disco.free):.2f} GB")

    print("\n==================================")


monitorar_computador()
