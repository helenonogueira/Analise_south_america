import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar Dados
df_mortes = pd.read_csv('C:\\Users\\Heleno\\Documents\\Projetos Portifólio\\saude_publica_analysis\\dados\\death_causes_mean.csv')
df_desenvolvimento = pd.read_csv('C:\\Users\\Heleno\\Documents\\Projetos Portifólio\\saude_publica_analysis\\dados\\indicator_analysis.csv')

# Colunas de interesse
colunas_mortes = [
    'Country', 'Meningitis', 'Deficiencia Nutricional', 'Malaria', 
    'Violencia Interpessoal', 'Drogas', 'Tuberculose', 
    'Cardiovascular', 'Diarreia', 'Diabetes'
]
colunas_desenvolvimento = [
    'Country', 'GDP', 'GNI', 'Densidade Populacional', 
    'Ensino Primario', 'Matricula Escolar'
]

# Filtragem das colunas
df_mortes = df_mortes[colunas_mortes]
df_desenvolvimento = df_desenvolvimento[colunas_desenvolvimento]

# Renomear as colunas para facilitar o merge
df_mortes.rename(columns={'Country': 'Country'}, inplace=True)
df_desenvolvimento.rename(columns={'Country': 'Country'}, inplace=True)

# Limpeza dos dados (remoção de valores nulos e transformação de tipos)
df_mortes = df_mortes.dropna()
df_desenvolvimento = df_desenvolvimento.dropna()

# Converter colunas para valores numéricos (se necessário)
for col in colunas_mortes[1:]:  # Colunas de fatalidades
    df_mortes[col] = pd.to_numeric(df_mortes[col], errors='coerce')

for col in colunas_desenvolvimento[1:]:  # Colunas de indicadores
    df_desenvolvimento[col] = pd.to_numeric(df_desenvolvimento[col], errors='coerce')

# Mesclar os dois dataframes com base na coluna 'Country'
df = pd.merge(df_mortes, df_desenvolvimento, on='Country')

# Criar uma nova coluna com o somatório das mortes por causas específicas
df['Total Fatalities'] = df[
    ['Meningitis', 'Deficiencia Nutricional', 'Malaria', 
    'Violencia Interpessoal', 'Drogas', 'Tuberculose', 
    'Cardiovascular', 'Diarreia', 'Diabetes'
    ]
].sum(axis=1)

# Análise 1: Correlação entre Total de Fatalidades e GNI per capita
correlacao = df['Total Fatalities'].corr(df['GNI'])
print(f'Correlação entre Total de Fatalidades e GNI per capita: {correlacao}')

plt.figure(figsize=(10, 6))
sns.boxplot(x='GNI', y='Total Fatalities', data=df)
plt.title('Correlação entre Renda per capita e Total de Fatalidades')
plt.xlabel('GNI per capita (US$)')
plt.ylabel('Total de Fatalidades')
plt.savefig('outputs/graficos/gni_total_fatalidades.png')
plt.show()

# Análise 2: Comparação das Taxas de Desenvolvimento por País
indicadores_pais = df.groupby('Country')[
    ['Densidade Populacional', 
     'Ensino Primario', 
     'Matricula Escolar'
    ]].mean()

indicadores_pais.plot(kind='bar', stacked=True, figsize=(12, 7))
plt.title('Indicadores de Desenvolvimento por País')
plt.xlabel('País')
plt.ylabel('Indicadores de Desenvolvimento (%)')
plt.legend(title='Indicadores')
plt.savefig('outputs/graficos/indicadores_desenvolvimento.png')
plt.show()


# Análise 3: Matriz de correlação das variáveis numéricas (heatmap)
correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',
 fmt=".2f")
plt.title('Matriz de Correlação das Variáveis Numéricas')
plt.savefig('outputs/graficos/heatmap.png')
plt.show()


# Análise 4: Gráfico de pizza correlacionando porcentagem de cada tipo de morte no País
for index, row in df_mortes.iterrows():
    
    country_name = row['Country']

    causes_of_death = row[1:]

# Criar o gráfico de pizza
    plt.figure(figsize=(8, 8))
    plt.pie(causes_of_death.values, autopct="%1.1f%%", startangle=140)
    plt.legend(causes_of_death.index, loc='best', bbox_to_anchor=(1, 0.5), handletextpad=1.2)
    plt.title(f"Distribuição de Causas de Morte: {country_name}")
    plt.savefig(f"outputs/graficos/grafico_{country_name}.png")
    plt.show()




# Exportação do relatório final
df.to_csv('outputs/relatorio_analise.csv', index=False)


print("Relatório exportado para outputs/relatorio_analise.csv")
