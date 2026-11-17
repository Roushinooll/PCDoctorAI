
import customtkinter as ctk
import requests
import sqlite3

from contextlib import closing
from historico import preparar_banco, salvar_medicao, ARQUIVO_BANCO

from threading import Thread
from queue import Queue, Empty

from diagnostico_ia import coletar_dados
from analise_regras import analisar_indicadores


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2:3b"

dados_atuais = None
fila_respostas = Queue()


def mostrar_diagnostico(texto):
    caixa_ia.configure(state="normal")
    caixa_ia.delete("1.0", "end")
    caixa_ia.insert("1.0", texto)
    caixa_ia.configure(state="disabled")


def ver_historico():
    try:
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
                LIMIT 5
            """).fetchall()

        if not registros:
            mostrar_diagnostico(
                "Nenhuma medicao foi salva ainda."
            )
            return

        texto = "ULTIMAS MEDICOES DO COMPUTADOR\n\n"

        for data, cpu, ram, disco, livre in registros:
            texto += (
                f"Data: {data.replace('T', ' ')}\n"
                f"Processador: {cpu:.1f}%\n"
                f"Memoria RAM: {ram:.1f}%\n"
                f"Armazenamento: {disco:.1f}% ocupado\n"
                f"Espaco livre: {livre:.2f} GB\n"
                "-----------------------------\n"
            )

        mostrar_diagnostico(texto)

    except sqlite3.Error as erro:
        mostrar_diagnostico(
            f"Erro ao consultar o historico:\n{erro}"
        )



def consultar_computador(salvar=False):
    global dados_atuais

    try:
        dados_atuais = coletar_dados()

        # Salva a medicao quando solicitado
        if salvar:
            preparar_banco()
            salvar_medicao(dados_atuais)

        dados = dados_atuais

        texto = (
            f"Processador: {dados['cpu_percentual']:.1f}% em uso\n\n"
            f"Memoria RAM: {dados['ram_percentual']:.1f}% em uso\n\n"
            f"Armazenamento: "
            f"{dados['disco_ocupado_percentual']:.1f}% ocupado\n\n"
            f"Espaco livre: {dados['disco_livre_gb']:.2f} GB"
        )

        resultado.configure(text=texto)

    except Exception as erro:
        resultado.configure(text=f"Erro na coleta: {erro}")


def consultar_ia():
    if dados_atuais is None:
        mostrar_diagnostico(
            "Primeiro clique em Verificar computador."
        )
        return

    botao_ia.configure(state="disabled")
    mostrar_diagnostico("Consultando a inteligencia artificial...")

    tarefa = Thread(
        target=gerar_resposta,
        args=(dados_atuais.copy(),),
        daemon=True
    )
    tarefa.start()


def gerar_resposta(dados):
    avisos = analisar_indicadores(dados)


    # Quando nao existem avisos, usa a explicacao das regras
    if not avisos:
        texto = (
            "RESULTADO DA ANALISE\n\n"
            "Seu computador nao apresentou indicadores "
            "acima dos limites de atencao.\n\n"

            "O processador e a memoria RAM estao sendo "
            "utilizados normalmente nesta medicao.\n\n"

            f"Voce ainda possui {dados['disco_livre_gb']:.2f} GB "
            "livres para armazenar seus arquivos.\n\n"

            "Nenhuma acao e necessaria com base "
            "nesses indicadores.\n\n"

            "Esta verificacao nao descarta outros problemas.\n\n"
            "Explicacao fornecida pelas regras do programa."
        )

        fila_respostas.put(texto)
        return

    if avisos:
        verificacao = "\n".join(avisos)
    else:
        verificacao = (
            "Nenhum indicador ultrapassou os limites "
            "de atencao nesta medicao."
        )


    instrucoes = (
        "Voce e um assistente de informatica para iniciantes. "
        "Explique os avisos recebidos em portugues brasileiro. "
        "Escreva um unico paragrafo com no maximo 3 frases. "
        "Explique o significado do aviso e sugira um cuidado simples. "
        "Use apenas os problemas identificados pelo programa. "
        "Nao acrescente outros problemas ou informacoes. "
        "Nao use listas, titulos ou numeracao."
    )



    pergunta = (
        "Explique estes avisos do computador: "
        + " ".join(avisos)
    )


    try:
        resposta = requests.post(
            URL,
            json={
                "model": MODELO,
                "system": instrucoes,
                "prompt": pergunta,
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "num_predict": 300
                }
            },
            timeout=(5, 120)
        )

        resposta.raise_for_status()
        explicacao = resposta.json().get("response", "").strip()

        if not explicacao:
            explicacao = "A IA nao retornou uma explicacao."

        explicacao = explicacao.replace("**", "")

        texto = (
            "RESULTADO DAS VERIFICACOES\n"
            + verificacao
            + "\n\nEXPLICACAO DA IA\n"
            + explicacao
        )

    except (requests.exceptions.RequestException, ValueError) as erro:
        texto = (
            "RESULTADO DAS VERIFICACOES\n"
            + verificacao
            + "\n\nNao foi possivel consultar a IA:\n"
            + str(erro)
        )

    fila_respostas.put(texto)


def verificar_respostas():
    try:
        texto = fila_respostas.get_nowait()
    except Empty:
        pass
    else:
        mostrar_diagnostico(texto)
        botao_ia.configure(state="normal")

    janela.after(200, verificar_respostas)


def atualizar_automaticamente():
    consultar_computador()
    janela.after(5000, atualizar_automaticamente)


# Janela principal
janela = ctk.CTk()
janela.title("PC Doctor AI")
janela.geometry("700x640")
janela.minsize(550, 570)

titulo = ctk.CTkLabel(
    janela,
    text="PC Doctor AI",
    font=("Arial", 28, "bold")
)
titulo.pack(pady=(25, 5))

subtitulo = ctk.CTkLabel(
    janela,
    text="Monitoramento inteligente do computador"
)
subtitulo.pack(pady=(0, 15))

painel = ctk.CTkFrame(janela)
painel.pack(padx=30, pady=10, fill="x")

resultado = ctk.CTkLabel(
    painel,
    text="Clique em Verificar computador.",
    font=("Arial", 16),
    justify="left"
)
resultado.pack(padx=20, pady=25)

botao_verificar = ctk.CTkButton(
    janela,
    text="Verificar computador",
    command=lambda: consultar_computador(salvar=True)
)
botao_verificar.pack(pady=8)

botao_ia = ctk.CTkButton(
    janela,
    text="Gerar diagnostico",
    command=consultar_ia
)
botao_ia.pack(pady=8)


botao_historico = ctk.CTkButton(
    janela,
    text="Ver historico",
    command=ver_historico
)
botao_historico.pack(pady=8)


caixa_ia = ctk.CTkTextbox(
    janela,
    font=("Arial", 14),
    wrap="word"
)
caixa_ia.pack(
    padx=30,
    pady=(10, 20),
    fill="both",
    expand=True
)

mostrar_diagnostico(
    "O diagnostico aparecera aqui apos consultar a IA."
)

janela.after(5000, atualizar_automaticamente)
janela.after(200, verificar_respostas)

janela.mainloop()
