print("FRAUD CREW STEP 1")

import re

print("FRAUD CREW STEP 2")

from crewai import (
    Crew,
    Task
)

print("FRAUD CREW STEP 3")

from agents.fraud_agent import (
    create_fraud_agent
)

print("FRAUD CREW STEP 4")


# TEMP MOCKS
# We will reconnect RAG + Memory later


class FraudRetriever:

    def retrieve(
        self,
        query
    ):
        print("RAG CALLED")

        return """
        Transactions above ₹50,000
        using a new device
        between 12 AM and 4 AM
        should be reviewed manually.

        Trusted devices reduce risk.
        """


class AdaptiveMemory:

    def retrieve_similar_cases(
        self,
        transaction
    ):
        print("MEMORY RETRIEVAL")

        return [
            "Similar case: High-value night transaction."
        ]

    def store_case(
        self,
        transaction,
        result
    ):
        print("MEMORY STORED")


class HumanReviewEngine:

    @staticmethod
    def needs_review(
        fraud_score
    ):
        return fraud_score > 0.75


print("FRAUD CREW STEP 5")


def extract_score(text):

    print("EXTRACTING SCORE")

    try:

        match = re.search(
            r"([0-9]*\.[0-9]+|[0-9]+)",
            text
        )

        if match:

            score = float(
                match.group(1)
            )

            if score > 1:
                score = (
                    score / 100
                )

            return score

    except Exception as e:
        print(
            "Score extraction error:",
            e
        )

    return 0.5


print("FRAUD CREW STEP 6")


def analyze_transaction(
    transaction
):

    print("START analyze_transaction")

    memory = (
        AdaptiveMemory()
    )

    retriever = (
        FraudRetriever()
    )

    print("GETTING RAG")

    rag_context = (
        retriever.retrieve(
            transaction
        )
    )

    print("GETTING MEMORY")

    similar_cases = (
        memory
        .retrieve_similar_cases(
            transaction
        )
    )

    memory_context = (
        "\n".join(similar_cases)
        if similar_cases
        else "No historical cases."
    )

    print("CREATING AGENT")

    agent = (
        create_fraud_agent()
    )

    print("CREATING TASK")

    task = Task(
        description=f"""
        Analyze this transaction.

        Transaction:
        {transaction}

        Fraud Policies:
        {rag_context}

        Historical Cases:
        {memory_context}

        Return:

        Fraud Score:
        Risk Level:
        Reasoning:
        Recommendation:
        """,

        expected_output=
        "Fraud analysis",

        agent=agent
    )

    print("CREATING CREW")

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    print("RUNNING CREW")

    result = str(
        crew.kickoff()
    )

    print("CREW FINISHED")

    fraud_score = (
        extract_score(
            result
        )
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
        "fraud_result":
        result,

        "fraud_score":
        fraud_score,

        "human_review":
        human_review
    }

    print("RETURNING RESULT")

    return response

# from crewai import (
#     Crew,
#     Task
# )

# from agents.fraud_agent import (
#     create_fraud_agent
# )

# from rag.retriever import (
#     FraudRetriever
# )

# from memory.adaptive_memory import (
#     AdaptiveMemory
# )

# from human_loop.review_engine import (
#     HumanReviewEngine
# )

# from crews.utils import (
#     extract_score
# )


# def analyze_transaction(
#     transaction
# ):

#     retriever = (
#         FraudRetriever()
#     )

#     memory = (
#         AdaptiveMemory()
#     )

#     rag_context = (
#         retriever.retrieve(
#             transaction
#         )
#     )

#     memory_context = (
#         memory
#         .retrieve_similar_cases(
#             transaction
#         )
#     )

#     agent = (
#         create_fraud_agent()
#     )

#     task = Task(
#         description=f"""
#         Analyze this transaction.

#         Transaction:
#         {transaction}

#         Fraud Rules:
#         {rag_context}

#         Historical Cases:
#         {memory_context}

#         Return:

#         Fraud Score:
#         Risk Level:
#         Reasoning:
#         Recommendation:
#         """,

#         expected_output=
#         "Fraud analysis",

#         agent=agent
#     )

#     crew = Crew(
#         agents=[agent],
#         tasks=[task]
#     )

#     result = str(
#         crew.kickoff()
#     )

#     score = (
#         extract_score(
#             result
#         )
#     )

#     human_review = (
#         HumanReviewEngine
#         .needs_review(
#             score
#         )
#     )

#     memory.store_case(
#         transaction,
#         result
#     )

#     return {
#         "fraud_result":
#         result,

#         "fraud_score":
#         score,

#         "human_review":
#         human_review
#     }