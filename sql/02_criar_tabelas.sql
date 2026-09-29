-- execute este script manualmente para criar as tabelas no banco de dados PostgreSQL

-- Criando Schemas raw e processed
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS processed;

-- CAMADA RAW (Cópia fiel do CSV original sem alterações)
CREATE TABLE If NOT EXISTS raw_vendas (
    invoice_id VARCHAR(50),
    branch VARCHAR(10),
    city VARCHAR(100),
    customer_type VARCHAR(50),
    gender VARCHAR(20),
    product_line VARCHAR(150),
    unit_price NUMERIC(10,2),
    quantity INTEGER,
    tax_5_percent NUMERIC(10,2),
    total NUMERIC(12,2),
    date_sale VARCHAR(20),
    time_sale VARCHAR(20),
    payment VARCHAR(50),
    cogs NUMERIC(12,2),
    gross_margin_percentage NUMERIC(10,2),
    gross_income NUMERIC(12,2),
    rating NUMERIC(4,2)
);

-- CAMADA TRATADA (Conforme Dicionário de Dados)
CREATE TABLE if NOT EXISTS vendas_tratadas (
    id_venda VARCHAR(50) PRIMARY KEY NOT NULL,
    filial VARCHAR(10) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(50),
    genero VARCHAR(20),
    linha_produto VARCHAR(150) NOT NULL,
    preco_unitario NUMERIC(10,2) NOT NULL CHECK (preco_unitario >= 0),
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    imposto NUMERIC(10,2) NOT NULL CHECK (imposto >= 0),
    valor_total NUMERIC(12,2) NOT NULL CHECK (valor_total >= 0),
    data_venda DATE NOT NULL,
    hora_venda TIME NOT NULL,
    forma_pagamento VARCHAR(50) NOT NULL,
    custo_mercadoria NUMERIC(12,2) NOT NULL CHECK (custo_mercadoria >= 0),
    margem_percentual NUMERIC(10,2),
    receita_bruta NUMERIC(12,2) NOT NULL CHECK (receita_bruta >= 0),
    avaliacao NUMERIC(4,2) CHECK (avaliacao BETWEEN 0 AND 10)
);