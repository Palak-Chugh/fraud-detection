from crewai import Agent, Task, Crew

from rag.retriever import retrieve_context

from agents.quant_agent import QuantAgent

quant_tool = QuantAgent("data/financials.csv")

quant_agent = Agent(
    role="Senior Credit Risk Analyst",
    goal="Analyze company financial metrics",
    backstory="Expert in credit underwriting and ratio analysis",
    verbose=True
)

research_agent = Agent(
    role="Financial Research Analyst",
    goal="Find hidden liabilities and fraud clues from reports",
    backstory="Expert in forensic accounting and financial audits",
    verbose=True
)

auditor_agent = Agent(
    role="Chief Auditor",
    goal="Provide final lending recommendation",
    backstory="Senior banking auditor responsible for final approvals",
    verbose=True
)

def run_credit_audit(company_id):

    quant_data = quant_tool.analyze_company(company_id)

    context = retrieve_context(
        f"Find fraud or liabilities for {company_id}"
    )

    quant_task = Task(
        description=f"""
        Analyze financial metrics:

        {quant_data}

        Determine financial risk.
        """,
        expected_output="Risk analysis summary",
        agent=quant_agent
    )

    research_task = Task(
        description=f"""
        Analyze report findings:

        {context}

        Detect fraud indicators.
        """,
        expected_output="Fraud analysis summary",
        agent=research_agent
    )

    final_task = Task(
        description="""
        Combine all findings and generate final GO/NO-GO decision.
        """,
        expected_output="Final audit recommendation",
        agent=auditor_agent
    )

    crew = Crew(
        agents=[
            quant_agent,
            research_agent,
            auditor_agent
        ],
        tasks=[
            quant_task,
            research_task,
            final_task
        ],
        verbose=True
    )

    result = crew.kickoff()

    return result