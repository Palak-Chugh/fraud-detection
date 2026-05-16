from faker import Faker
import pandas as pd
import numpy as np
import random
import os

fake = Faker()

NUM_COMPANIES = 1000

sectors = [
    "Manufacturing",
    "Technology",
    "Healthcare",
    "Retail",
    "Energy",
    "Finance",
]

data = []

for i in range(NUM_COMPANIES):

    revenue = random.randint(1_000_000, 100_000_000)

    ebitda = revenue * random.uniform(0.05, 0.35)

    debt = revenue * random.uniform(0.1, 1.2)

    equity = revenue * random.uniform(0.05, 0.8)

    current_assets = revenue * random.uniform(0.1, 0.5)

    current_liabilities = revenue * random.uniform(0.05, 0.4)

    interest_expense = debt * random.uniform(0.02, 0.12)

    cash_flow = revenue * random.uniform(-0.05, 0.25)

    fraud_flag = random.choice([0, 1])

    hidden_liability = random.choice([0, 1])

    leverage_ratio = debt / max(equity, 1)

    if leverage_ratio > 3:
        risk = "High"
        credit_score = random.randint(300, 550)
    elif leverage_ratio > 1.5:
        risk = "Medium"
        credit_score = random.randint(551, 700)
    else:
        risk = "Low"
        credit_score = random.randint(701, 850)

    data.append({
        "company_id": f"CMP{i+1:04}",
        "company_name": fake.company(),
        "sector": random.choice(sectors),
        "annual_revenue": round(revenue, 2),
        "ebitda": round(ebitda, 2),
        "total_debt": round(debt, 2),
        "total_equity": round(equity, 2),
        "current_assets": round(current_assets, 2),
        "current_liabilities": round(current_liabilities, 2),
        "interest_expense": round(interest_expense, 2),
        "cash_flow": round(cash_flow, 2),
        "employee_count": random.randint(50, 10000),
        "credit_score": credit_score,
        "fraud_flag": fraud_flag,
        "hidden_liability": hidden_liability,
        "bankruptcy_risk": risk
    })

df = pd.DataFrame(data)

os.makedirs("data", exist_ok=True)

df.to_csv("data/financials.csv", index=False)

print("Dataset generated successfully!")