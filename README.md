# 🏦 Bank Loan Default Prediction

A machine learning project that predicts whether a loan applicant is likely to default based on financial, credit, employment, and personal information.

The project includes data preprocessing, exploratory data analysis (EDA), class imbalance handling, machine learning model comparison, threshold tuning, feature importance analysis, and a final XGBoost-based prediction model.

---

## 📌 Project Overview

Loan default prediction is an important task in banking and financial risk management.

The goal of this project is to identify applicants who may be at higher risk of defaulting on their loans.

Because the dataset contains significantly more non-default cases than default cases, special attention was given to **class imbalance** and **recall for default cases**.

The final model uses **Balanced XGBoost with a classification threshold of 0.6**.

---

## 🎯 Project Objectives

* Analyze loan applicant data
* Perform exploratory data analysis (EDA)
* Understand factors associated with loan default
* Handle categorical variables using one-hot encoding
* Handle class imbalance
* Train and compare multiple machine learning models
* Evaluate models using suitable classification metrics
* Tune the classification threshold
* Identify important features
* Build a reusable prediction script

---

## 📊 Dataset

The dataset contains:

* **255,347 loan records**
* **18 original columns**
* No missing values
* No duplicate rows

### Main Features

* Age
* Income
* LoanAmount
* CreditScore
* MonthsEmployed
* NumCreditLines
* InterestRate
* LoanTerm
* DTIRatio
* Education
* EmploymentType
* MaritalStatus
* HasMortgage
* HasDependents
* LoanPurpose
* HasCoSigner
* Default

`LoanID` was not used as a prediction feature because it is an identifier.

---

## ⚠️ Class Imbalance

The target variable `Default` is imbalanced:

| Class          | Records | Percentage |
| -------------- | ------: | ---------: |
| 0 - No Default | 225,694 |     88.39% |
| 1 - Default    |  29,653 |     11.61% |

This means that simply achieving high accuracy is not enough.

The project therefore focuses more on **Recall, F1 Score, and ROC-AUC** when evaluating models.

---

## 🔍 Exploratory Data Analysis

EDA was performed to understand the relationship between applicant characteristics and loan defaults.

The analysis included:

* Default distribution
* Age analysis
* Loan amount analysis
* Interest rate analysis
* Credit score analysis
* Income analysis
* Correlation analysis
* Default rate comparisons across different applicant groups

### Important Observations

* Default cases represent a minority of the dataset.
* Interest rate showed a positive relationship with default.
* Age and income showed negative relationships with default.
* Loan amount and number of credit lines showed smaller positive relationships with default.
* Class imbalance significantly affected the performance of the original Logistic Regression and XGBoost models.

---

## 🛠️ Data Preprocessing

The following preprocessing steps were performed:

1. Checked the dataset structure
2. Checked missing values
3. Checked duplicate records
4. Removed `LoanID` from model features
5. Separated features and target
6. Applied one-hot encoding to categorical variables
7. Used stratified train-test splitting
8. Addressed class imbalance during model training

After one-hot encoding:

* **Original feature columns:** 16
* **Encoded feature columns:** 24

### Train-Test Split

The dataset was split into:

* **80% training data**
* **20% testing data**
* `random_state = 42`
* Stratified split to maintain the target distribution

---

## 🤖 Machine Learning Models

The following models were trained and compared:

1. Logistic Regression
2. Balanced Logistic Regression
3. Random Forest
4. XGBoost
5. Balanced XGBoost

The original models showed high accuracy but relatively low recall for default cases.

Balanced versions were therefore evaluated to give more importance to the minority default class.

---

## 📈 Model Comparison

| Model                        | Accuracy | Recall | F1 Score | ROC-AUC |
| ---------------------------- | -------: | -----: | -------: | ------: |
| Balanced Logistic Regression |   67.65% | 69.94% |   33.43% |  75.32% |
| Random Forest                |   88.08% | 14.82% |   22.40% |  74.73% |
| XGBoost                      |   88.62% |  7.30% |   12.96% |  75.46% |
| Balanced XGBoost             |   71.17% | 65.62% |   34.59% |  75.32% |

The comparison shows why accuracy alone is not sufficient for this problem.

The balanced models achieved much higher recall for identifying default cases.

---

## 🎚️ Threshold Tuning

After training Balanced XGBoost, different classification thresholds were tested.

| Threshold |  Precision |     Recall |   F1 Score |
| --------: | ---------: | ---------: | ---------: |
|       0.3 |     16.28% |     87.91% |     27.47% |
|       0.4 |     19.53% |     78.30% |     31.27% |
|       0.5 |     23.48% |     65.62% |     34.59% |
|   **0.6** | **28.79%** | **51.15%** | **36.85%** |
|       0.7 |     35.94% |     34.14% |     35.02% |

A threshold of **0.6** was selected because it produced the highest F1 Score among the tested thresholds.

---

## 🏆 Final Model

### Balanced XGBoost + Threshold 0.6

Final test performance:

| Metric    |     Result |
| --------- | ---------: |
| Accuracy  | **79.64%** |
| Precision | **28.79%** |
| Recall    | **51.15%** |
| F1 Score  | **36.85%** |
| ROC-AUC   | **75.32%** |

The final model was selected to provide a better balance between identifying default cases and limiting false positive predictions.

---

## 📊 Confusion Matrix

At the selected threshold of 0.6:

* True Negatives: **37,636**
* False Positives: **7,503**
* False Negatives: **2,897**
* True Positives: **3,034**

The model correctly identified **3,034 actual default cases** in the test set.

---

## ⭐ Feature Importance

The top features identified by the final Balanced XGBoost model included:

| Feature                   | Importance |
| ------------------------- | ---------: |
| Age                       |   0.122950 |
| InterestRate              |   0.073542 |
| Income                    |   0.062463 |
| HasCoSigner_Yes           |   0.059525 |
| HasDependents_Yes         |   0.054406 |
| MonthsEmployed            |   0.051712 |
| EmploymentType_Unemployed |   0.048972 |
| LoanAmount                |   0.047457 |
| HasMortgage_Yes           |   0.038290 |
| MaritalStatus_Married     |   0.037339 |

Age was the most important feature in the final model based on XGBoost feature importance.

---

## 📁 Project Structure

```text
Bank_Loan_Default_Prediction/
│
├── data/
│   ├── raw/
│   │   └── Loan_default.csv
│   │
│   └── cleaned/
│       └── loan_default_cleaned.csv
│
├── models/
│   ├── balanced_xgboost_model.pkl
│   ├── final_loan_default_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── 01_loan_default_analysis.ipynb
│
├── reports/
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── model_comparison.png
│
├── src/
│   └── predict.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/alishasaleem8680-dot/Bank_Loan_Default_Prediction.git
```

### 2. Open the Project

```bash
cd Bank_Loan_Default_Prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Prediction Script

```bash
python src/predict.py
```

The script loads the trained model, calculates the default probability, and applies the selected classification threshold.

---

## 💾 Saved Model

The final model is saved as:

```text
models/final_loan_default_model.pkl
```

The saved object contains:

* Balanced XGBoost model
* Selected classification threshold: **0.6**

---

## 🧰 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Joblib
* Jupyter Notebook
* Git
* GitHub

---

## 📌 Key Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis
* Data Preprocessing
* Categorical Encoding
* Class Imbalance Handling
* Machine Learning
* Model Comparison
* Model Evaluation
* Threshold Tuning
* Feature Importance
* Model Saving
* Prediction Pipeline
* Git & GitHub

---

## 🚀 Future Improvements

Possible future improvements include:

* Hyperparameter tuning
* Cross-validation
* Advanced imbalance techniques such as SMOTE
* Model explainability using SHAP
* Streamlit web application
* Free cloud deployment
* More detailed risk-level classification

---

## 👩‍💻 Author

**Alisha Saleem**

BS Data Science Graduate | Machine Learning | Data Analytics | Power BI

GitHub:
https://github.com/alishasaleem8680-dot

LinkedIn:
https://www.linkedin.com/in/alisha-saleem-4a1319379
