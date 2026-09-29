# 🛒 Supermarket Sales - End-to-End ETL & Analytics Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14%2B-336791?style=for-the-badge&logo=postgresql)
![Pandas](https://img.shields.io/badge/Pandas-ETL-150458?style=for-the-badge&logo=pandas)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)

Este projeto consiste em um pipeline completo de **Engenharia e Análise de Dados (ETL)** desenvolvido em Python e PostgreSQL. O sistema realiza desde a ingestão dos dados brutos (*raw*) até o tratamento, modelagem relacional, carga automatizada na camada processada (*processed*), geração de relatórios de métricas de negócio e salvamento de visualizações estatísticas.

---

## 📌 1. Objetivo do Projeto

O objetivo principal é extrair dados brutos de vendas de uma rede de supermercados, realizar processos de validação e limpeza de dados (remoção de duplicatas, tratamento de nulos, tipagem estrita de colunas e criação de atributos derivados) e disponibilizá-los em um banco de dados relacional (PostgreSQL) para responder a 8 perguntas estratégicas do negócio:

1. Filial com maior faturamento total.
2. Filial com maior quantidade de itens vendidos.
3. Linha de produto com maior faturamento.
4. Linha de produto com melhor avaliação média (satisfação dos clientes).
5. Forma de pagamento mais utilizada.
6. Ticket médio das vendas.
7. Valor da maior venda individual registrada.
8. Dia da semana com maior volume de vendas.

---

## 🏗️ 2. Arquitetura e Fluxo de Dados

O fluxo de dados segue o padrão de medalhão/camadas clássico de data warehousing:

[ CSV Bruto ] ──► (src/leitura_dados.py) ──► [ PostgreSQL: Schema raw ]
│
▼
[ CSV Processado ] ◄── (src/etl_vendas.py) ◄───────┘
│
├──► [ PostgreSQL: Schema processed ]
│
└──► (src/estatistica.py) ──► [ Métricas no Terminal + Gráficos (PNG) ]

1. **Ingestão (Raw Layer):** Leitura do arquivo fonte em `data/raw/` e carga direta na tabela `raw.raw_vendas`.
2. **Transformação (Processed Layer):**
   - Normalização de nomes de colunas.
   - Remoção de vendas duplicadas (`id_venda`).
   - Tratamento de nulos em chaves essenciais.
   - Extração do dia da semana (`dia_semana`).
   - Casting estrito de tipos (`float` arredondado para 2 casas, `int` para quantidade, `date` e `time` nativos).
3. **Carga (Load):** Exportação para `data/processed/vendas_tratadas.csv` e gravação persistente em `processed.vendas_tratadas`.
4. **Analytics & Dataviz:** Agregações SQL/Pandas e exportação automática dos gráficos estatísticos para `resultados/estatisticas e graficos/`.

---

## 📂 3. Estrutura de Pastas do Repositório

```text
projeto_avaliativo_supermarket_etl/
│
├── .env                       # Variáveis de ambiente (senhas/credenciais)
├── .gitignore                 # Arquivos ignorados pelo Git (ex: .venv, .env)
├── README.md                  # Documentação principal do projeto
├── requirements.txt           # Lista de dependências Python
│
├── data/
│   ├── raw/                   # Dados brutos de entrada (SuperMarket Analysis.csv)
│   └── processed/             # Dados limpos exportados em CSV (vendas_tratadas.csv)
│
├── resultados/
│   └── estatisticas e graficos/  # Gráficos e relatórios gerados (PNG/TXT)
│
├── sql/                       # Scripts DDL e DML SQL
│   ├── 01_criar_banco.sql     # Script de criação da base de dados
│   ├── 02_criar_tabelas.sql   # DDL dos schemas raw e processed
│   └── 03_consultas.sql       # Consultas analíticas auxiliares
│   └── run_etl.py             # Orquestrador central do pipeline│
│
└── src/                       # Módulos Python com a lógica do ETL
    ├── leitura_dados.py       # Módulo 1: Leitura do CSV e ingestão no raw
    ├── etl_vendas.py          # Módulo 2: Tratamento e gravação no processed
    └── estatistica.py         # Módulo 3: Métricas de negócio e geração de gráficos
```

## 4. Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:

* **Python 3.10** ou superior.
* **PostgreSQL 14** ou superior (rodando localmente ou em servidor remoto).
* **Git** para clonar o repositório.
* **VS Code** ou IDE de sua preferência.

## 🚀 5. Instalação e Configuração Passo a Passo

### 5.1. Clonando o Repositório

git clone [https://github.com/pavlakghp-creator/projeto_avaliativo_supermarket_etl.git](https://github.com/seu-usuario/projeto_avaliativo_supermarket_etl.git)
cd projeto_avaliativo_supermarket_etl

### 5.2. Configuração das Variáveis de Ambiente (`.env`)

Crie um arquivo chamado `.env` na raiz do projeto (no mesmo nível do `run_etl.py`) e insira as credenciais do seu PostgreSQL:

DATABASE_URL=postgresql+psycopg2://usuário:sua_senha@seuhost:5432/supermarket_vendas

### 5.5. Preparação do Banco de Dados PostgreSQL

Antes de executar o pipeline, execute os scripts da pasta `sql/` no seu SGBD (DBeaver, pgAdmin ou `psql`):

1. Execute `sql/01_criar_banco.sql` para criar a base `supermarket_vendas`.
2. Execute `sql/02_criar_tabelas.sql` para estruturar os schemas `raw` e `processed` com suas respectivas restrições (`NOT NULL`, `CHECK`).



## 🏃 6. Como Executar o Pipeline Completo

Para rodar todo o pipeline de ponta a ponta (Ingestão ➔ Tratamento ➔ Gravação ➔ Análises Estatísticas), basta executar o orquestrador central:

python run_etl.py

Exemplo de Saída Esperada no Terminal:


🚀 INICIANDO O PIPELINE COMPLETO DE DADOS...

--- ETAPA 1: Ingestão de Dados Raw ---
✅ Carga concluída: 1000 registros salvos em raw.raw_vendas.

--- ETAPA 2: Tratamento e Carga (ETL) ---
✅ ETL concluído e dados gravados na camada processed!

--- ETAPA 3: Análise Estatística e Gráficos ---

###### 🎯 RESPOSTAS ÀS PERGUNTAS DE NEGÓCIO

1. Filial com Maior Faturamento: Giza (R$ 110,568.86)
2. Filial com Maior Qtd de Vendas: Alex (1859 itens)
3. Linha de Produto com Maior Faturamento: Food and beverages (R$ 56,144.96)
4. Linha com Melhor Avaliação Média: Food and beverages (7.11)
5. Forma de Pagamento Mais Utilizada: Ewallet (345 transações)
6. Valor Médio das Vendas: R$ 322.97
7. Maior Venda Registrada: R$ 1,042.65
8. Dia da Semana com Mais Vendas: Sábado (164 transações)

✅ PIPELINE EXECUTADO COM SUCESSO!


## 📊 7. Visualização dos Resultados

Após a execução:

* Os arquivos tratados estarão disponíveis em `data/processed/vendas_tratadas.csv`.
* As tabelas relacionais estarão populadas nos schemas `raw` e `processed` do seu banco PostgreSQL.
* Os gráficos de desempenho (como `faturamento_por_filial.png`) estarão disponíveis dentro do diretório `resultados/estatisticas e graficos/`.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Manipulação de Dados:** Pandas
* **Conexão com Banco:** SQLAlchemy, Psycopg2-binary
* **Visualização de Dados:** Matplotlib, Seaborn
* **Banco de Dados:** PostgreSQL
* **Variáveis de Ambiente:** Python-dotenv
