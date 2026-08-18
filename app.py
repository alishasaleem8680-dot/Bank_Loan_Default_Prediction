from flask import Flask, render_template, request
from src.predict import predict_default

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():

    input_data = {
        "Age": int(request.form["Age"]),
        "Income": float(request.form["Income"]),
        "LoanAmount": float(request.form["LoanAmount"]),
        "CreditScore": int(request.form["CreditScore"]),
        "MonthsEmployed": int(request.form["MonthsEmployed"]),
        "NumCreditLines": int(request.form["NumCreditLines"]),
        "InterestRate": float(request.form["InterestRate"]),
        "LoanTerm": int(request.form["LoanTerm"]),
        "DTIRatio": float(request.form["DTIRatio"]),
        "Education": request.form["Education"],
        "EmploymentType": request.form["EmploymentType"],
        "MaritalStatus": request.form["MaritalStatus"],
        "HasMortgage": request.form["HasMortgage"],
        "HasDependents": request.form["HasDependents"],
        "LoanPurpose": request.form["LoanPurpose"],
        "HasCoSigner": request.form["HasCoSigner"]
    }

    prediction, probability = predict_default(input_data)

    probability_percent = round(probability * 100, 2)

    if prediction == 1:
        result = "Likely to Default"
        risk = "High Risk"
    else:
        result = "Unlikely to Default"
        risk = "Low Risk"

    return render_template(
        "result.html",
        result=result,
        risk=risk,
        probability=probability_percent
    )


# Model Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Run Application
if __name__ == "__main__":
    app.run(debug=True)