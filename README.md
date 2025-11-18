# Medical Insurance Annual Cost Prediction

Machine Learning Zoomcamp – Midterm Project

This project builds a full end-to-end machine learning solution to predict annual medical insurance costs using demographic, lifestyle, health, and insurance-related features.

## 📋 Project Overview

The goal of this project is to predict annual medical insurance costs for customers using machine learning. Insurance costs depend on multiple factors including age, BMI, lifestyle, chronic conditions, plan type, premiums, provider quality, and risk scores.

### 🎯 Key Features

- **Data preparation & cleaning**
- **Exploratory Data Analysis (EDA)**
- **Feature engineering and multicollinearity reduction**
- **Model selection & hyperparameter tuning**
- **Final model training (Decision Tree Regressor)**
- **Serving the model via a REST API (Flask + Waitress)**
- **Local & Docker deployment**
- **Reproducible environment files**

## 📁 Project Structure
Midterm_Project/
│
├── dataset/
│ └── medical_insurance.csv
│
├── notebook/
│ ├── medical_Insurance_df_regression_with_EDA.ipynb
│ ├── completed_final_decision_tree_model_notebook.ipynb
│ ├── predict-test.ipynb
│ └── pycache/
│
├── train.py
├── predict.py
├── test.py
├── final_dt_model.bin
├── requirements.txt
├── environment.yml
├── Dockerfile
└── README.md (this file)


## 1. Project Description

The project includes:

- ✔ Cleaning medical insurance dataset
- ✔ Exploratory data analysis (EDA)
- ✔ Handling missing data and categorical encoding
- ✔ Log-transforming the target for better distribution
- ✔ Removing high multicollinearity using VIF
- ✔ Model comparison and tuning
- ✔ Training and exporting a final Decision Tree Regression model
- ✔ Building a Flask API to serve predictions
- ✔ Dockerizing the service for easy deployment

## 2. Dataset

**File:** `dataset/medical_insurance.csv`

If missing, place the file in the `dataset/` folder or update the file path inside `train.py`.

**Features include:**
- **Demographics**: age, sex, region, marital_status
- **Lifestyle**: smoker, alcohol_freq, bmi, physical activity
- **Health indicators**: blood pressure, hba1c, ldl, chronic conditions
- **Insurance details**: plan_type, deductible, network_tier, provider_quality
- **Claims data**
- **Cost variables** including target: `annual_medical_cost`

## 3. Notebooks

### 📓 `medical_Insurance_df_regression_with_EDA.ipynb`
- Initial cleaning
- EDA & visualizations
- Feature inspection
- Correlation analysis
- Problem statements

### 📓 `completed_final_decision_tree_model_notebook.ipynb`
- Final cleaned dataset
- VIF multicollinearity removal
- Train/validation model comparison
- Decision Tree tuning (max_depth, min_samples_split)
- Evaluation on log-transformed target

### 📓 `predict-test.ipynb`
- API testing
- Model inference examples

These notebooks document the full ML lifecycle from exploration to deployment.

## 4. Model Training (`train.py`)

The training script:
- Loads dataset
- Cleans missing values
- Drops high multicollinearity features
- Log-transforms the target (`annual_medical_cost`)
- Encodes categorical variables using DictVectorizer
- Trains a `DecisionTreeRegressor(max_depth=15)`
- Saves model + vectorizer to `final_dt_model.bin`

**Run training:**
```bash
python train.py


Output:

final_dt_model.bin (trained model and vectorizer)

5. Prediction Service (predict.py)
A Flask + Waitress API used to serve the trained model.

Endpoints:

Health Check

GET /ping

Prediction

POST /predict

Example Request (JSON):
{
  "age": 45,
  "sex": "male",
  "region": "northwest",
  "income": 75000,
  "bmi": 27.5,
  "smoker": "no",
  "alcohol_freq": "never",
  "visits_last_year": 2,
  "provider_quality": 4.5,
  "annual_premium": 5000
}
Run the API:
python predict.py

6. Testing the API (test.py)
Example script to test the running service via requests.

python test.py

7. Dependencies

Option 1 — pip

pip install -r requirements.txt

Option 2 — conda

conda env create -f environment.yml
conda activate datasciencejosepy

8. Docker Deployment

Build image:

docker build -t medical-insurance-api .

Run container:

docker run -p 9696:9696 medical-insurance-api

API now available at:

http://localhost:9696/predict

9. Author

Denis Munene Peter




