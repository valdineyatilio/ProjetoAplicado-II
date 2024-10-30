import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV com a codificação 'latin1'
url = "https://raw.githubusercontent.com/valdineyatilio/Projeto-Aplicado-I/main/Aula2/Dados%20YouTube.csv.csv"
youtube_data = pd.read_csv(url, encoding='latin1')

# Selecionar as colunas 'Youtuber' e 'subscribers_for_last_30_days', removendo valores nulos
recent_growth = youtube_data[['Youtuber', 'subscribers_for_last_30_days']].dropna()

# Ordenar por crescimento de inscritos e selecionar os 10 principais
top_growth = recent_growth.sort_values(by='subscribers_for_last_30_days', ascending=False).head(10)

# Gráfico de barras
plt.figure(figsize=(12, 6))
sns.barplot(x=top_growth['subscribers_for_last_30_days'], y=top_growth['Youtuber'], palette="magma")
plt.title("Canais com Maior Crescimento de Inscritos nos Últimos 30 Dias")
plt.xlabel("Inscritos nos Últimos 30 Dias")
plt.ylabel("Youtuber")
plt.show()