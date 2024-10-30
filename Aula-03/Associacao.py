# Bibliotecas
#Encontra regras de associação entre Country e high_earnings
#pip install mlxtend
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Carregar a base de dados
url = "https://github.com/valdineyatilio/ProjetoAplicado-II/raw/refs/heads/main/Aula-02/BaseDeDadosYouTube.csv"
dados_youtube = pd.read_csv(url, encoding='latin1')

# Preparar os dados para associação
dados_youtube['high_earnings'] = dados_youtube['highest_yearly_earnings'] > 1000000
basket = dados_youtube.groupby(['Country', 'high_earnings'])['rank'].count().unstack().fillna(0)

# Converter os dados para booleanos usando map
basket = basket > 0

# Aplicando o algoritmo
frequent_itemsets = apriori(basket, min_support=0.1, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

print(rules)

