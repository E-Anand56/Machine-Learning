# 🏦 Banknote Authentication using Support Vector Machine (SVM)

## 📌 Project Overview

This project uses a **Support Vector Machine (SVM)** classifier to predict whether a banknote is **Genuine** or **Fake** based on four numerical features extracted from banknote images.

The project covers the complete Machine Learning workflow, from data preprocessing and exploratory data analysis (EDA) to model training, evaluation, and deployment using Streamlit.

---

## 🎯 Problem Statement

Counterfeit banknotes are a significant issue in financial systems. The goal of this project is to build a machine learning model that can accurately classify banknotes as **Genuine** or **Fake** using statistical features extracted from their images.

---

## 📊 Dataset Information

**Dataset:** Banknote Authentication Dataset

**Features**

- Variance
- Skewness
- Kurtosis
- Entropy

**Target**

- 0 → Genuine Banknote
- 1 → Fake Banknote

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 📈 Machine Learning Workflow

- Data Loading
- Data Understanding
- Exploratory Data Analysis (EDA)
- Missing Value Check
- Duplicate Check
- Outlier Detection (IQR Method)
- Skewness Analysis
- Feature Scaling (StandardScaler)
- Train-Test Split
- Model Training (Support Vector Machine)
- Cross Validation
- Model Evaluation
- Model Saving using Joblib
- Streamlit Deployment

---

## 🤖 Machine Learning Algorithm

**Support Vector Machine (SVM)**

Reasons for choosing SVM:

- Effective for binary classification
- Performs well on small to medium-sized datasets
- Works well with high-dimensional data
- Finds the optimal separating hyperplane with maximum margin

---

## 📊 Model Evaluation

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Cross Validation

### Cross Validation Results

| Metric | Score |
|---------|--------|
| Accuracy | **99.75%** |
| Precision | **99.19%** |
| Recall | **100%** |
| F1 Score | **99.59%** |