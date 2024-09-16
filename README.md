# DocMed Chat

DocMed Chat é um sistema de chatbot desenvolvido para auxiliar no descobrimento sobre pacientes com Miastenia Gravis por meio de perguntas e respostas predeterminadas. Este projeto foi desenvolvido utilizando PyQt5 para a interface gráfica.

## Funcionalidades

- Interface de usuário com tema escuro.
- Mensagem de boas-vindas ao iniciar o programa.
- Botão "Nova Consulta" que inicia uma nova consulta e faz a primeira pergunta.
- Botão "Sair" que fecha a aplicação.
- Respostas predeterminadas para as perguntas do chatbot.

## Requisitos

- Python 3.x
- PyQt5

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/docmed-chat.git
   cd docmed-chat

2. Crie um ambiente virtual (opcional, mas recomendado):
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. Instale as dependências:
    pip install PyQt5

## Uso

1. Execute o script principal:
    python main.py

2. A interface do DocMed Chat será exibida. Você verá uma mensagem de boas-vindas.

3. Clique no botão "Nova Consulta" para iniciar uma nova consulta. A primeira pergunta será feita após uma mensagem de "digitando...".

4. Responda à pergunta com "1" para primeira consulta ou "2" para retorno. Se você inserir uma resposta inválida, o chatbot responderá com uma mensagem de erro.

5. Use o botão "Sair" para fechar a aplicação.



