import json
import re
from crewai import Crew, Task
from agents.fraud_agent import (
    create_fraud_agent
)
from memory.adaptive_memory import (
    AdaptiveMemory
)
from rag.retriever import (
    FraudRetriever
)

from human_loop.review_engine import (
    HumanReviewEngine
)

def extract_score(text):

    match = re.search(
        r"Fraud Score.*?([0-9.]+)",
        text,
        re.IGNORECASE
    )

    if match:
        return float(match.group(1))

    return 0.5


def analyze_transaction(
    transaction
):

    memory = AdaptiveMemory()

    retriever = FraudRetriever()

    rag_context = (
        retriever.retrieve(
            transaction
        )
    )

    similar_cases = (
        memory.retrieve_similar_cases(
            transaction
        )
    )

    memory_context = (
        "\n".join(similar_cases)
        if similar_cases
        else "No historical cases."
    )

    agent = (
        create_fraud_agent()
    )

    task = Task(
        description=f"""
        Analyze the transaction.

        Transaction:
        {transaction}

        Fraud Policies (RAG):
        {rag_context}

        Similar Historical Cases:
        {memory_context}

        You must return:

        Fraud Score: number
        Risk Level:
        Reasoning:
        Recommendation:

        Rules:
        - Score between 0 and 1
        - Explain WHY
        - Mention policy triggers
        - Mention memory relevance
        """,

        expected_output="""
        Structured fraud report
        """,

        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    result = str(
        crew.kickoff()
    )

    fraud_score = (
        extract_score(result)
    )

    human_review = (
        HumanReviewEngine
        .needs_review(
            fraud_score
        )
    )

    memory.store_case(
        transaction,
        result
    )

    response = {
        "fraud_result": result,
        "fraud_score": fraud_score,
        "human_review":
            human_review
    }

    return response