# PC Doctor AI

**Projeto integrante do INOVAIA**

**Desenvolvedor:** Daniel Muniz Da Silva  
**Instituição:** Instituto Federal de Mato Grosso do Sul (IFMS)  
**Curso:** Técnico em Informática Integrado ao Ensino Médio  
**Semestre:** 6º semestre

## 1. Sobre o INOVAIA

O **INOVAIA** é um projeto desenvolvido como parte das atividades de estágio de estudantes do curso Técnico em Informática Integrado ao Ensino Médio do IFMS.

O projeto reúne trabalhos relacionados à inteligência artificial e suas aplicações em diferentes áreas da tecnologia. A proposta é explorar ferramentas de IA, estudar seu funcionamento e desenvolver aplicações práticas que possam ser documentadas em artigos técnicos e científicos.

Cada integrante desenvolve seu próprio trabalho, abordando uma aplicação ou possibilidade de utilização da inteligência artificial.

O **PC Doctor AI** é um dos projetos desenvolvidos dentro do INOVAIA, com foco na utilização de inteligência artificial local para auxiliar no diagnóstico de computadores.

## 2. Sobre o PC Doctor AI

O PC Doctor AI é um programa para Windows desenvolvido em Python, que utiliza inteligência artificial executada localmente para auxiliar na identificação de possíveis problemas de desempenho do computador.

O sistema coleta informações sobre o uso do processador, memória RAM e armazenamento, identifica indicadores que merecem atenção e apresenta explicações simples ao usuário.

A proposta é facilitar a compreensão do funcionamento do computador, principalmente para pessoas que não possuem conhecimentos técnicos em informática.

O programa utiliza o Ollama para executar um modelo de inteligência artificial diretamente no computador, sem depender de serviços externos para gerar os diagnósticos.

## 3. Objetivo

Desenvolver uma aplicação simples de monitoramento e diagnóstico computacional, integrando Python e inteligência artificial local para interpretar informações do Windows e apresentar recomendações compreensíveis ao usuário.

O projeto também busca demonstrar a possibilidade de utilizar modelos de linguagem em computadores pessoais, sem a necessidade de uma placa de vídeo dedicada.

## 4. Funcionalidades

O PC Doctor AI possui as seguintes funcionalidades:

- Monitoramento do uso de CPU, memória RAM e armazenamento.
- Atualização automática das informações exibidas.
- Consulta aos processos ativos por meio dos módulos de monitoramento.
- Identificação de possíveis problemas por regras programadas.
- Análise de medições anteriores para identificar utilização elevada repetida.
- Diagnósticos com auxílio de inteligência artificial local.
- Explicações em linguagem simples para usuários sem conhecimento técnico.
- Interface gráfica desenvolvida em Python.
- Armazenamento do histórico de medições utilizando SQLite.
- Consulta das últimas medições realizadas.

As medições são atualizadas automaticamente na interface. O armazenamento de uma nova medição no histórico ocorre quando o usuário utiliza o botão de verificação.

O sistema não realiza correções automáticas nem altera configurações do Windows.

## 5. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.14 | Desenvolvimento do programa |
| Ollama | Execução da inteligência artificial local |
| Llama 3.2 3B | Geração de explicações dos diagnósticos |
| Psutil | Coleta de informações do computador |
| CustomTkinter | Desenvolvimento da interface gráfica |
| SQLite | Armazenamento das medições |
| Requests | Comunicação entre Python e Ollama |
| PyInstaller | Criação do executável para Windows |

## 6. Como instalar e executar

O PC Doctor AI pode ser executado diretamente pelo Python. Uma versão executável para Windows também está prevista.

### Opção 1 — Executar pelo Python

**1. Instalar o Python**

Baixe e instale o Python 3.14:

https://www.python.org/downloads/

**2. Instalar o Ollama**

Baixe o Ollama para Windows:

https://ollama.com/download/windows

**3. Baixar o modelo de inteligência artificial**

Após instalar o Ollama, abra o terminal e execute:

`ollama pull llama3.2:3b`

Esse comando baixa o modelo que será utilizado pelo programa.

**4. Baixar o PC Doctor AI**

Baixe os arquivos deste repositório e extraia a pasta do projeto.

**5. Criar um ambiente virtual**

Abra o terminal na pasta do projeto e execute:

`python -m venv .venv`

**6. Instalar as bibliotecas**

Execute:

`.\.venv\Scripts\python.exe -m pip install -r requirements.txt`

**7. Iniciar o programa**

Com o Ollama em execução, utilize:

`.\.venv\Scripts\python.exe interface_pcdoctor.py`

A interface gráfica do PC Doctor AI será aberta.

### Opção 2 — Executar pelo arquivo .exe

**O executável ainda está em desenvolvimento e será disponibilizado após os testes finais.**

A versão executável permitirá utilizar o programa sem instalar separadamente o Python e as bibliotecas do projeto.

Para utilizá-la, será necessário:

1. Instalar o Ollama no Windows.
2. Baixar o modelo utilizando `ollama pull llama3.2:3b`.
3. Acessar a seção **Releases** deste repositório.
4. Baixar a versão disponível do PC Doctor AI.
5. Extrair os arquivos, caso estejam compactados.
6. Executar `PCDoctorAI.exe` com o Ollama em funcionamento.

O executável e suas instruções definitivas serão disponibilizados após a conclusão dos testes de distribuição.

## 7. Como utilizar

Após abrir o PC Doctor AI, o usuário encontrará uma interface com as informações principais do computador e três botões.

**Verificar computador**

Coleta informações atualizadas sobre o processador, memória RAM e armazenamento, além de salvar uma nova medição no histórico.

**Gerar diagnóstico**

Analisa as informações coletadas e verifica se algum indicador ultrapassou os limites definidos.

Quando não existem alertas, o programa apresenta uma explicação baseada nas regras desenvolvidas em Python.

Quando existem alertas, o sistema pode utilizar o modelo Llama 3.2 3B para explicar a situação em linguagem simples.

**Ver histórico**

Permite visualizar as cinco últimas medições armazenadas no banco de dados.

## 8. Armazenamento das informações

O PC Doctor AI utiliza SQLite para armazenar as medições realizadas.

Durante o desenvolvimento pelo Python, os dados ficam no arquivo `data/pcdoctor.db`.

Na versão executável, o banco será armazenado em uma pasta própria do aplicativo dentro dos dados locais do usuário no Windows.

O histórico é mantido localmente e não exige uma conta online.

O arquivo do banco de dados não está incluído no repositório, pois cada instalação cria seu próprio histórico.

## 9. Requisitos do sistema

O programa foi desenvolvido para computadores com Windows.

**Computador utilizado no desenvolvimento:**

- Processador AMD Ryzen 5 4600G.
- Sistema operacional Windows.
- Execução da IA utilizando recursos locais do computador.
- Sem necessidade de placa de vídeo dedicada.

O funcionamento em computadores com outras configurações dependerá dos recursos disponíveis, principalmente da memória RAM e do processador.

O modelo precisa ser baixado com conexão à internet na primeira instalação. Depois disso, os diagnósticos locais podem funcionar sem internet, desde que o Ollama e o modelo estejam disponíveis.

## 10. Limitações

O PC Doctor AI é um projeto de caráter técnico e educacional.

Seus diagnósticos são baseados em indicadores de desempenho e não garantem a identificação de todos os possíveis problemas do computador.

O modelo de inteligência artificial também pode produzir explicações imprecisas. Por esse motivo, o programa utiliza regras desenvolvidas em Python para identificar inicialmente situações que merecem atenção.

O sistema não substitui a avaliação de um profissional especializado e não funciona como antivírus.

## 11. Desenvolvimento e artigo científico

O PC Doctor AI faz parte das atividades desenvolvidas no INOVAIA e será documentado em um artigo técnico-científico.

O artigo abordará a utilização de inteligência artificial local, as ferramentas escolhidas, o processo de desenvolvimento, o funcionamento do sistema, os testes realizados e as limitações identificadas.

O objetivo é apresentar uma aplicação prática que possa ser compreendida, executada e analisada no contexto da formação técnica em Informática.

## 12. Autor

**Daniel Muniz Da Silva**

Estudante do curso Técnico em Informática Integrado ao Ensino Médio do Instituto Federal de Mato Grosso do Sul (IFMS).

Projeto individual desenvolvido como parte do **INOVAIA**, trabalho coletivo voltado ao estudo e à aplicação de inteligência artificial e tecnologias relacionadas.