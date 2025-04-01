# Desafio 2 - Extração e Processamento de Dados do PDF

Este projeto tem como objetivo extrair tabelas de um arquivo PDF específico, processá-las e gerar um arquivo CSV compactado em um ZIP.

## Requisitos

Antes de executar o script, certifique-se de ter o Python 3 instalado em sua máquina.

## Configuração do Ambiente Virtual

Para garantir um ambiente isolado, crie um ambiente virtual e instale as dependências necessárias:

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

## Como Executar o Script

1. Certifique-se de que os PDFs já foram baixados e estão dentro da pasta `anexos` (executando o Desafio 1 primeiro).
2. Ative o ambiente virtual.
3. Execute o script:

```bash
python desafio_2.py
```

O script irá:
- Procurar um arquivo PDF na pasta `anexos` cujo nome contenha `Anexo_I_`.
- Extrair tabelas da página que contém o título "Rol de Procedimentos e Eventos em Saúde".
- Substituir abreviações "OD" e "AMB" por suas descrições completas.
- Gerar um arquivo CSV chamado `Rol_Procedimentos.csv`.
- Compactar o CSV em um arquivo ZIP chamado `Teste_Filipe.zip`.

## Resultado

Após a execução, o arquivo `Teste_Filipe.zip` estará disponível no diretório do projeto contendo o CSV gerado a partir do PDF.

Se encontrar algum problema, certifique-se de que os PDFs estão corretamente baixados na pasta `anexos` e que o ambiente virtual está ativado com todas as dependências instaladas.

