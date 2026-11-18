# PC Doctor AI

**Desenvolvedor:** Daniel Muniz Da Silva  
**Instituição:** Instituto Federal de Mato Grosso do Sul (IFMS)  
**Curso:** Técnico em Informática Integrado ao Ensino Médio  
**Semestre:** 6º semestre  
**Projeto:** INOVIA

## 1. Sobre o PC Doctor AI

O **PC Doctor AI** é um aplicativo para Windows desenvolvido em Python para ajudar o usuário a acompanhar o desempenho do computador. Ele mostra o uso do processador, da memória RAM e do armazenamento, identifica situações que merecem atenção e apresenta explicações em linguagem simples.

O projeto utiliza **regras programadas em Python** para identificar alertas e, quando necessário, o **Ollama com o modelo Llama 3.2 3B** para gerar explicações com inteligência artificial executada localmente.

O PC Doctor AI faz parte do INOVIA, projeto voltado ao estudo e à aplicação prática da inteligência artificial.

## 2. Funcionalidades

Na interface, o usuário encontra:

- **Monitoramento:** exibe CPU, memória RAM, porcentagem de armazenamento ocupado e espaço livre, com atualização periódica.
- **Verificar computador:** atualiza os indicadores e salva uma nova medição.
- **Gerar diagnóstico:** analisa os dados. Sem alertas, mostra uma explicação baseada nas regras do programa; com alertas, consulta a IA local para explicar a situação.
- **Ver histórico:** apresenta as últimas cinco medições registradas no banco SQLite.

O repositório também contém scripts utilizados no desenvolvimento e nos testes, incluindo monitoramento de processos, análise de medições anteriores e simulação de alertas. Essas funções auxiliares não são todas exibidas como botões na interface principal.

O programa **não faz reparos automáticos, não altera configurações do Windows e não funciona como antivírus**.

## 3. Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python 3.14 | Desenvolvimento e testes |
| psutil | Coleta de indicadores do computador |
| CustomTkinter | Interface gráfica |
| SQLite | Histórico local de medições |
| requests | Comunicação com a API local do Ollama |
| Ollama | Execução do modelo de IA no computador |
| Llama 3.2 3B | Geração de explicações dos alertas |
| PyInstaller | Criação do executável para Windows |

## 4. Como instalar e executar

O programa foi desenvolvido e testado no **Windows 11**. A execução em outros computadores pode variar conforme o hardware e as configurações do sistema.

### Opção A — Executar pelo arquivo `.exe`

O executável Windows foi gerado e testado no computador de desenvolvimento. **Quando a primeira versão for publicada**, ela estará disponível na seção **Releases** deste repositório.

1. Instale o Ollama para Windows: https://ollama.com/download/windows
2. Abra o PowerShell e baixe o modelo utilizado pelo programa:

   ```powershell
   ollama pull llama3.2:3b
   ```

3. Confira a instalação com `ollama list`. O modelo `llama3.2:3b` deve aparecer na lista.
4. Quando estiver disponível, baixe o arquivo ZIP na seção **Releases** e extraia seu conteúdo.
5. Abra a pasta extraída e execute `PCDoctorAI.exe`, mantendo a pasta `_internal` junto do executável.
6. Mantenha o Ollama disponível para utilizar os diagnósticos com IA.

A versão `.exe` **não exige instalar o Python separadamente**, mas a geração de explicações por IA exige o Ollama e o modelo indicados acima.

**Observação:** o executável não possui assinatura digital profissional e pode apresentar avisos de segurança em determinados computadores. Ele foi testado no computador de desenvolvimento, mas ainda não foi validado em diferentes máquinas.

### Opção B — Executar pelo código Python

1. Instale o Python (a versão utilizada no desenvolvimento foi a 3.14): https://www.python.org/downloads/
2. Instale o Ollama e baixe o modelo conforme os passos anteriores.
3. Baixe ou clone este repositório e abra um terminal na pasta do projeto.
4. Crie um ambiente virtual:

   ```powershell
   python -m venv .venv
   ```

5. Instale as dependências:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

6. Execute a interface:

   ```powershell
   .\.venv\Scripts\python.exe interface_pcdoctor.py
   ```

## 5. Como utilizar

Na tela principal, acompanhe os indicadores de CPU, RAM, armazenamento ocupado e espaço livre.

- Clique em **Verificar computador** para atualizar os valores e registrar uma medição.
- Clique em **Gerar diagnóstico** para receber uma explicação dos indicadores. A IA local é consultada quando as regras identificam alertas.
- Clique em **Ver histórico** para visualizar as cinco medições mais recentes.

O histórico fica armazenado **no próprio computador**. Durante a execução em Python, o banco é criado em `data/pcdoctor.db`. Na versão empacotada, é utilizado o diretório `%LOCALAPPDATA%\PCDoctorAI\pcdoctor.db`.

## 6. Funcionamento sem internet

A internet é necessária para baixar e instalar inicialmente o Ollama e o modelo. Após essa preparação, o diagnóstico com IA pode funcionar **sem conexão com a internet**, desde que o Ollama esteja em execução e o modelo esteja disponível localmente.

Esse funcionamento foi verificado em um teste com alerta simulado de memória RAM elevada.

## 7. Testes realizados

Os resultados abaixo são **observações no computador de desenvolvimento**, não requisitos mínimos nem valores máximos de consumo:

| Teste | Resultado observado |
|---|---|
| CPU do `PCDoctorAI.exe`, após cerca de 30 segundos | 3,2% |
| Memória do `PCDoctorAI.exe` | 37,1 MB |
| Memória do processo `llama-server` em uma captura | aproximadamente 2.447 MB |
| Tempo de uma resposta da IA a um alerta simulado | 10,10 segundos |
| Geração de explicação local sem internet | Funcionou no teste |
| Abertura e diagnóstico básico no `.exe` | Funcionaram no computador de desenvolvimento |

O computador de desenvolvimento utiliza **Windows 11 e processador AMD Ryzen 5 4600G**. O consumo e o tempo de resposta podem variar em outros equipamentos. A resposta por IA dentro do executável ainda não foi validada com um alerta real.

## 8. Limitações

O PC Doctor AI monitora indicadores básicos de desempenho, mas não identifica todas as possíveis causas de lentidão, não faz manutenção automática e não substitui um profissional especializado. As explicações produzidas pela inteligência artificial podem apresentar erros e devem ser consideradas **orientações informativas**.

O programa não substitui ferramentas de segurança ou antivírus. A versão executável ainda não passou por testes de distribuição em diferentes computadores.

## 9. Autor

**Daniel Muniz Da Silva**  
Estudante do curso Técnico em Informática Integrado ao Ensino Médio do Instituto Federal de Mato Grosso do Sul (IFMS).
