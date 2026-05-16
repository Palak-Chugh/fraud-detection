# pip install scikit-learn

import pandas as pd

from sklearn.ensemble import IsolationForest

df = pd.read_csv("data/financials.csv")

features = df[[
    "annual_revenue",
    "ebitda",
    "total_debt",
    "cash_flow"
]]

model = IsolationForest(
    contamination=0.1,
    random_state=42
)

model.fit(features)

df["anomaly"] = model.predict(features)

print(df[["company_name", "anomaly"]].head())