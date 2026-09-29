# Através deste script, os dados do arquivo CSV serão carregados para o banco de dados PostgreSQL.
import os
import pandas as pd
from sqlalchemy import create_engine, text

# Função para carregar os dados do CSV para o banco de dados PostgreSQL
def carregar_dados_raw():
    path_raw_csv = os.path.join("data", "raw", "SuperMarket Analysis.csv")
    
    if os.path.exists(path_raw_csv):
        df_raw = pd.read_csv(path_raw_csv)
        
        df_raw.columns = [
            'invoice_id', 'branch', 'city', 'customer_type', 'gender',
            'product_line', 'unit_price', 'quantity', 'tax_5_percent',
            'total', 'date_sale', 'time_sale', 'payment', 'cogs',
            'gross_margin_percentage', 'gross_income', 'rating'
        ]
        
        # Conectando ao PostgreSQL e criando o schema 'raw' se não existir
        engine_raw = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/supermarket_vendas")
        
        with engine_raw.begin() as conn:
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw;"))
            
        df_raw.to_sql(name='raw_vendas', con=engine_raw, schema='raw', if_exists='append', index=False)
        print(f"✅ Carga concluída: {len(df_raw)} registros salvos em raw.raw_vendas.")
    else:
        print("Arquivo CSV não encontrado!")
