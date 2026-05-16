class AuditorAgent:

    def evaluate(self, quant_data, research_data):

        risk_flags = []

        if quant_data["debt_to_equity"] > 2.5:
            risk_flags.append("High leverage detected")

        if len(research_data["findings"]) > 0:
            risk_flags.append("Potential fraud indicators found")

        recommendation = (
            "NO-GO" if len(risk_flags) > 0 else "GO"
        )

        return {
            "recommendation": recommendation,
            "risk_flags": risk_flags
        }
        
def auditor_agent(quant_data, research_data):
    agent = AuditorAgent()
    return agent.evaluate(quant_data, research_data)
