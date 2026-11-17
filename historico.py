import os
import sys
import sqlite3
from pathlib import Path
from contextlib import closing

from diagnostico_ia import coletar_dados


# Define onde os dados serao armazenados

# Define um local permanente para o banco de dados
if getattr(sys, "frozen", False):
    pasta_local = os.getenv("LOCALAPPDATA")

    if pasta_local:
        PASTA_DADOS = Path(pasta_local) / "PCDoctorAI"
    else:
        PASTA_DADOS = Path.home() / "PCDoctorAI"
else:
    PASTA_DADOS = Path(__file__).resolve().parent / "data"

ARQUIVO_BANCO = PASTA_DADOS / "pcdoctor.db"


def preparar_banco():
    # Cria a pasta data, caso nao exista
    PASTA_DADOS.mkdir(exist_ok=True)

    with closing(sqlite3.connect(ARQUIVO_BANCO)) as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS medicoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_hora TEXT NOT NULL,
                cpu_percentual REAL NOT NULL,
                ram_percentual REAL NOT NULL,
                disco_ocupado_percentual REAL NOT NULL,
                disco_livre_gb REAL NOT NULL
            )
        """)

        conexao.commit()


def salvar_medicao(dados):
    with closing(sqlite3.connect(ARQUIVO_BANCO)) as conexao:
        conexao.execute("""
            INSERT INTO medicoes (
                data_hora,
                cpu_percentual,
                ram_percentual,
                disco_ocupado_percentual,
                disco_livre_gb
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            dados["data_hora"],
            dados["cpu_percentual"],
            dados["ram_percentual"],
            dados["disco_ocupado_percentual"],
            dados["disco_livre_gb"]
        ))

        conexao.commit()


def mostrar_historico():
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
            LIMIT 5
        """).fetchall()

        total = conexao.execute(
            "SELECT COUNT(*) FROM medicoes"
        ).fetchone()[0]

    print("\n===== HISTORICO DO PC DOCTOR AI =====")
    print("Total de medicoes salvas:", total)

    for data, cpu, ram, disco, livre in reversed(registros):
        print(f"\nData e hora: {data}")
        print(f"CPU: {cpu:.1f}%")
        print(f"RAM: {ram:.1f}%")
        print(f"Armazenamento ocupado: {disco:.1f}%")
        print(f"Espaco livre: {livre:.2f} GB")


def main():
    print("========== PC DOCTOR AI ==========")
    print("Coletando informacoes do computador...")

    preparar_banco()

    dados = coletar_dados()
    salvar_medicao(dados)

    print("\nMedicao salva com sucesso!")
    print("Banco de dados:", ARQUIVO_BANCO)

    mostrar_historico()


if __name__ == "__main__":
    main()
