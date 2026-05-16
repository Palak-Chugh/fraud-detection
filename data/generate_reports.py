#pip install fpdf

from fpdf import FPDF
import pandas as pd
import os
import random

df = pd.read_csv("data/financials.csv")

os.makedirs("data/audit_reports", exist_ok=True)

for _, row in df.iterrows():

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    report = f"""
    Company Audit Report

    Company: {row['company_name']}
    Sector: {row['sector']}

    Revenue: {row['annual_revenue']}
    EBITDA: {row['ebitda']}
    Total Debt: {row['total_debt']}

    Current Assets: {row['current_assets']}
    Current Liabilities: {row['current_liabilities']}

    Cash Flow: {row['cash_flow']}

    """

    if row['hidden_liability'] == 1:
        report += "\nPotential undisclosed liability related to offshore subsidiary."

    if row['fraud_flag'] == 1:
        report += "\nIrregular financial transactions detected during review."

    pdf.multi_cell(0, 10, report)

    filename = f"data/audit_reports/{row['company_id']}.pdf"

    pdf.output(filename)

print("PDF reports generated!")