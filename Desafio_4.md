# Desafio 4 - Teste de API
Este desafio consiste em desenvolver uma aplicação completa com uma API (backend) e um frontend. A API é responsável por fornecer dados de operadoras a partir de um arquivo CSV, enquanto o frontend permite que o usuário busque esses dados de forma interativa.

Estrutura do Projeto

O projeto está organizado em duas pastas principais dentro do diretório desafio_4:

 ```
 ├── desafio_4/
│   ├── api
│   ├── web
├──
 ```
## API

### Navegue até a pasta da API:

```bash
cd desafio_4/api
```
### Instale as dependências:
```bash
pip install -r requirements.txt
```
### Execute a API:

```bash
python app.py
```

A API estará disponível em http://localhost:5000.

### Testando a API
Vá no seu Postman, Insomnia ou qualquer outro software que faça requisições a APIs

**Faça uma requisição do tipo `get` para:**
```bash
http://localhost:5000/search?q=praça da bandeira
```
**Você receberá uma resposta neste formato:**
```json
[
    {
        "Bairro": "PRAÇA DA BANDEIRA",
        "CEP": "36660000",
        "CNPJ": "19541931000125",
        "Cargo_Representante": "SÓCIO ADMINISTRADOR",
        "Cidade": "Além Paraíba",
        "Complemento": "",
        "DDD": "32",
        "Data_Registro_ANS": "2015-05-19",
        "Endereco_eletronico": "contabilidade@cbnassessoria.com.br",
        "Fax": "",
        "Logradouro": "RUA CAPITÃO MEDEIROS DE REZENDE",
        "Modalidade": "Administradora de Benefícios",
        "Nome_Fantasia": "",
        "Numero": "274",
        "Razao_Social": "18 DE JULHO ADMINISTRADORA DE BENEFÍCIOS LTDA",
        "Regiao_de_Comercializacao": "6",
        "Registro_ANS": "419761",
        "Representante": "LUIZ HENRIQUE MARENDINO GONÇALVES",
        "Telefone": "34624649",
        "UF": "MG"
    }
]
```
## Frontend
Até então só utilizamos o python, então caso você não tenha node no seu computador baixe-o [clicando aqui](https://nodejs.org/pt/download) e siga os passos de instalação<br>
Para garantir que ele foi instalado rode
```bash
node -v
```
### Navegue até a pasta do frontend:

```bash
cd desafio_4/web
```
### Instale as dependências:

```bash
npm install
```

Certifique-se de que o arquivo package.json contenha as dependências necessárias, como axios.

### Execute o frontend:
```bash
vue serve
```
Caso não tenha a CLI do Vue.js você pode instalá-la através do comando
```bash
npm i -g @vue/cli
```
<hr>

[🔙 Voltar](README.md)