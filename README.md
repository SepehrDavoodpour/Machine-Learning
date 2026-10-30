# Machine Learning Classification & Evaluation: Breast Cancer Wisconsin Dataset

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📌 Objective
The objective of this project is to implement, evaluate, and compare the performance of several supervised machine learning classification algorithms using the **Breast Cancer Wisconsin Dataset**. 

To prevent data leakage and ensure robust evaluation, feature scaling and model training are organized using pipelines, assessed via the standard **Train-Test Splits**, and enhanced using **Ensemble Methods**.

---

## 📊 Dataset Overview
- **Source:** Breast Cancer Wisconsin (Diagnostic) Dataset.
- **Target Variable:** Binary classification (`class`: Benign vs. Malignant, encoded as `0` and `1`).
- **Data Preprocessing Steps:**
  - Dropping unnecessary identifier columns (`id`).
  - Handling missing values and coercing non-numeric formats (`bare_nucleoli`).
  - Removing duplicate rows to maintain data integrity.
  - Optional feature engineering sections (IQR outlier removal, high-correlation feature filtering).

---

## 🛠️ Models Implemented
The following base classifiers are implemented and evaluated:
1. **Support Vector Machine (SVM):** Utilizing an RBF kernel with regularization (`C=1.0`) and scaled features.
2. **K-Nearest Neighbors (KNN):** $k=5$ using the Minkowski metric ($p=2$).
3. **Multi-Layer Perceptron (MLP Neural Network):** Architecture with hidden layers `(16, 8)`, ReLU activation, and the Adam solver.
   - *Hyperparameter tuning experiments* include testing various activation functions (`identity`, `logistic`, `tanh`, `relu`) and neuron sizes.

### 🤝 Ensemble Methods
To boost predictive performance, the base models are combined using a **Voting Classifier**:
- **Hard Voting:** Majority rule prediction based on predicted class labels.
- **Soft Voting:** Weighted probability averaging across base classifiers.

---

## 📈 Evaluation Metrics
Models are comprehensively evaluated using:
- **Accuracy**
- **Precision, Recall, and F1-Score**
- **Confusion Matrix**

---

## 🚀 Code Structure & Usage

Make sure you have the required dependencies installed:
```bash
pip install pandas numpy matplotlib scikit-learn
