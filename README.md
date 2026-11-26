
# PC Doctor AI

**Projeto desenvolvido no contexto do INOVIA**

**Integrantes:**
- Daniel Muniz da Silva
- Victor Augusto Lino Rocha 

**Instituição:** Instituto Federal de Mato Grosso do Sul (IFMS)  
**Curso:** Técnico em Informática Integrado ao Ensino Médio  
**Turma:** 1212A  
**Semestre:** 6º semestre

## 1. Sobre o projeto

O PC Doctor AI é um programa para Windows desenvolvido em Python, que utiliza inteligência artificial local para auxiliar na identificação de possíveis problemas de desempenho do computador.

O sistema coleta informações sobre o uso do processador, memória RAM e armazenamento, identifica indicadores que merecem atenção e apresenta explicações simples ao usuário.

A proposta é facilitar a compreensão do funcionamento do computador, principalmente para pessoas que não possuem conhecimentos avançados em informática.

O programa utiliza o Ollama para executar um modelo de inteligência artificial diretamente no computador, sem depender de serviços externos para gerar os diagnósticos.

O PC Doctor AI faz parte das atividades desenvolvidas no projeto INOVIA, voltado ao estudo e à aplicação prática da inteligência artificial.

## 2. Objetivo

Desenvolver uma aplicação simples de monitoramento e diagnóstico computacional, integrando Python e inteligência artificial local para interpretar informações do Windows e apresentar recomendações compreensíveis ao usuário.

O projeto também busca demonstrar que é possível utilizar modelos de linguagem em computadores pessoais, inclusive sem placa de vídeo dedicada, dependendo dos recursos disponíveis.

Além do desenvolvimento do programa, o trabalho envolve testes, documentação e orientações para que outras pessoas consigam instalar e utilizar a ferramenta.

## 3. Funcionalidades

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

## 4. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.14 | Desenvolvimento do programa |
| Ollama | Execução da inteligência artificial local |
| Llama 3.2 3B | Geração de explicações dos diagnósticos |
| psutil | Coleta de informações do computador |
| CustomTkinter | Desenvolvimento da interface gráfica |
| SQLite | Armazenamento das medições |
| Requests | Comunicação entre Python e Ollama |
| PyInstaller | Criação do executável para Windows |
| Git e GitHub | Versionamento e distribuição do projeto |

## 5. Como instalar e executar

O PC Doctor AI pode ser utilizado pelo arquivo executável para Windows ou diretamente pelo código Python.

### Opção 1 — Executar pelo arquivo .exe

Esta é a opção mais simples para quem deseja apenas utilizar o programa.

**1. Instalar o Ollama**

Acesse:

https://ollama.com/download/windows

Baixe e instale o Ollama para Windows.

**2. Baixar o modelo de inteligência artificial**

Após instalar o Ollama, abra o PowerShell ou o Terminal do Windows e execute:

```powershell
ollama pull llama3.2:3b
```

Esse comando baixa o modelo utilizado pelo PC Doctor AI.

Para conferir se o modelo foi instalado corretamente, execute:

```powershell
ollama list
```

O modelo `llama3.2:3b` deverá aparecer na lista.

**3. Baixar o PC Doctor AI**

Acesse a página de download da versão 0.1.0:

https://github.com/Roushinooll/PCDoctorAI/releases/tag/v0.1.0

Na seção de arquivos da Release, baixe:

`PCDoctorAI-Windows-v0.1.0.zip`

**4. Extrair o programa**

Extraia o conteúdo do arquivo ZIP.

É importante manter o arquivo `PCDoctorAI.exe` junto da pasta `_internal`, pois ela contém componentes necessários para o funcionamento do programa.

**5. Executar o aplicativo**

Abra a pasta extraída e execute:

`PCDoctorAI.exe`

A interface gráfica do PC Doctor AI será aberta.

Não é necessário instalar separadamente o Python para executar essa versão. Entretanto, o Ollama e o modelo Llama 3.2 3B precisam estar disponíveis para a geração de diagnósticos com inteligência artificial.

O executável não possui assinatura digital profissional e pode apresentar avisos de segurança em determinados computadores.

### Opção 2 — Executar pelo Python

Esta opção é indicada para quem deseja estudar o código, realizar testes ou contribuir com o desenvolvimento.

**1. Instalar o Python**

Baixe o Python 3.14:

https://www.python.org/downloads/

**2. Instalar o Ollama**

Baixe e instale o Ollama:

https://ollama.com/download/windows

**3. Baixar o modelo**

No terminal, execute:

```powershell
ollama pull llama3.2:3b
```

**4. Baixar o projeto**

Clone o repositório:

```powershell
git clone https://github.com/Roushinooll/PCDoctorAI.git
```

Ou baixe o código-fonte pelo botão **Code > Download ZIP** no GitHub.

**5. Criar um ambiente virtual**

Abra o terminal na pasta do projeto e execute:

```powershell
python -m venv .venv
```

**6. Instalar as bibliotecas**

Execute:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**7. Iniciar o programa**

Com o Ollama em funcionamento, execute:

```powershell
.\.venv\Scripts\python.exe interface_pcdoctor.py
```

A interface gráfica do PC Doctor AI será aberta.

## 6. Como utilizar

Após abrir o PC Doctor AI, o usuário encontrará uma interface com informações sobre o desempenho do computador e três botões principais.

### Verificar computador

Coleta informações atualizadas sobre o processador, memória RAM e armazenamento, além de salvar uma nova medição no histórico.

### Gerar diagnóstico

Analisa as informações coletadas e verifica se algum indicador ultrapassou os limites definidos.

Quando não existem alertas, o programa apresenta uma explicação baseada nas regras desenvolvidas em Python.

Quando existem alertas, o sistema utiliza o modelo Llama 3.2 3B para auxiliar na explicação da situação em linguagem simples.

### Ver histórico

Permite visualizar as cinco últimas medições armazenadas no banco de dados.

## 7. Armazenamento das informações

O PC Doctor AI utiliza SQLite para armazenar as medições realizadas.

Durante o desenvolvimento pelo Python, os dados ficam no arquivo:

`data/pcdoctor.db`

Na versão executável, o banco de dados é armazenado na pasta de dados locais do usuário no Windows, dentro do diretório do PC Doctor AI.

O histórico é mantido localmente e não exige uma conta online.

O arquivo do banco de dados não está incluído no repositório, pois cada instalação cria seu próprio histórico.

## 8. Requisitos do sistema

O programa foi desenvolvido para computadores com Windows.

**Computador utilizado no desenvolvimento e nos testes:**

- Sistema operacional Windows 11.
- Processador AMD Ryzen 5 4600G.
- Execução local do modelo Llama 3.2 3B.
- Sem necessidade de placa de vídeo dedicada no ambiente testado.

O funcionamento em computadores com outras configurações dependerá dos recursos disponíveis, principalmente da memória RAM e do processador.

O modelo precisa ser baixado com conexão à internet na primeira instalação. Depois disso, os diagnósticos locais podem funcionar sem internet, desde que o Ollama e o modelo estejam disponíveis.

## 9. Testes e resultados

Durante o desenvolvimento, foram realizados testes de monitoramento, armazenamento de histórico, geração de diagnósticos e funcionamento da inteligência artificial local.

Os testes também incluíram a execução do aplicativo pelo arquivo `.exe`, sem necessidade de abrir o código pelo VS Code.

### Consumo do aplicativo

Em uma observação realizada após aproximadamente 30 segundos de funcionamento, o executável apresentou:

- CPU: 3,2%.
- Memória RAM: 37,1 MB.

Esses valores representam uma observação específica no computador utilizado, não o consumo máximo do aplicativo.

### Consumo da inteligência artificial

Em um teste separado, o processo `llama-server`, responsável pela execução do modelo Llama 3.2 3B, utilizou aproximadamente 2.447 MB de memória RAM.

Esse valor também representa uma medição pontual.

### Tempo de resposta

Foram realizados testes com alertas simulados de utilização elevada da memória RAM.

Em uma das execuções, a inteligência artificial apresentou uma resposta em aproximadamente 10,10 segundos.

### Funcionamento sem internet

O Ollama foi testado com o computador desconectado da internet e conseguiu gerar explicações utilizando o modelo instalado localmente.

Esses resultados demonstram o funcionamento do projeto no ambiente utilizado nos testes.

## 10. Limitações

O PC Doctor AI é um projeto de caráter técnico e educacional.

Seus diagnósticos são baseados em indicadores de desempenho e não garantem a identificação de todos os possíveis problemas do computador.

O modelo de inteligência artificial também pode produzir explicações imprecisas. Por isso, o programa utiliza regras desenvolvidas em Python para identificar inicialmente situações que merecem atenção.

O aplicativo:

- Não realiza reparos automáticos.
- Não altera configurações do Windows.
- Não funciona como antivírus.
- Não substitui a avaliação de um profissional especializado.
- Não garante funcionamento idêntico em computadores com configurações diferentes.

A versão executável foi testada no computador de desenvolvimento. Os diagnósticos com IA para situações de alerta foram testados com dados simulados pelo Python.

## 11. Desenvolvimento e responsabilidades

O PC Doctor AI é um projeto desenvolvido no contexto das atividades de estágio do curso Técnico em Informática Integrado ao Ensino Médio do IFMS.

O trabalho envolve diferentes atividades de programação, monitoramento computacional, integração de inteligência artificial, testes, documentação e distribuição.

**Daniel Muniz da Silva**

Responsável pelo desenvolvimento principal da aplicação, incluindo a implementação do monitoramento, integração da inteligência artificial, banco de dados, interface gráfica, empacotamento e documentação técnica.

**Victor Augusto Rocha Lino**

Responsável pela frente de testes complementares em Python, incluindo validação das regras de diagnóstico, testes de coleta de dados com psutil, verificação do SQLite, comunicação com o Ollama e análise do histórico. Essas contribuições devem ser registradas conforme forem realizadas.

O projeto também possui um artigo técnico que apresenta sua finalidade, as ferramentas utilizadas, os procedimentos de instalação, os testes e suas limitações.

## 12. Integrantes

**Daniel Muniz da Silva**  
**Victor Augusto Lino Rocha **

Estudantes do curso Técnico em Informática Integrado ao Ensino Médio do Instituto Federal de Mato Grosso do Sul (IFMS).

Projeto desenvolvido no contexto do **INOVIA**, iniciativa voltada ao estudo e à aplicação prática da inteligência artificial.
