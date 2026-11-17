
import psutil

def listar_processos():
    processos = []

    # Percorre os processos ativos no Windows
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

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Ordena do maior para o menor consumo de RAM
    processos.sort(
        key=lambda p: p["memoria"],
        reverse=True
    )

    print("\n========== PC DOCTOR AI ==========")
    print("TOP 10 PROCESSOS POR USO DE RAM\n")

    print(f"{'PID':<10} {'PROCESSO':<30} {'RAM (MB)':>12}")
    print("-" * 54)

    for processo in processos[:10]:
        print(
            f"{processo['pid']:<10} "
            f"{processo['nome'][:29]:<30} "
            f"{processo['memoria']:>12.2f}"
        )

    print("\nTotal de processos identificados:", len(processos))
    print("==================================")


listar_processos()
