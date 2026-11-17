
from analise_regras import analisar_indicadores
from diagnostico_com_regras2 import explicar_com_ia
print("Versao utilizada:", explicar_com_ia.__module__)


# Dados ficticios para testar o diagnostico
dados_simulados = {
    "cpu_percentual": 12.0,
    "ram_percentual": 95.0,
    "disco_ocupado_percentual": 73.9,
    "disco_livre_gb": 58.18
}

print("========== PC DOCTOR AI ==========")
print("TESTE COM DADOS SIMULADOS")
print("Estes valores NAO sao do computador real.\n")

# Verifica os indicadores
alertas = analisar_indicadores(dados_simulados)

print("Avisos encontrados:", len(alertas))

for alerta in alertas:
    print("-", alerta)

# Solicita a explicacao da IA local
explicar_com_ia(dados_simulados, alertas)
