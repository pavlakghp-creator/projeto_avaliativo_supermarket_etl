""" Para executar o pipeline completo, basta rodar este script.
 Ele irá chamar as funções de ingestão, ETL e análise estatística em sequência."""

from leitura_dados import carregar_dados_raw
from etl_vendas import executar_etl
from estatistica import gerar_estatisticas

def main():
    print(" INICIANDO O PIPELINE COMPLETO DE DADOS...")
    
    print("\n--- ETAPA 1: Ingestão de Dados Raw ---")
    carregar_dados_raw()

    print("\n--- ETAPA 2: Tratamento e Carga (ETL) ---")
    executar_etl()

    print("\n--- ETAPA 3: Análise Estatística e Gráficos ---")
    gerar_estatisticas()

    print(f"\n PIPELINE EXECUTADO COM SUCESSO!")

if __name__ == "__main__":
    main()