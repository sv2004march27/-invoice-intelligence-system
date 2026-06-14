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
```text
📦 INVOICE_PROJECT
 ┣ 📂 .vscode/                       # VS Code workspace settings
 ┃ ┗ 📜 settings.json
 ┣ 📂 invoice/                       # General invoice handling module
 ┣ 📂 invoice_intelligence_system/   # Core Machine Learning package
 ┃ ┣ 📂 __pycache__/
 ┃ ┣ 📂 data/                        # Datasets for training and testing
 ┃ ┣ 📂 freight_cost_prediction/     # ML module for freight cost analysis
 ┃ ┣ 📂 inference/                   # Model inference and prediction scripts
 ┃ ┣ 📂 invoice_flagging_/           # Anomaly detection and flagging logic
 ┃ ┣ 📂 notebooks/                   # Jupyter notebooks for experimentation
 ┃ ┗ 📜 __init__.py
 ┣ 📂 venv/                          # Python virtual environment (ignored in git)
 ┃ ┣ 📂 etc/
 ┃ ┣ 📂 Include/
 ┃ ┣ 📂 Lib/
 ┃ ┣ 📂 Scripts/
 ┃ ┣ 📂 share/
 ┃ ┗ ⚙️ pyvenv.cfg
 ┣ 📜 app.py                         # Main application entry point
 ┣ 📜 README.md                      # Project documentation
 ┗ 📜 requirements.txt               # Python dependencies



---

## 🎯 Project Objective

The **Invoice Intelligence System** is an AI-driven solution designed to automate, optimize, and secure the invoice processing workflow. By leveraging Machine Learning and data analytics, this project aims to reduce manual review times, identify financial anomalies, and intelligently validate logistical expenses.

### Key Features & Goals:

*   **🚩 Automated Invoice Flagging:** Utilizes machine learning algorithms to automatically detect anomalies, data entry errors, discrepancies, or potentially fraudulent activities within incoming invoices.
*   **🚚 Freight Cost Prediction:** Analyzes historical shipping and invoice data to predict and validate freight costs. This helps ensure accurate billing, prevents overcharging, and optimizes logistics budgets.
*   **⚡ Seamless Model Inference:** Features a robust inference pipeline designed to quickly process new invoice data through trained models, delivering fast and reliable insights.
*   **💻 End-to-End Application:** Integrates complex predictive models into a cohesive, user-friendly application (`app.py`), bridging the gap between raw data science and practical business utility.

---
