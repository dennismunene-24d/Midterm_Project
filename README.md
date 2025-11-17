# Annual Medical Cost Prediction — Decision Tree Regression Model

A machine learning project to predict annual medical costs using a Decision Tree Regression model.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Model Performance](#model-performance)

## 🎯 Project Overview

This project focuses on developing a **Machine Learning Regression Model** to accurately predict a patient's **annual medical cost** (the continuous target variable).

Accurate cost forecasting is vital for healthcare organizations, insurers, and policymakers. The model uses patient-level information, including:

- **Demographics**: Age, sex, region, urban/rural residence
- **Clinical Measurements**: BMI, blood pressure, chronic disease count
- **Healthcare Utilization**: Visits, claims, hospitalizations
- **Insurance Factors**: Plan type, deductible, copay
- **Lifestyle Factors**: Smoking, alcohol frequency

The final model chosen is a **Decision Tree Regressor**, selected for its fast training time and high performance (near-perfect R² scores) compared to computationally intensive alternatives like Random Forest.

## 📁 Project Structure
├── medical_Insurance_df_regression_with_EDA.ipynb # EDA, Feature Importance, Model Selection
├── train.py # Training script
├── predict.py # Flask prediction service
├── requirements.txt # Python dependencies
├── environment.yml # Conda environment
├── Dockerfile # Container configuration
├── predict-test.ipynb # API testing notebook
└── dataset/
└── medical_insurance.csv # Dataset (see setup instructions)  


## 📊 Dataset

### Setup Instructions

1. Obtain the `medical_insurance.csv` file
2. Create a folder named `dataset` in the root directory
3. Place the `medical_insurance.csv` file inside the `dataset/` folder

> **Note**: The `train.py` script expects the dataset at `dataset/medical_insurance.csv`

## 🚀 Installation & Setup

### Option A: Local Setup

#### 1. Install Dependencies

**Using pip:**
```bash
pip install -r requirements.txt  

## 📊 Dataset

### Setup Instructions

1. Obtain the `medical_insurance.csv` file
2. Create a folder named `dataset` in the root directory
3. Place the `medical_insurance.csv` file inside the `dataset/` folder

> **Note**: The `train.py` script expects the dataset at `dataset/medical_insurance.csv`

## 🚀 Installation & Setup

### Option A: Local Setup

#### 1. Install Dependencies

**Using pip:**
```bash
pip install -r requirements.txt

2. Train the Model
bash
python train.py
This generates the final_dt_model.bin file.

3. Run the Prediction Service
bash
python predict.py
The Flask service will start on port 9696.

Option B: Docker Setup
1. Build the Docker Image
bash
docker build -t medical-cost-prediction .
2. Run the Container
bash
docker run -it --rm -p 9696:9696 medical-cost-prediction
💻 Usage
API Endpoint
Method: POST

URL: http://localhost:9696/predict

Port: 9696

Example Request
python
import requests

url = "http://localhost:9696/predict"

customer = {
    "age": 45, "sex": "male", "region": "northwest", "urban_rural": "urban", "income": 75000.0,
    "education": "bachelor", "marital_status": "married", "employment_status": "employed",
    "household_size": 3, "dependents": 1, "bmi": 27.5, "smoker": "no",
    "alcohol_freq": "never", "visits_last_year": 2, "hospitalizations_last_3yrs": 0,
    "days_hospitalized_last_3yrs": 0, "medication_count": 1, "systolic_bp": 120.0,
    "diastolic_bp": 80.0, "ldl": 110.0, "hba1c": 5.4, "plan_type": "HMO",
    "network_tier": "Silver", "deductible": 500, "copay": 25, "policy_term_years": 3,
    "policy_changes_last_2yrs": 0, "provider_quality": 4.5, "risk_score": 0.2,
    "annual_premium": 5000.0, "claims_count": 2, "avg_claim_amount": 300.0,
    "total_claims_paid": 600.0, "chronic_count": 0, "hypertension": 0,
    "proc_imaging_count": 0, "proc_surgery_count": 0, "proc_physio_count": 0,
    "proc_consult_count": 1, "proc_lab_count": 1, "is_high_risk": 0,
    "had_major_procedure": 0
}

response = requests.post(url, json=customer)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
Example Response
json
{
    "message": "Predicted annual medical cost for 1 customer(s)",
    "predictions": [18570.42]
}
📈 Model Performance
The Decision Tree Regressor model demonstrates:

High predictive accuracy with near-perfect R² scores

Fast training time compared to ensemble methods

Interpretable results for healthcare stakeholders

 
