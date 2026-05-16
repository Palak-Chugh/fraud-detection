import pandas as pd

class QuantAgent:

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def analyze_company(self, company_id):

        company = self.df[self.df['company_id'] == company_id]

        if company.empty:
            return {"error": "Company not found"}

        company = company.iloc[0]

        debt_to_equity = (
            company['total_debt'] / max(company['total_equity'], 1)
        )

        current_ratio = (
            company['current_assets'] /
            max(company['current_liabilities'], 1)
        )

        return {
            "company_name": company['company_name'],
            "debt_to_equity": round(debt_to_equity, 2),
            "current_ratio": round(current_ratio, 2),
            "credit_score": company['credit_score'],
            "risk": company['bankruptcy_risk']
        }
   
def quant_agent(company_data):
    agent = QuantAgent("data/companies.csv")  # adjust path if needed
    return agent.analyze_company(company_data["company_id"])
