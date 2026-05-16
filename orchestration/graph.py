from agents.quant_agent import QuantAgent
from agents.research_agent import ResearchAgent
from agents.auditor_agent import AuditorAgent
from agents.crew_setup import run_credit_audit

def run_pipeline(company_data):
    quant_result = quant_agent(company_data)
    research_result = research_agent(company_data["name"])
    
    final_decision = auditor_agent(quant_result, research_result)

    return {
        "quant": quant_result,
        "research": research_result,
        "decision": final_decision
    }