
import requests
import time

# Endereco da IA local
URL = "http://localhost:11434/api/generate"

# Informacoes enviadas ao Ollama
dados = {
    "model": "llama3.2:1b",
    "prompt": (
        "Responda em portugues, de forma breve: "
        "o que pode causar uso elevado de CPU "
        "em um computador Windows?"
    ),
    "stream": False
}

print("=== PC DOCTOR AI ===")
print("Conectando a inteligencia artificial...")

inicio = time.perf_counter()

try:
    resposta = requests.post(
        URL,
        json=dados,
        timeout=(5, 180)
    )

    resposta.raise_for_status()

    resultado = resposta.json()
    tempo = time.perf_counter() - inicio

    print("\nResposta da IA:")
    print(resultado["response"])

    print(f"\nTempo da requisicao: {tempo:.2f} segundos")

except requests.exceptions.RequestException as erro:
    print("\nErro ao conectar com o Ollama:")
    print(erro)
