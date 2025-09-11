
# 🏠 House Price Prediction

A machine learning project to predict house prices based on various features using regression models. This tool helps buyers, sellers, and real estate professionals make informed, data-driven decisions. 💰🏡

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Dataset](#dataset)
4. [Project Structure](#project-structure)
5. [Installation & Setup](#installation--setup)
6. [Usage](#usage)
7. [Model Training & Evaluation](#model-training--evaluation)
8. [Results](#results)
9. [Future Enhancements](#future-enhancements)
10. [Author](#author)

---

## 🚀 Project Overview

This project predicts house prices using regression models by analyzing features such as number of rooms, area, location, and other housing characteristics.

**Key Benefits:**
- 🏡 Accurate price estimation for buyers and sellers
- 📊 Market analysis for real estate professionals
- 💡 Data-driven property investment decisions

---

## 🛠 Technologies Used

- **Programming Language:** Python 🐍
- **Libraries/Frameworks:**
  - Pandas, NumPy – Data processing 🧮
  - Scikit-learn – Regression models 🤖
  - Matplotlib, Seaborn – Visualization 📊
  - Jupyter Notebook – Data exploration & modeling 💻
  - Pickle – Model serialization 💾

---

## 📂 Dataset

- Contains various house-related features (e.g., area, bedrooms, location, age).
- Located in the `data/` folder.

---

## 🗂 Project Structure

```
House-Price-Prediction/
│── data/                   # Dataset files
│── templates/              # HTML templates (for Flask app)
│── House_Price_Prediction.ipynb  # EDA & modeling notebook
│── price_pred.py           # Prediction script or Flask app
│── price_predictor.pkl     # Trained regression model
│── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

Clone the repository:
```bash
git clone https://github.com/Ramrajkrushn25/House_Price_Prediction.git
cd House-Price-Prediction
```

---

## 🎯 Usage

- **Jupyter Notebook:** Explore data, train models, and evaluate performance.
  ```bash
  jupyter notebook
  ```
- **Prediction Script/Web App:** Predict house prices.
  ```bash
  python price_pred.py
  ```
- Upload house features and get predicted prices 💰.

---

## 🧠 Model Training & Evaluation

**Models Trained:**
- Linear Regression
- Ridge Regression (with/without hyperparameter tuning)
- Lasso Regression (with/without hyperparameter tuning)

**Regression Metrics:**

| Model                | R² Score |   MSE   |  RMSE  |  MAE   |
|----------------------|:--------:|:-------:|:------:|:------:|
| Linear Regression    |  0.9161  | 0.0135  | 0.1162 | 0.0818 |
| Ridge (no tuning)    |  0.9222  | 0.0125  | 0.1119 | 0.0809 |
| Ridge (tuned)        |  0.9219  | 0.0126  | 0.1121 | 0.0809 |
| Lasso (no tuning)    |  0.9222  | 0.0125  | 0.1119 | 0.0830 |
| Lasso (tuned)        |    ...   | 0.0140  | 0.1185 | 0.0825 |

**Metrics Explained:**
- **R² Score:** Variance explained by the model 📈
- **MSE:** Mean Squared Error 🔢
- **RMSE:** Root Mean Squared Error 🧮
- **MAE:** Mean Absolute Error ✨

---

## 📈 Results

- Ridge and Lasso regression models achieved the highest accuracy (~92% R²).
- Linear Regression performed well with an R² of 0.916.
- The model reliably estimates house prices for informed real estate decisions. 🏡💵

---

## 🌟 Future Enhancements

- 🌐 Deploy as a web application for real-time predictions
- 📊 Add feature importance visualization
- ⏱ Incorporate geographical and temporal features
- 🤖 Integrate advanced models (e.g., XGBoost, Random Forest)

---

## 👨‍💻 Author

**Ramrajkrushn Dadhaniya**
