# 🏥 Medical Insurance Annual Cost Prediction

**Machine Learning Zoomcamp – Midterm Project**

This project builds a full end-to-end machine learning solution to predict **annual medical insurance costs** using demographic, lifestyle, health, and insurance-related features.

---

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [📁 Project Structure](#-project-structure)
- [✅ Project Deliverables](#-project-deliverables)
- [📊 Dataset](#-dataset)
- [📓 Notebooks](#-notebooks)
- [⚙️ Model Training](#️-model-training)
- [🚀 Prediction Service](#-prediction-service)
- [🧪 Testing the API](#-testing-the-api)
- [📦 Dependencies](#-dependencies)
- [🐳 Docker Deployment](#-docker-deployment)
- [👨‍💻 Author](#-author)

---

## 🎯 Project Overview

The core goal of this project is to predict **annual medical insurance costs** for customers using a machine learning model. Insurance costs are determined by multiple factors, including age, BMI, lifestyle, chronic conditions, plan type, premiums, provider quality, and risk scores.

### Key Features

- **Data preparation & cleaning**
- **Exploratory Data Analysis (EDA)**
- **Feature engineering and multicollinearity reduction**
- **Model selection & hyperparameter tuning**
- **Final model training (Decision Tree Regressor)**
- **Serving the model via a REST API (Flask + Waitress)**
- **Local & Docker deployment**
- **Reproducible environment files**

---

## 📁 Project Structure

```
Midterm_Project/
│
├── dataset/
│   └── medical_insurance.csv
│
├── notebook/
│   ├── medical_Insurance_df_regression_with_EDA.ipynb
│   ├── completed_final_decision_tree_model_notebook.ipynb
│   ├── predict-test.ipynb
│   └── __pycache__/
│
├── train.py
├── predict.py
├── test.py
├── final_dt_model.bin
├── requirements.txt
├── environment.yml
├── Dockerfile
└── README.md
```

---

## ✅ Project Deliverables

This project successfully implements the following steps in the ML lifecycle:

- ✅ Cleaning medical insurance dataset
- ✅ Exploratory data analysis (EDA)
- ✅ Handling missing data and categorical encoding
- ✅ Log-transforming the target for better distribution
- ✅ Removing high multicollinearity using VIF
- ✅ Model comparison and tuning
- ✅ Training and exporting a final Decision Tree Regression model
- ✅ Building a Flask API to serve predictions
- ✅ Dockerizing the service for easy deployment

---

## 📊 Dataset

**File:** `dataset/medical_insurance.csv`

**Setup Note:** If the file is missing, please place it in the `dataset/` folder or update the file path inside `train.py`.

**Features include:**

- **Demographics:** age, sex, region, marital_status
- **Lifestyle:** smoker, alcohol_freq, bmi, physical activity
- **Health indicators:** blood pressure, hba1c, ldl, chronic conditions
- **Insurance details:** plan_type, deductible, network_tier, provider_quality
- **Claims data**
- **Target Variable:** annual_medical_cost

---

## 📓 Notebooks

These notebooks document the full ML lifecycle from exploration to deployment.

### `medical_Insurance_df_regression_with_EDA.ipynb`

- Initial cleaning
- EDA & visualizations
- Feature inspection
- Correlation analysis
- Problem statements

### `completed_final_decision_tree_model_notebook.ipynb`

- Final cleaned dataset
- VIF multicollinearity removal
- Train/validation model comparison
- Decision Tree tuning (max_depth, min_samples_split)
- Evaluation on log-transformed target

### `predict-test.ipynb`

- API testing
- Model inference examples

---

## ⚙️ Model Training

The training script performs feature engineering, cleaning, log-transformation, and encoding, then trains and saves the model.

**Training Steps:**

1. Loads dataset
2. Cleans missing values and drops high multicollinearity features
3. Log-transforms the target (`annual_medical_cost`)
4. Encodes categorical variables using DictVectorizer
5. Trains a `DecisionTreeRegressor(max_depth=15)`
6. Saves the model and vectorizer to `final_dt_model.bin`

**Run training:**
```bash
python train.py
```

**Output:** `final_dt_model.bin` (trained model and vectorizer)

---

## 🚀 Prediction Service

This is a Flask + Waitress API used to serve the trained model on port 9696.

**Run the API:**
```bash
python predict.py
```

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/ping` | GET | Health Check |
| `/predict` | POST | Returns the predicted medical cost |

### Example Request (POST `/predict`)

```json
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
```

---

## 🧪 Testing the API

Run this script to send an example request to the running prediction service.

```bash
python test.py
```

---

## 📦 Dependencies

### Option 1 — pip

```bash
pip install -r requirements.txt
```

### Option 2 — conda

```bash
conda env create -f environment.yml
conda activate datasciencejosepy
```

---

## 🐳 Docker Deployment

The service is configured for containerization for easy, reproducible deployment.

**Build image:**
```bash
docker build -t medical-insurance-api .
```

**Run container (Exposes port 9696):**
```bash
docker run -p 9696:9696 medical-insurance-api
```

The API will be available at: `http://localhost:9696/predict`

---

## 👨‍💻 Author

**Denis Munene Peter**  
Machine Learning Zoomcamp Midterm Project

---

*Last updated: November 2024*
