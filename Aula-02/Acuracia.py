# Bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import label_binarize, StandardScaler

# Carregar os dados
url = "https://github.com/valdineyatilio/ProjetoAplicado-II/raw/refs/heads/main/Aula-02/BaseDeDadosYouTube.csv"
dados_youtube = pd.read_csv(url, encoding='latin1')

# Colunas relevantes
dados_selecionados = dados_youtube[['rank', 'subscribers', 'video views', 'category', 'uploads', 'Country', 'video_views_for_the_last_30_days', 'lowest_monthly_earnings', 'highest_monthly_earnings', 'lowest_yearly_earnings', 'highest_yearly_earnings', 'subscribers_for_last_30_days']]

# Pré-processamento dos dados
X = dados_selecionados.drop('subscribers', axis=1)
y = dados_selecionados['subscribers']

# Tratar valores ausentes
X = X.fillna(0)
y = y.fillna(0)

# Codificar variáveis categóricas
X = pd.get_dummies(X, columns=['category', 'Country'], drop_first=True)

# Normalizar os dados
scaler = StandardScaler()
X = scaler.fit_transform(X)


# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Treinar o modelo
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# Calcular métricas
acuracia = accuracy_score(y_test, y_pred)
precisao = precision_score(y_test, y_pred, average='weighted', zero_division=1)
recall = recall_score(y_test, y_pred, average='weighted', zero_division=1)
f1 = f1_score(y_test, y_pred, average='weighted', zero_division=1)

# Verificar se há mais de uma classe em y_test
if len(set(y_test)) > 1:
    # Binarizar as classes para o cálculo do ROC AUC
    classes = list(set(y_train) | set(y_test))
    y_test_binarized = label_binarize(y_test, classes=classes)
    y_pred_proba = modelo.predict_proba(X_test)

    # Calcular ROC AUC
    try:
        roc_auc = roc_auc_score(y_test_binarized, y_pred_proba, multi_class='ovr')
        print(f"AUC-ROC: {roc_auc}")
    except ValueError as e:
        print(f"Erro ao calcular AUC-ROC: {e}")
else:
    print("AUC-ROC: Não é possível calcular o AUC-ROC com apenas uma classe presente em y_test.")

print(f"Acurácia: {acuracia}")
print(f"Precisão: {precisao}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")