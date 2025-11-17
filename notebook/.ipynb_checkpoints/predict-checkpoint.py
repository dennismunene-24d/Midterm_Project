import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, jsonify, Response
import json
from waitress import serve

# Load model and vectorizer
with open("final_dt_model.bin", "rb") as f_in:
    dv, model = pickle.load(f_in)

app = Flask("Annual_Medical_Cost_Prediction")

# Ping endpoint
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok", "message": "Medical Cost Prediction API is running"})

# Helper: pretty JSON
def pretty_json(data, status=200):
    return Response(json.dumps(data, indent=4), status=status, mimetype="application/json")

# Predict endpoint
@app.route("/predict", methods=["POST"])
def predict_medical_cost():
    data = request.get_json()

    if data is None:
        return pretty_json({"error": "No JSON body found"}, status=400)

    # Convert to DataFrame
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    elif isinstance(data, list):
        df = pd.DataFrame(data)
    else:
        return pretty_json({"error": "Input must be a dict or list of dicts"}, status=400)

    num_customers = len(df)
    print(f"📊 Processing {num_customers} customer(s)")

    # Transform and predict
    X = dv.transform(df.to_dict(orient="records"))
    y_pred_log = model.predict(X)
    y_pred = np.expm1(y_pred_log)  # reverse log1p

    # Round predictions to 2 decimals
    predictions = [round(float(x), 2) for x in y_pred]

    result = {
        "message": f"Predicted annual medical cost for {num_customers} customer(s)",
        "predictions": predictions
    }

    return pretty_json(result)

# Run with Waitress on Windows
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=9696)
