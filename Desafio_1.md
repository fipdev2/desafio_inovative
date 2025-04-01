# Desafio 1 - Teste de Web Scrapping

Este projeto tem como objetivo baixar anexos em formato PDF de uma página do site da ANS e compactá-los em um arquivo ZIP.

## Requisitos

Antes de executar o script, certifique-se de ter o Python 3 instalado em sua máquina.

## Configuração do Ambiente Virtual

Para garantir um ambiente isolado, crie um ambiente virtual e instale as dependências necessárias:

```bash
python -m venv .venv
pip install -r requirements.txt
```

## Como Executar o Script

1. Certifique-se de que o ambiente virtual está ativado.
2. Execute o seguinte comando:

```bash
python desafio_1/index.py
```

O script irá:
- Acessar a página da ANS.
- Extrair os links dos anexos I e II.
- Fazer o download dos PDFs.
- Compactar os arquivos baixados em um arquivo ZIP chamado `anexos.zip`.

## Resultado

Após a execução bem-sucedida, o arquivo `anexos.zip` conterá os PDFs baixados e estará localizado no diretório do projeto.

Caso tenha alguma dúvida ou encontre problemas, verifique sua conexão com a internet e tente novamente.

