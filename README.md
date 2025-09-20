@"
# Telco Customer Churn Prediction


This project focuses on predicting **customer churn** using the Kaggle Telco Customer Churn dataset.  
The workflow covers **data cleaning, exploratory data analysis (EDA), machine learning modeling (Logistic Regression & Random Forest), and feature importance analysis**.

---

## 📊 Dataset
- **Source:** [Kaggle – Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
- **Rows:** 7,043 customers  
- **Columns:** 21 features (demographics, contract, services, charges) + target `Churn`

## 🗂️ Project Structure

churn-project/
├─ data/
│ ├─ raw/
│ └─ processed/ # telco_clean.csv
├─ notebooks/
│ ├─ 01_load_data.py
│ ├─ 02_eda.py
│ └─ 03_model.py
├─ requirements.txt
└─ README.md

📊 Key Findings from EDA

Churn Rate: ≈ 26.5%

Contract: Month-to-month contracts have the highest churn, while two-year contracts have the lowest.

Tenure: New customers are more likely to churn.

Monthly Charges: Higher monthly charges correlate with higher churn.

Payment Method: Customers paying via Electronic Check churn more.

🤖 Models & Results

Logistic Regression

Accuracy: ~79%

Recall (Churn=1): ~54%

Random Forest

Accuracy: ~79%

Recall (Churn=1): ~50%

⚠️ Note: Accuracy is high, but recall for churn cases is moderate, meaning some churned customers are missed.

⭐ Feature Importance (Random Forest)

Top predictors influencing churn:

TotalCharges

tenure

MonthlyCharges

Contract (Month-to-month)

Contract (Two year)

OnlineSecurity (No)

TechSupport (No)

PaymentMethod (Electronic Check)

InternetService (Fiber optic)

OnlineBackup (No)

📌 Business Insights

High-risk customers: short-tenure, month-to-month contracts, high monthly charges, Electronic Check payments, no extra services.

Recommendations:

Offer loyalty discounts for new customers.

Encourage long-term contracts.

Bundle extra services (security, tech support) to reduce churn risk.

🔮 Possible Improvements

Handle class imbalance with SMOTE or threshold tuning.

Try advanced models: XGBoost, LightGBM, Gradient Boosting.

Perform hyperparameter optimization (GridSearchCV, RandomizedSearchCV).

Deploy as an API using Flask/Django for real-time predictions.
