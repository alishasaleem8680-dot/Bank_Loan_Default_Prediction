# 🏦 Bank Loan Default Prediction

A machine learning project that predicts whether a loan applicant is likely to default based on financial, credit, employment, and personal information.

The project includes exploratory data analysis, data preprocessing, machine learning model comparison, an XGBoost-based final model, and an interactive Flask web application.

---

## 📌 Project Overview

Loan default prediction is an important task in banking and financial risk management.

This project uses historical loan applicant data to identify applicants who may be at higher risk of default.

The final machine learning model is integrated into a Flask web application where users can enter applicant information and receive:

- Default prediction
- Default probability
- Risk level
- Model performance insights

---

## 🎯 Project Objectives

- Analyze loan applicant data
- Perform exploratory data analysis (EDA)
- Identify important factors associated with loan default
- Handle categorical variables
- Train and compare multiple machine learning models
- Address class imbalance
- Select a suitable final model
- Build an interactive loan default prediction web application
- Present model performance through a dashboard

---

## 📊 Dataset

The dataset contains **255,347 loan records** and **18 original features**.

### Main Features

- Age
- Income
- LoanAmount
- CreditScore
- MonthsEmployed
- NumCreditLines
- InterestRate
- LoanTerm
- DTIRatio
- Education
- EmploymentType
- MaritalStatus
- HasMortgage
- HasDependents
- LoanPurpose
- HasCoSigner
- Default

The target variable is:

```text
Default