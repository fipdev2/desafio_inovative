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
