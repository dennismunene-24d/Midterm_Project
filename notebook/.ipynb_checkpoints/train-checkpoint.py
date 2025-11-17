# Final Decision Tree Model Script

import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeRegressor
import pickle
from datetime import datetime

print("🚀 Starting Medical Insurance Cost Prediction Model Training...")
print(f"📅 Training started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Load dataset
print("\n📂 Loading dataset...")
path = r"C:\Users\HP\Desktop\Machine_Learning_Zoomcamp\Midterm_Project\dataset\medical_insurance.csv"
df = pd.read_csv(path)
print(f"✅ Dataset loaded successfully! Shape: {df.shape}")

# Preprocessing
print("\n🔄 Starting data preprocessing...")

# Drop identifier
print("🗑️  Dropping person_id column...")
df = df.drop(columns=['person_id'])

# Fill missing categorical values
print("🔧 Handling missing values in alcohol_freq...")
df['alcohol_freq'] = df['alcohol_freq'].fillna('Unknown')
print(f"   Missing values filled: {df['alcohol_freq'].isnull().sum()} remaining")

# Log-transform the target
print("📊 Applying log transformation to target variable...")
df['annual_medical_cost_log'] = np.log1p(df['annual_medical_cost'])
df = df.drop(columns=['annual_medical_cost'])
df = df.rename(columns={'annual_medical_cost_log': 'annual_medical_cost'})
print("✅ Target variable transformed to log scale")

# Drop columns with infinite VIF (high multicollinearity)
print("🎯 Removing highly correlated features...")
drop_inf_cols = [
    'diabetes', 'liver_disease', 'arthritis', 'mental_health', 'asthma', 
    'copd', 'cardiovascular_disease', 'cancer_history', 'kidney_disease',
    'monthly_premium'
]
df = df.drop(columns=drop_inf_cols)
print(f"✅ Removed {len(drop_inf_cols)} highly correlated features")
print(f"   Dataset shape after dropping columns: {df.shape}")

# Feature Columns
print("\n🔍 Analyzing feature types...")
categorical_columns = df.columns[df.dtypes == 'object'].tolist()
numerical_columns = list(set(df.columns) - set(categorical_columns))

# Remove target from numerical features
numerical_columns.remove('annual_medical_cost')

features = numerical_columns + categorical_columns

print(f"📊 Feature breakdown:")
print(f"   - Numerical features: {len(numerical_columns)}")
print(f"   - Categorical features: {len(categorical_columns)}")
print(f"   - Total features: {len(features)}")
print(f"   - Target variable: annual_medical_cost (log scale)")

# Convert data to Dict format for DictVectorizer
print("\n🔄 Converting data to dictionary format...")
df_dict = df[features].to_dict(orient='records')
print("✅ Data converted to dictionary format")

# Initialize vectorizer
print("🔧 Initializing DictVectorizer...")
dv = DictVectorizer(sparse=False)
X_full = dv.fit_transform(df_dict)
print(f"✅ Features transformed! Final feature matrix shape: {X_full.shape}")

# Target variable
y_full = df['annual_medical_cost'].values
print(f"🎯 Target variable shape: {y_full.shape}")

# Train final Decision Tree model
print("\n🌳 Training Decision Tree model...")
print("   Model parameters: max_depth=15, min_samples_split=10, min_samples_leaf=1")
final_dt = DecisionTreeRegressor(
    max_depth=15,
    min_samples_split=10,
    min_samples_leaf=1,
    random_state=42
)

final_dt.fit(X_full, y_full)
print("✅ Model training completed successfully!")

# Model performance check
train_score = final_dt.score(X_full, y_full)
print(f"📈 Model R² score on training data: {train_score:.4f}")

# Save combined model (vectorizer + model) using pickle
print("\n💾 Saving model artifacts...")
output_file = "final_dt_model.bin"

with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, final_dt), f_out)

print(f"✅ Model and vectorizer saved to: {output_file}")
print(f"📦 File includes: DictVectorizer + DecisionTreeRegressor")

print(f"\n🎉 Training pipeline completed successfully!")
print(f"📅 Training finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"📊 Final model trained on {X_full.shape[0]} samples with {X_full.shape[1]} features")
print("🚀 Model is ready for predictions!")

# Print usage instructions
print("\n" + "="*50)
print("📋 USAGE INSTRUCTIONS:")
print("="*50)
print("To make predictions, use:")
print("""
with open('final_dt_model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)
    
# For new customer data
new_customer = {...}  # your customer data as dict
customer_df = pd.DataFrame([new_customer])
X_new = dv.transform(customer_df.to_dict(orient='records'))
y_pred_log = model.predict(X_new)
y_pred_dollars = np.expm1(y_pred_log)
print(f"Predicted cost: ${y_pred_dollars[0]:.2f}")
""")
  