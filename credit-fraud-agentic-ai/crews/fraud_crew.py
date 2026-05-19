from crewai import Crew, Task
from agents.fraud_agent import (
    create_fraud_agent
)
from memory.adaptive_memory import (
    AdaptiveMemory
)


def analyze_transaction(transaction):

    memory = AdaptiveMemory()

    previous_cases = (
        memory.retrieve_similar_cases(
            transaction
        )
    )

    context = "\n".join(previous_cases)

    agent = create_fraud_agent()

    task = Task(
        description=f"""
        Analyze the following transaction
        for fraud risk.

        Current transaction:
        {transaction}

        Similar historical cases:
        {context}

        Analyze:

        1. Fraud Score (0-1)
        2. Risk Level
        3. Suspicious Signals
        4. Recommendation

        Format response cleanly.
        """,

        expected_output="""
        Fraud report with
        score, reasoning,
        recommendation
        """,

        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    result = crew.kickoff()

    memory.store_case(
        transaction,
        str(result)
    )

    return str(result)