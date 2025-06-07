# Bot de Atendimento Virtual para Telegram - Data Max Solutions

Este projeto implementa um bot simples para Telegram, desenvolvido em Python, como parte de um projeto acadêmico. O bot oferece um menu interativo para fornecer informações sobre a empresa fictícia "Data Max Solutions", seus serviços e coletar feedback.

## Funcionalidades

*   **Mensagem de Boas-Vindas:** Ao iniciar a conversa com o comando `/start`, o bot cumprimenta o usuário e apresenta o menu principal.
*   **Menu Principal:** Oferece três opções:
    1.  **Sobre a empresa:** Exibe informações sobre a Data Max Solutions e seus criadores (alunos da UNINOVE).
    2.  **Nossos serviços:** Apresenta um submenu com os serviços oferecidos (Desenvolvimento de Sistemas, Suporte Técnico, Consultoria em TI). Ao selecionar um serviço, o bot sugere o agendamento de uma reunião (atualmente, apenas informa para entrar em contato).
    3.  **Dar um feedback:** Exibe uma mensagem incentivando o usuário a compartilhar sua opinião.
*   **Navegação:** Botões "Voltar ao Menu" permitem retornar facilmente à tela inicial.

## Requisitos

*   Python 3.7 ou superior instalado.
*   Conta no Telegram.

## Configuração e Execução (Windows)

1.  **Obtenha um Token de Bot:**
    *   Abra o Telegram e procure por "BotFather".
    *   Inicie uma conversa com o BotFather enviando `/start`.
    *   Crie um novo bot enviando `/newbot`.
    *   Siga as instruções para dar um nome e um username ao seu bot (o username deve terminar em "bot", por exemplo, `DataMaxSolucoesBot`).
    *   O BotFather fornecerá um **token de acesso HTTP API**. Guarde este token com segurança, pois você precisará dele.

2.  **Baixe os Arquivos do Projeto:**
    *   Certifique-se de ter os arquivos `bot.py` e `requirements.txt` na mesma pasta no seu computador.

3.  **Instale as Dependências:**
    *   Abra o Prompt de Comando (CMD) ou PowerShell no Windows.
    *   Navegue até a pasta onde você salvou os arquivos do projeto usando o comando `cd` (por exemplo, `cd C:\Users\SeuUsuario\Documents\ProjetoBot`).
    *   Instale as bibliotecas necessárias executando o comando:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Configure o Token no Código:**
    *   Abra o arquivo `bot.py` com um editor de texto (como Bloco de Notas, VS Code, Sublime Text, etc.).
    *   Localize a linha que diz: `TOKEN = "SEU_TOKEN_AQUI"`
    *   Substitua `"SEU_TOKEN_AQUI"` pelo token que você obteve do BotFather. Certifique-se de manter as aspas.
    *   Salve o arquivo `bot.py`.

5.  **Execute o Bot:**
    *   No mesmo Prompt de Comando ou PowerShell, na pasta do projeto, execute o script Python:
        ```bash
        python bot.py
        ```
    *   Se tudo estiver correto, você verá mensagens no terminal indicando que o bot foi iniciado.

6.  **Interaja com o Bot:**
    *   Abra o Telegram e procure pelo username do bot que você criou.
    *   Inicie uma conversa e envie o comando `/start` para ver o menu.

## Estrutura do Código (`bot.py`)

*   **Importações:** Importa as bibliotecas necessárias (`logging`, `telegram`, `telegram.ext`).
*   **Logging:** Configura o sistema de logs para acompanhar a execução e possíveis erros.
*   **Constantes:** Define informações fixas como o token (a ser preenchido), nome da empresa, textos das mensagens, etc.
*   **Handlers:** Funções que respondem a comandos (`start`) ou interações (cliques em botões - `button_callback`).
*   **`main()`:** Função principal que configura o bot com o token, registra os handlers e inicia o bot para receber atualizações do Telegram.
*   **Error Handler:** Uma função para capturar e logar erros que possam ocorrer durante a execução.

## Próximos Passos (Sugestões)

*   Implementar um sistema real de agendamento (ex: integração com Google Calendar API, ou um sistema simples de salvar horários disponíveis).
*   Armazenar feedback dos usuários em um arquivo ou banco de dados.
*   Adicionar mais detalhes sobre cada serviço.
*   Melhorar o tratamento de erros e mensagens ao usuário.

