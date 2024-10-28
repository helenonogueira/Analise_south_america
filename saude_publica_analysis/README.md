# Análise de Saúde Pública e Desenvolvimento Socioeconômico

Este projeto analisa a relação entre indicadores de saúde pública e desenvolvimento socioeconômico de diferentes países.

## Dados

Os dados utilizados neste projeto são:

* `death_causes_mean.csv`: Dados sobre média da mortalidade por diferentes causas em países da américa latina.
* `indicator_analysis.csv`: Indicadores de desenvolvimento socioeconômico.

## Código

O código `analise_socioeconomica.py` realiza as seguintes etapas:

1. Carrega os dados dos arquivos CSV.
2. Seleciona as colunas relevantes para a análise.
3. Limpa os dados, removendo valores ausentes e convertendo tipos de dados.
4. Mescla os dois DataFrames com base no nome do país.
5. Realiza análises e gera visualizações:
   * Correlação entre total de fatalidades e renda per capita.
   * Comparação de indicadores de desenvolvimento por país.
   * Distribuição geográfica das fatalidades.
6. Exporta o relatório final em formato CSV.

## Resultados

Os resultados da análise são salvos na pasta `outputs`:

* Gráficos: `outputs/graficos/`
* Relatório final: `outputs/relatorio_analise.csv`

## Executando o Código

1. Certifique-se de ter as bibliotecas necessárias instaladas (`pandas`, `matplotlib`, `seaborn`, `geopandas`).
2. Coloque os arquivos de dados na pasta `dados/`.
3. Execute o código `analise_socioeconomica.py`.


## Clone do Repositório : 
https://github.com/helenonogueira/Analise_south_america.git
