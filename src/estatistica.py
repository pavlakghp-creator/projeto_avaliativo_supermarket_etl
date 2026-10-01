# Importando bibliotecas necessárias
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para gerar estatísticas e insights de negócio
def gerar_estatisticas():
    path_processed = os.path.join("data", "processed", "vendas_tratadas.csv")
    df = pd.read_csv(path_processed)

    print("=" * 60)
    print("🎯 RESPOSTAS ÀS PERGUNTAS DE NEGÓCIO")
    print("=" * 60)

    # Fazendo a soma do faturamento por filial e ordenando em ordem decrescente
    fat_filial = df.groupby('filial')['valor_total'].sum().sort_values(ascending=False)
    print(f"1. Filial com Maior Faturamento: {fat_filial.index[0]} (R$ {fat_filial.iloc[0]:,.2f})")

    # Fazendo a soma da quantidade de vendas por filial e ordenando em ordem decrescente    
    qtd_filial = df.groupby('filial')['quantidade'].sum().sort_values(ascending=False)
    print(f"2. Filial com Maior Qtd de Vendas: {qtd_filial.index[0]} ({qtd_filial.iloc[0]} itens)")

    # Fazendo a soma do faturamento por linha de produto e ordenando em ordem decrescente
    fat_prod = df.groupby('linha_produto')['valor_total'].sum().sort_values(ascending=False)
    print(f"3. Linha de Produto com Maior Faturamento: {fat_prod.index[0]} (R$ {fat_prod.iloc[0]:,.2f})")

    # Calculando a média de avaliação por linha de produto e ordenando em ordem decrescente
    aval_prod = df.groupby('linha_produto')['avaliacao'].mean().sort_values(ascending=False)
    print(f"4. Linha com Melhor Avaliação Média: {aval_prod.index[0]} ({aval_prod.iloc[0]:.2f})")

    # Calculando a frequência de cada forma de pagamento e identificando a mais utilizada
    pag_freq = df['forma_pagamento'].value_counts()
    print(f"5. Forma de Pagamento Mais Utilizada: {pag_freq.index[0]} ({pag_freq.iloc[0]} transações)")

    # Calculando o valor médio das vendas (ticket médio) e a maior venda registrada
    print(f"6. Valor Médio das Vendas: R$ {df['valor_total'].mean():,.2f}")
    print(f"7. Maior Venda Registrada: R$ {df['valor_total'].max():,.2f}")

    # Calculando o dia da semana com mais vendas
    vendas_dia = df['dia_semana'].value_counts()
    print(f"8. Dia da Semana com Mais Vendas: {vendas_dia.index[0]} ({vendas_dia.iloc[0]} transações)")

    print("=" * 60)
    print("📊 RESPOSTAS DE NEGÓCIO")
    print("=" * 60)

    # Verificando quais categorias de produtos vendem mais
    categoria_vendas = df.groupby('linha_produto')['quantidade'].sum().sort_values(ascending=False)
    print(f"9. Categoria de Produto com Mais Vendas: {categoria_vendas.index[0]} ({categoria_vendas.iloc[0]} itens vendidos)")

    # comparação de desempenho entre filiais
    desempenho_filiais = df.groupby('filial')['valor_total'].sum().sort_values(ascending=False)
    print(f"10. Comparação de Desempenho entre Filiais:")
    for filial, valor in desempenho_filiais.items():
        print(f"    {filial}: {valor}")

    # Períodos com maior quantidade de vendas top 5
    vendas_periodo = df.groupby('data_venda')['quantidade'].sum().sort_values(ascending=False)
    print(f"11. 5 Períodos com Maior Qtd de Vendas:")
    for data, qtd in vendas_periodo.head(5).items():
        print(f"    {data}: {qtd} itens vendidos")

    # Avaliando satisfação dos clientes por genero
    satisfacao_genero = df.groupby('genero')['avaliacao'].mean().sort_values(ascending=False)
    print(f"12. Satisfação dos Clientes por Gênero:")
    for genero, avaliacao in satisfacao_genero.items():
        print(f"    {genero}: {avaliacao:.2f} / 10")
    print("\n")

    # Gerar e Salvar Gráficos
    path_img = os.path.join("resultados", "estatisticas e graficos")
    os.makedirs(path_img, exist_ok=True)

    # Gráfico 1: Faturamento por Filial
    plt.figure(figsize=(7, 4))
    sns.barplot(x=fat_filial.index, y=fat_filial.values, palette="mako")
    plt.title("Faturamento por Filial")
    plt.savefig(os.path.join(path_img, "faturamento_por_filial.png"))
    plt.close()

    # Gráfico 2: Quantidade de Vendas por Filial
    plt.figure(figsize=(7, 4))
    sns.barplot(x=qtd_filial.index, y=qtd_filial.values, palette="mako")
    plt.title("Quantidade de Vendas por Filial")
    plt.savefig(os.path.join(path_img, "quantidade_vendas_por_filial.png"))
    plt.close()

    # Gráfico 3: Quantidade de Vendas por Período
    plt.figure(figsize=(7, 4))
    sns.lineplot(x=vendas_periodo.index, y=vendas_periodo.values, marker='o')
    plt.title("Quantidade de Vendas por Período")
    plt.xlabel("Data")
    plt.ylabel("Quantidade de Vendas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(path_img, "quantidade_vendas_por_periodo.png"))
    plt.close()

    # Salvar resumo textual das respostas em resultados/
    path_relatorio = os.path.join("resultados", "relatorio_negocio.txt")
    os.makedirs(os.path.dirname(path_relatorio), exist_ok=True)

    resumo_texto = f"""============================================================
    🎯 RESUMO EXECUTIVO DE NEGÓCIO - SUPERMARKET SALES
    ============================================================
    1. Filial com Maior Faturamento: {fat_filial.index[0]} (R$ {fat_filial.iloc[0]:,.2f})
    2. Filial com Maior Qtd de Vendas: {qtd_filial.index[0]} ({qtd_filial.iloc[0]} itens)
    3. Linha de Produto com Maior Faturamento: {fat_prod.index[0]} (R$ {fat_prod.iloc[0]:,.2f})
    4. Linha com Melhor Avaliação Média: {aval_prod.index[0]} ({aval_prod.iloc[0]:.2f})
    5. Forma de Pagamento Mais Utilizada: {pag_freq.index[0]} ({pag_freq.iloc[0]} transações)
    6. Valor Médio das Vendas (Ticket Médio): R$ {df['valor_total'].mean():,.2f}
    7. Maior Venda Registrada: R$ {df['valor_total'].max():,.2f}
    8. Dia da Semana com Mais Vendas: {vendas_dia.index[0]} ({vendas_dia.iloc[0]} transações)
    =============================================================
    Levantamento de Insights Adicionais:
    9. Categoria de Produto com Mais Vendas: {categoria_vendas.index[0]} ({categoria_vendas.iloc[0]} itens vendidos)
    10. Comparação de Desempenho entre Filiais: {', '.join([f'{filial}: R$ {valor:,.2f}' for filial, valor in desempenho_filiais.items()])}
    11. 5 Períodos com Maior Qtd de Vendas: {', '.join([f'{data}: {qtd} itens vendidos' for data, qtd in vendas_periodo.head(5).items()])}
    12. Satisfação dos Clientes por Gênero: {', '.join([f'{genero}: {avaliacao:.2f} / 10' for genero, avaliacao in satisfacao_genero.items()])}
    =============================================================
    """

    with open(path_relatorio, "w", encoding="utf-8") as f:
        f.write(resumo_texto)

    print(f"📄 Relatório salvo com sucesso em: {path_relatorio}")
