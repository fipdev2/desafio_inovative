# Crie uma pasta chamada csv_files na raiz do projeto
# Bote seus arquivos .csv nesta pasta
# Transfira essa pasta para o servidor MySQL utilizando o Docker com o seguinte comando: docker cp ./csv_files mysql-container:/var/lib/mysql-files

# Importar 1º trimestre de 2024
LOAD DATA INFILE '/var/lib/mysql-files/csv_files/1T2024.csv' INTO
TABLE dados_financeiros CHARACTER SET utf8mb4 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    vl_saldo_inicial =
REPLACE (@vl_saldo_inicial, ',', '.'),
    vl_saldo_final =
REPLACE (@vl_saldo_final, ',', '.');
