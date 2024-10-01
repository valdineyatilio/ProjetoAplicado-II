#Bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carregar os dados
url = "https://github.com/valdineyatilio/ProjetoAplicado-II/raw/refs/heads/main/Aula-02/BaseDeDadosYouTube.csv"
dados_youtube = pd.read_csv(url, encoding='latin1')

# Limpeza de dados
dados_youtube.drop_duplicates(inplace=True)
dados_youtube.fillna(dados_youtube.mean(numeric_only=True), inplace=True)

# Transformação de dados
numeric_columns = dados_youtube.select_dtypes(include=['float64', 'int64']).columns
scaler = StandardScaler()
dados_youtube[numeric_columns] = scaler.fit_transform(dados_youtube[numeric_columns])

# Dividindo os dados
train_dados_youtube, test_dados_youtube = train_test_split(dados_youtube, test_size=0.2, random_state=42)

# Exibindo as primeiras linhas dos conjuntos de treinamento e teste
print("Conjunto de Treinamento:")
print(train_dados_youtube.head())
print("\nConjunto de Teste:")
print(test_dados_youtube.head())
