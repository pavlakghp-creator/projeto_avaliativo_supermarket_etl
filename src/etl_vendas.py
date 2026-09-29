# Importando bibliotecas
import os
import pandas as pd
from sqlalchemy import create_engine, text

def executar_etl():
    engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/supermarket_vendas")
    
    # Leitura do Banco (Camada Raw)
    df_raw = pd.read_sql("SELECT * FROM raw.raw_vendas;", engine)
    
    # Mapeamento de Colunas
    colunas_map = {
        'invoice_id': 'id_venda', 'branch': 'filial', 'city': 'cidade',
        'customer_type': 'tipo_cliente', 'gender': 'genero', 'product_line': 'linha_produto',
        'unit_price': 'preco_unitario', 'quantity': 'quantidade', 'tax_5_percent': 'imposto',
        'total': 'valor_total', 'date_sale': 'data_venda', 'time_sale': 'hora_venda',
        'payment': 'forma_pagamento', 'cogs': 'custo_mercadoria',
        'gross_margin_percentage': 'margem_percentual', 'gross_income': 'receita_bruta',
        'rating': 'avaliacao'
    }
    # Renomeando Colunas
    df_tratado = df_raw.rename(columns=colunas_map)
    
    # Limpeza de Dados
    # Remover Colunas Desnecessárias (Valores duplicados e valores nulos)
    df_tratado = df_tratado.drop_duplicates(subset=['id_venda'])
    df_tratado = df_tratado.dropna(subset=['id_venda', 'filial', 'linha_produto', 'valor_total'])
   
    # Ajuste de conversões e Tipagem
    df_tratado['data_venda'] = pd.to_datetime(df_tratado['data_venda']).dt.date
    df_tratado['hora_venda'] = pd.to_datetime(df_tratado['hora_venda'], format='mixed').dt.time

    # Criando coluna Derivada
    df_tratado['dia_semana'] = pd.to_datetime(df_tratado['data_venda']).dt.day_name()

    # Transformando os dias da semana para português
    dias_semana_pt = {
        'Monday': 'Segunda-feira', 'Tuesday': 'Terça-feira', 'Wednesday': 'Quarta-feira',
        'Thursday': 'Quinta-feira', 'Friday': 'Sexta-feira', 'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }    
    df_tratado['dia_semana'] = df_tratado['dia_semana'].map(dias_semana_pt)

    # Ajuste de Tipagem para Colunas Numéricas
    cols_float = ['preco_unitario', 'imposto', 'valor_total', 'custo_mercadoria', 
                  'margem_percentual', 'receita_bruta', 'avaliacao']
    for col in cols_float:
        df_tratado[col] = df_tratado[col].astype(float).round(2)

    # Ajuste de Tipagem para Colunas Inteiras    
    df_tratado['quantidade'] = df_tratado['quantidade'].astype(int)
    
    # Salvando em CSV
    path_processed_csv = os.path.join("data", "processed", "vendas_tratadas.csv")
    os.makedirs(os.path.dirname(path_processed_csv), exist_ok=True)
    df_tratado.to_csv(path_processed_csv, index=False)
    
    # Salvar na Tabela Processed no Postgres
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS processed;"))
        
    df_tratado.to_sql(name='vendas_tratadas', con=engine, schema='processed', if_exists='append', index=False)
    print("✅ ETL concluído e dados gravados na camada processed!")

