-- Consultas SQL para validação e exportação de dados da Camada Raw

-- Total de registros carregados na Raw
SELECT COUNT(*) AS total_registros_raw FROM raw_vendas;

-- Faturamento total por filial (Consulta preliminar)
SELECT 
    branch AS filial, 
    SUM(total) AS faturamento_total
FROM raw_vendas
GROUP BY branch
ORDER BY faturamento_total DESC;

-- Média de vendas por filial (Consulta preliminar)
SELECT 
    branch AS filial, 
    AVG(total) AS media_vendas
FROM raw_vendas
GROUP BY branch
ORDER BY media_vendas DESC;

-- Exportação dos dados brutos para verificação
-- Nota: Pode ser executado via cliente psql ou script Python de extração
SELECT * FROM raw_vendas;