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