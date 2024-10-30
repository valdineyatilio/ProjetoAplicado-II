import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV com a codificação 'latin1'
url = "https://raw.githubusercontent.com/valdineyatilio/Projeto-Aplicado-I/main/Aula2/Dados%20YouTube.csv.csv"
dados_youtube = pd.read_csv(url, encoding='latin1')

# Contagem de categorias de conteúdo
category_counts = dados_youtube['category'].value_counts()

# Gráfico de barras horizontal para visualizar as categorias
plt.figure(figsize=(12, 8))
sns.barplot(y=category_counts.index, x=category_counts.values, palette="viridis")
plt.title("Distribuição de Categorias de Conteúdo dos Canais")
plt.xlabel("Número de Canais")
plt.ylabel("Categoria")
plt.show()