# Biblioteca
#Comparar video views entre diferentes categorias

import pandas as pd
from scipy.stats import f_oneway

# Carregar a base de dados
url = "https://github.com/valdineyatilio/ProjetoAplicado-II/raw/refs/heads/main/Aula-02/BaseDeDadosYouTube.csv"
dados_youtube = pd.read_csv(url, encoding='latin1')


# Preparar os dados
categorias = dados_youtube['category'].unique()
grupos = [dados_youtube[dados_youtube['category'] == categoria]['video views'] for categoria in categorias]

# Filtrar grupos não vazios
grupos_nao_vazios = [grupo for grupo in grupos if len(grupo) > 0]


# Verificar se há pelo menos dois grupos para realizar a ANOVA
if len(grupos_nao_vazios) > 1:
    # Realizar ANOVA
    f_stat, p_val = f_oneway(*grupos_nao_vazios)
    print(f"Estatística F: {f_stat}, Valor p: {p_val}")
else:
    print("Não há grupos suficientes com dados para realizar a ANOVA.")
    

