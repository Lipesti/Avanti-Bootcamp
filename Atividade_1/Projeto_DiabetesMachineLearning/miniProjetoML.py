# --- PASSO 1: Carregar as Bibliotecas Essenciais ---
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.GREEN + "Bibliotecas importadas com sucesso!")

# --- PASSO 2: Carregar o Dataset (arquivo .xlsx localmente) ---
print(Fore.CYAN + "\nLendo o arquivo local 'diabetes_formatado.xlsx'...")
file_name = 'diabetes_formatado.xlsx'

try:
    df = pd.read_excel('docs/diabetes_formatado.xlsx')
    print(Fore.GREEN + f"\nArquivo '{file_name}' carregado com sucesso!")
    print(Fore.YELLOW + "\nPrimeiras 5 linhas do dataset original:")
    print(df.head())
    print(Fore.YELLOW + f"\nShape do dataset (linhas, colunas): {df.shape}")
except FileNotFoundError:
    print(Fore.RED + f"Erro: O arquivo '{file_name}' não foi encontrado.")
    exit()
except Exception as e:
    print(Fore.RED + f"Ocorreu um erro ao carregar o arquivo: {e}")
    exit()

# --- PASSO 2.1: Análise Inicial e Tratamento de Zeros como Dados Ausentes ---
columns_to_impute = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

print(Fore.LIGHTBLUE_EX + "\n--- Verificacao e Tratamento de Zeros ---")
print("Numero de zeros antes da substituicao:")
for col in columns_to_impute:
    num_zeros = (df[col] == 0).sum()
    print(Fore.YELLOW + f"- {col}: {num_zeros}")

print(Fore.CYAN + "\nSubstituindo zeros pela mediana:")
for col in columns_to_impute:
    median_value = df.loc[df[col] != 0, col].median()
    df[col] = df[col].replace(0, median_value)
    print(Fore.LIGHTGREEN_EX + f"- {col}: Zeros substituídos pela mediana ({median_value:.2f})")

print(Fore.LIGHTBLUE_EX + "\nVerificando novamente os zeros:")
for col in columns_to_impute:
    num_zeros_after = (df[col] == 0).sum()
    print(Fore.YELLOW + f"- {col}: {num_zeros_after}")

print(Fore.YELLOW + "\nPrimeiras 5 linhas do dataset apos substituicao dos zeros:")
print(df.head())

# --- PASSO 3: Padronizacao dos Dados ---
features = df.drop('Outcome', axis=1)
target = df['Outcome']

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
features_scaled_df = pd.DataFrame(features_scaled, columns=features.columns)

print(Fore.GREEN + "\n--- Padronizacao ---")
print(Fore.CYAN + "Dados padronizados com sucesso!")
print(features_scaled_df.head())

# --- PASSO 4: Divisao dos Dados ---
X_train, X_temp, y_train, y_temp = train_test_split(features_scaled_df, target, test_size=0.30, random_state=42, stratify=target)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp)

print(Fore.LIGHTBLUE_EX + "\n--- Divisao dos Dados ---")
print(f"Treinamento: {X_train.shape[0]} amostras")
print(f"Validacao: {X_val.shape[0]} amostras")
print(f"Teste: {X_test.shape[0]} amostras")

# --- PASSO 5: Treinamento do Modelo ---
model = LogisticRegression(random_state=42, solver='liblinear')
print(Fore.GREEN + "\n--- Treinamento do Modelo ---")
model.fit(X_train, y_train)
print(Fore.GREEN + "Modelo treinado com sucesso!")

# --- PASSO 6: Avaliacao no Conjunto de Validacao ---
y_pred_val = model.predict(X_val)
cm_val = confusion_matrix(y_val, y_pred_val)
accuracy_val = accuracy_score(y_val, y_pred_val)
precision_val = precision_score(y_val, y_pred_val)
recall_val = recall_score(y_val, y_pred_val)
f1_val = f1_score(y_val, y_pred_val)

print(Fore.MAGENTA + "\n--- Avaliacao no Conjunto de Validacao ---")
print(Fore.CYAN + "Matriz de Confusao:")
print(Fore.YELLOW + str(cm_val))
print(Fore.LIGHTBLUE_EX + f"Acuracia: {accuracy_val:.4f}")
print(Fore.LIGHTGREEN_EX + f"Precisao: {precision_val:.4f}")
print(Fore.LIGHTMAGENTA_EX + f"Recall: {recall_val:.4f}")
print(Fore.LIGHTCYAN_EX + f"F1-Score: {f1_val:.4f}")

# --- PASSO 7: Avaliacao Final no Conjunto de Teste ---
y_pred_test = model.predict(X_test)
cm_test = confusion_matrix(y_test, y_pred_test)
accuracy_test = accuracy_score(y_test, y_pred_test)
precision_test = precision_score(y_test, y_pred_test)
recall_test = recall_score(y_test, y_pred_test)
f1_test = f1_score(y_test, y_pred_test)

print(Fore.MAGENTA + "\n--- Avaliacao Final no Conjunto de Teste ---")
print(Fore.CYAN + "Matriz de Confusao:")
print(Fore.YELLOW + str(cm_test))
print(Fore.LIGHTBLUE_EX + f"Acuracia: {accuracy_test:.4f}")
print(Fore.LIGHTGREEN_EX + f"Precisao: {precision_test:.4f}")
print(Fore.LIGHTMAGENTA_EX + f"Recall: {recall_test:.4f}")
print(Fore.LIGHTCYAN_EX + f"F1-Score: {f1_test:.4f}")

print(Fore.LIGHTGREEN_EX + "\n--- Projeto Concluido com Sucesso! ---")