# Avanti-Bootcamp

# 🧠 Previsão de Diabetes com Regressão Logística

Este projeto tem como objetivo prever a presença de diabetes com base em dados clínicos usando um modelo de **Regressão Logística**.

---

## 📊 Sobre o Projeto

- O modelo foi desenvolvido para classificar se uma pessoa tem ou não diabetes (`Outcome`), com base em variáveis como:
  - Número de gestações
  - Glicose
  - Pressão arterial
  - Espessura da pele
  - Nível de insulina
  - IMC
  - Função hereditária de diabetes
  - Idade

---

## 📁 Fonte dos Dados

- Base de dados retirada do Kaggle: [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## ⚙️ Como Rodar o Projeto

### 1. Clone este repositório

```bash
git clone https://github.com/Lipesti/Avanti-Bootcamp/tree/eb5a22f829809dabe084b40618d9bd5af9c3b883/Atividade_1/Projeto_DiabetesMachineLearning
cd Projeto_DiabetesMachineLearning
```

### 2. Instale as bibliotecas necessárias

```bash
pip install pandas numpy scikit-learn colorama openpyxl
```

> A biblioteca `colorama` é usada para exibir os textos coloridos no terminal.

### 3. Execute o código principal

```bash
python miniProjetoML.py
```

---

## 🔍 Etapas do Projeto

O projeto foi dividido nas seguintes fases:

1. **Carregamento do Dataset**
2. **Limpeza e tratamento dos dados (substituindo zeros pela mediana)**
3. **Padronização das variáveis numéricas**
4. **Divisão dos dados:**
   - Treinamento: 70%
   - Validação: 15%
   - Teste: 15%
5. **Treinamento do modelo de Regressão Logística**
6. **Avaliação do desempenho nos conjuntos de validação e teste usando:**
   - Matriz de confusão
   - Acurácia
   - Precisão
   - Recall
   - F1-Score

---

## 🎨 Visualização com Cores no Terminal

Este projeto usa a biblioteca `colorama` para destacar os resultados com cores no terminal e facilitar a leitura das métricas.

### 📦 Instalar a biblioteca necessária

```bash
pip install colorama
```

> Compatível com Windows, Linux e MacOS.

---

### ▶️ Exemplo de Saída Colorida

Aqui está um exemplo visual do terminal após a execução do projeto:
![Resultado](https://github.com/user-attachments/assets/fc8fb450-6351-40ba-b6a1-f756d0e73524)



---

## ✅ Resultado Final

Ao fim da execução, você verá os resultados do modelo com destaque colorido, incluindo métricas no conjunto de validação e no conjunto de teste.

---

## ✍️ Autor

- **Felipe Santos**  
 

---

## 🧠 Aprendizados

Este projeto me ajudou a entender melhor como:
- Limpar e preparar dados reais
- Aplicar padronização
- Treinar e avaliar um modelo de classificação
- Dividir corretamente o conjunto de dados em três partes (treino, validação e teste)
- Interpretar métricas de avaliação de modelos
