from agents.quant_agent import QuantAgent
from agents.research_agent import ResearchAgent
from agents.auditor_agent import AuditorAgent

quant = QuantAgent("data/financials.csv")

research = ResearchAgent()

auditor = AuditorAgent()

company_id = "CMP0001"

quant_result = quant.analyze_company(company_id)

research_result = research.read_report(
    f"data/audit_reports/{company_id}.pdf"
)

final_result = auditor.evaluate(
    quant_result,
    research_result
)

print("\nQUANT ANALYSIS")
print(quant_result)

print("\nRESEARCH FINDINGS")
print(research_result)

print("\nFINAL AUDIT")
print(final_result)