
# DocMed Chat - Sistema de Consulta para Miastenia Gravis

## Descrição

O **DocMed Chat** é um sistema de chatbot desenvolvido para auxiliar no diagnóstico de pacientes com **Miastenia Gravis** (MG), utilizando perguntas baseadas na escala **MGFA** (Miastenia Gravis Foundation of America). O sistema permite que o usuário/médico responda a perguntas sobre os sintomas do paciente e, ao final, o chatbot classifica os sintomas e recomenda o próximo passo com base na gravidade da condição. O projeto faz uso da **API GPT-4 da OpenAI** para validar as respostas e direcionar o fluxo da consulta.

## Funcionalidades

- **Chatbot interativo** para coleta de informações e diagnósticos preliminares.
- **Interface gráfica** desenvolvida em **PyQt5**, com janelas de configuração, consulta e resultados.
- **Integração com a API GPT-4** para validação e processamento das respostas.
- **Pontuação baseada na escala MGFA**, classificando a Miastenia Gravis em cinco diferentes classes de severidade.
- Armazenamento e carregamento de **chaves API** e **dados de consulta** em arquivos JSON.
- Interface com tema **escuro**, responsiva e de fácil navegação.

## Requisitos

### Dependências

- **Python 3.8+**
- **PyQt5**: Interface gráfica para a aplicação.
- **OpenAI API**: Para integração com GPT-4.
- **Bibliotecas adicionais**: `sys`, `json`, `re`

### Instalação das Dependências

Para instalar as dependências necessárias, execute:

```bash
pip install PyQt5 openai
```

## Como Utilizar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seuusuario/docmed-chat.git
   cd docmed-chat
   ```

2. **Configure a chave da API OpenAI**:
   
   O sistema requer uma chave de API válida da **OpenAI** para interagir com o modelo GPT-4. A chave é armazenada em um arquivo `config.json`.

   - Ao rodar o sistema pela primeira vez, um diálogo será exibido para que você insira a chave da API. 
   - Alternativamente, você pode criar o arquivo `config.json` manualmente no formato:

     ```json
     {
       "api_key": "sua_chave_api"
     }
     ```

3. **Execute o aplicativo**:

   Para iniciar a aplicação, execute o comando:

   ```bash
   python main.py
   ```

4. **Inicie uma nova consulta**:

   - Na interface, clique em **"Nova Consulta"** para começar.
   - O chatbot fará perguntas ao usuário com base em um questionário pré-carregado e validará as respostas usando GPT-4.
   - Ao final do questionário, o sistema perguntará se você deseja prosseguir com a **Escala MGFA**.

5. **Visualize os resultados**:

   - Após responder todas as perguntas, o sistema exibirá uma **pontuação total** e a **classificação da Miastenia Gravis** do paciente.
   - O sistema também permite a visualização de **indicações médicas** e **efeitos adversos** relacionados à condição.

## Estrutura do Projeto

```bash
.
├── main.py          # Arquivo principal da aplicação
├── config.json      # Arquivo de configuração para armazenar a chave API (gerado automaticamente)
├── questions.json   # Arquivo com as perguntas da consulta
├── classes.json     # Arquivo contendo as classes MGFA e suas informações
├── responses.json   # Arquivo gerado com as respostas do usuário (salvo após a consulta)
└── README.md        # Instruções do projeto
```

## Estrutura dos Arquivos JSON

### `config.json`

Armazena a chave da API da OpenAI:

```json
{
  "api_key": "sua_chave_api"
}
```

### `questions.json`

Contém as perguntas do chatbot e as possíveis opções de resposta:

```json
{
  "questions": {
    "q1": {
      "question": "Qual o principal sintoma que o paciente apresenta?",
      "options": ["Fraqueza ocular", "Dificuldade de deglutição", "Problemas respiratórios"]
    },
    ...
  }
}
```

### `classes.json`

Contém as informações das classes da Miastenia Gravis:

```json
{
  "classeI": "Miastenia ocular pura, sem envolvimento generalizado",
  "classeII": "Forma leve generalizada",
  ...
}
```

## Contribuição

Se você quiser contribuir com melhorias para este projeto, siga os seguintes passos:

1. Faça um **fork** do projeto.
2. Crie uma nova **branch** para a funcionalidade ou correção que deseja implementar (`git checkout -b minha-nova-funcionalidade`).
3. Faça o **commit** das suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. **Push** para a branch criada (`git push origin minha-nova-funcionalidade`).
5. Abra um **Pull Request** no repositório original.


## Contato

Caso tenha dúvidas ou sugestões, entre em contato pelo e-mail: **cassioms764@gmail.com**.
