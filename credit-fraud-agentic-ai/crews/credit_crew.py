from crewai import (
    Crew,
    Task
)

from agents.credit_risk_agent import (
    create_credit_agent
)

from rag.retriever import (
    FraudRetriever
)

from memory.adaptive_memory import (
    AdaptiveMemory
)


def analyze_credit(
    customer_data
):

    retriever = (
        FraudRetriever()
    )

    memory = (
        AdaptiveMemory()
    )

    rag_context = (
        retriever.retrieve(
            customer_data
        )
    )

    memory_context = (
        memory
        .retrieve_similar_cases(
            customer_data
        )
    )

    agent = (
        create_credit_agent()
    )

    task = Task(
        description=f"""
        Analyze customer
        credit risk.

        Customer Data:
        {customer_data}

        Credit Policies:
        {rag_context}

        Historical Cases:
        {memory_context}

        Return:

        Credit Risk:
        Confidence:
        Default Probability:
        Recommendation:
        Reasoning:
        """,

        expected_output="""
        Credit risk report
        """,

        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    result = (
        crew.kickoff()
    )

    memory.store_case(
        customer_data,
        str(result)
    )

    return str(result)