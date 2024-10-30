# Bibliotecas 
#Utilizar subscribers, video views e uploads para prever highest_yearly_earnings

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# Carregar a base de dados
url = "https://github.com/valdineyatilio/ProjetoAplicado-II/raw/refs/heads/main/Aula-02/BaseDeDadosYouTube.csv"
dados_youtube = pd.read_csv(url, encoding='latin1')

# Preparar os dados
X = dados_youtube[['subscribers', 'video views', 'uploads']]
y = dados_youtube['highest_yearly_earnings']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Treinar a rede neural
modelo = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=2000, learning_rate_init=0.0001, solver='sgd', alpha=0.001, random_state=42)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
print(f"Erro Quadrático Médio da Rede Neural: {mse}")
