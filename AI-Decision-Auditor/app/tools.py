import joblib
import pandas as pd
import os

# Load trained ML model and columns
MODEL_PATH = os.path.join(os.path.dirname(__file__), "risk_model.pkl")
COLUMNS_PATH = os.path.join(os.path.dirname(__file__), "model_columns.pkl")

model = joblib.load(MODEL_PATH)
model_columns = joblib.load(COLUMNS_PATH)

def compute_risk(input_data: dict):
    """
    Compute risk score and risk level for a given decision input.
    """

    # Convert input to DataFrame
    df = pd.DataFrame([input_data])

    # Encode categorical values
    df_encoded = pd.get_dummies(df, drop_first=True)

    # Align columns with training data
    df_encoded = df_encoded.reindex(columns=model_columns, fill_value=0)

    # Predict risk probability
    risk_score = model.predict_proba(df_encoded)[0][1]

    # Convert score to level
    if risk_score < 0.4:
        risk_level = "Low"
    elif risk_score < 0.7:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "risk_score": float(round(risk_score, 2)),
        "risk_level": risk_level
    }
