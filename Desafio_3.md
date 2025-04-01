# Desafio 3 - Teste de Banco de Dados

Este desafio tem como objetivo estruturar um banco de dados MySQL utilizando Docker, importar dados financeiros das operadoras de planos de saúde e realizar consultas analíticas.

## Requisitos

- Docker instalado na sua máquina.
- Arquivos CSV contendo os dados financeiros a serem importados.

## Configuração do Banco de Dados

Para configurar o banco de dados, utilize o seguinte **docker-compose.yml**:

```yaml
version: '3.8'

services:
  mysql:
    image: mysql:latest
    container_name: mysql-container
    environment:
      MYSQL_ROOT_PASSWORD: senha
      MYSQL_DATABASE: inovative
      MYSQL_USER: usuario
      MYSQL_PASSWORD: senha
    ports:
      - "3306:3306"
```

### Iniciando o Banco de Dados

Para rodar o MySQL no Docker, execute:

```bash
docker-compose up -d
```

Isso criará e executará um container MySQL.

## Criação da Tabela

Execute o seguinte script SQL para criar a tabela `dados_financeiros`:

```sql
DROP TABLE IF EXISTS dados_financeiros;

CREATE TABLE dados_financeiros (
    data DATE,
    reg_ans VARCHAR(10),
    cd_conta_contabil VARCHAR(20),
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2)
);

ALTER TABLE dados_financeiros
    ADD INDEX idx_saldo_inicial (vl_saldo_inicial),
    ADD INDEX idx_saldo_final (vl_saldo_final),
    ADD INDEX idx_conta_data (cd_conta_contabil, data);
```

## Importação dos Arquivos CSV

### 📂 **Passos Importantes**

1. **Crie uma pasta chamada `csv_files` na raiz do projeto**.
2. **Adicione os arquivos CSV dentro dessa pasta**.
3. **Transfira a pasta para o servidor MySQL no Docker**:

```bash
docker cp ./csv_files mysql-container:/var/lib/mysql-files
```

4. **Execute a seguinte query para importar os dados do primeiro trimestre de 2024:**

```sql
LOAD DATA INFILE '/var/lib/mysql-files/csv_files/1T2024.csv' INTO TABLE dados_financeiros
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS (
    @data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
```

## Consultas Analíticas

### 🔍 **Consulta das 10 operadoras com maiores despesas em assistência à saúde**

```sql
SELECT reg_ans,
       SUM(CASE
               WHEN data >= CURDATE() - INTERVAL 3 MONTH THEN vl_saldo_final
               ELSE 0
           END) AS despesas_ultimo_trimestre,
       SUM(CASE
               WHEN data >= CURDATE() - INTERVAL 1 YEAR THEN vl_saldo_final
               ELSE 0
           END) AS despesas_ultimo_ano
FROM dados_financeiros
WHERE descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
GROUP BY reg_ans
ORDER BY despesas_ultimo_trimestre DESC, despesas_ultimo_ano DESC
LIMIT 10;
```

## Considerações Finais

Este desafio tem como objetivo a manipulação de grandes volumes de dados financeiros e a extração de insights valiosos por meio de queries analíticas.

Caso encontre algum problema, verifique se os arquivos CSV estão corretamente formatados e se a conexão com o banco de dados está ativa.

[🔙 Voltar](README.md)

