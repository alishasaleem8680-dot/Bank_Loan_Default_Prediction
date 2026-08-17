import joblib
import pandas as pd

# Load final model
model_info = joblib.load("models/final_loan_default_model.pkl")

model = model_info["model"]
threshold = model_info["threshold"]

print("Final Loan Default Prediction Model Loaded")
print("Selected Threshold:", threshold)


def predict_default(input_data):

    input_df = pd.DataFrame([input_data])

    # One-hot encode categorical features
    input_encoded = pd.get_dummies(
        input_df,
        columns=[
            "Education",
            "EmploymentType",
            "MaritalStatus",
            "HasMortgage",
            "HasDependents",
            "LoanPurpose",
            "HasCoSigner"
        ],
        drop_first=True,
        dtype=int
    )

    # Match training features
    input_encoded = input_encoded.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    probability = model.predict_proba(input_encoded)[0][1]

    prediction = int(probability >= threshold)

    return prediction, probability


sample_loan = {
    "Age": 30,
    "Income": 50000,
    "LoanAmount": 100000,
    "CreditScore": 600,
    "MonthsEmployed": 24,
    "NumCreditLines": 2,
    "InterestRate": 15,
    "LoanTerm": 36,
    "DTIRatio": 0.5,
    "Education": "Bachelor's",
    "EmploymentType": "Full-time",
    "MaritalStatus": "Single",
    "HasMortgage": "Yes",
    "HasDependents": "No",
    "LoanPurpose": "Business",
    "HasCoSigner": "Yes"
}

prediction, probability = predict_default(sample_loan)

print("Default Prediction:", prediction)
print("Default Probability:", round(probability, 4))