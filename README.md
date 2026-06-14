# 📊 Vendor Invoice Intelligence System  
**Freight Cost Prediction & Invoice Risk Flagging**

---

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [Business Objectives](#business-objectives)
- [Data Sources](#data-sources)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Models Used](#models-used)
- [Evaluation Metrics](#evaluation-metrics)
- [Application](#application)
- [Project Structure](#project-structure)
- [How to Run This Project](#how-to-run-this-project)
- [Author & Contact](#author--contact)

---

## 🚀 Project Overview

This project implements an **end-to-end machine learning system** designed to support finance teams by:

1. **Predicting expected freight cost** for vendor invoices  
2. **Flagging high-risk invoices** that require manual review  

The system helps automate decision-making and improve financial efficiency.

---

## 🎯 Business Objectives

- 📦 Improve freight cost forecasting accuracy  
- 🚨 Detect abnormal or suspicious invoices  
- 💰 Reduce financial leakage and fraud  
- ⚡ Automate invoice approval workflows  

---

## 📂 Data Sources

- Internal invoice dataset (SQLite database)
- Features include:
  - Invoice quantity
  - Invoice dollars
  - Freight cost
  - Total item quantity
  - Total item dollars

---

## 📊 Exploratory Data Analysis

- Distribution analysis of invoice values  
- Correlation between freight and invoice dollars  
- Outlier detection  
- Feature relationships visualization  

---

## 🤖 Models Used

### 🔹 Freight Cost Prediction
- Linear Regression ✅ (Best Model)
- Decision Tree Regressor
- Random Forest Regressor

### 🔹 Invoice Flagging
- Random Forest Classifier

---

## 📏 Evaluation Metrics

### Regression (Freight Prediction)
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

### Classification (Invoice Flag)
- Accuracy
- Precision
- Recall
- F1-score

---

## 💻 Application

A **Streamlit web app** is built to:

- Predict freight cost in real-time  
- Flag invoices for manual approval  
- Provide an interactive UI for finance users  

---

## 🗂️ Project Structure
