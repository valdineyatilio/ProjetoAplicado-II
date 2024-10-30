import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV com a codificação 'latin1'
url = "https://raw.githubusercontent.com/valdineyatilio/Projeto-Aplicado-I/main/Aula2/Dados%20YouTube.csv.csv"
dados_youtube = pd.read_csv(url, encoding='latin1')

# Contagem de canais por país
country_counts = dados_youtube['Country'].value_counts()

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x=country_counts.values, y=country_counts.index, palette="viridis")
plt.title("Número de Canais Populares por País")
plt.xlabel("Número de Canais")
plt.ylabel("País")
plt.show()