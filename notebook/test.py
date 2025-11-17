import requests

url = "http://localhost:9696/predict"

customer = {
    "age": 45,
    "sex": "male",
    "region": "northwest",
    "urban_rural": "urban",
    "income": 75000.0,
    "education": "bachelor",
    "marital_status": "married",
    "employment_status": "employed",
    "household_size": 3,
    "dependents": 1,
    "bmi": 27.5,
    "smoker": "no",
    "alcohol_freq": "never",
    "visits_last_year": 2,
    "hospitalizations_last_3yrs": 0,
    "days_hospitalized_last_3yrs": 0,
    "medication_count": 1,
    "systolic_bp": 120.0,
    "diastolic_bp": 80.0,
    "ldl": 110.0,
    "hba1c": 5.4,
    "plan_type": "HMO",
    "network_tier": "Silver",
    "deductible": 500,
    "copay": 25,
    "policy_term_years": 3,
    "policy_changes_last_2yrs": 0,
    "provider_quality": 4.5,
    "risk_score": 0.2,
    "annual_premium": 5000.0,
    "claims_count": 2,
    "avg_claim_amount": 300.0,
    "total_claims_paid": 600.0,
    "chronic_count": 0,
    "hypertension": 0,
    "proc_imaging_count": 0,
    "proc_surgery_count": 0,
    "proc_physio_count": 0,
    "proc_consult_count": 1,
    "proc_lab_count": 1,
    "is_high_risk": 0,
    "had_major_procedure": 0
}

response = requests.post(url, json=customer)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
