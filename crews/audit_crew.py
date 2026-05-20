from crewai import (
    Crew,
    Task
)

from agents.audit_agent import (
    create_audit_agent
)

from rag.retriever import (
    FraudRetriever
)


def generate_audit(
    fraud_result,
    credit_result,
    human_review=False
):

    retriever = (
        FraudRetriever()
    )

    rag_context = (
        retriever.retrieve(
            "audit compliance"
        )
    )

    agent = (
        create_audit_agent()
    )

    task = Task(
        description=f"""
        Generate audit report.

        Fraud Analysis:
        {fraud_result}

        Credit Analysis:
        {credit_result}

        Human Review:
        {human_review}

        Audit Policies:
        {rag_context}

        Include:
        1. Decision Summary
        2. Risk Explanation
        3. Compliance Notes
        4. Final Recommendation
        """,

        expected_output="""
        Structured audit report
        """,

        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    return str(
        crew.kickoff()
    )