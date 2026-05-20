# from crewai import (
#     Crew,
#     Task
# )

# from agents.credit_risk_agent import (
#     create_credit_agent
# )

# from rag.retriever import (
#     FraudRetriever
# )

# from memory.adaptive_memory import (
#     AdaptiveMemory
# )


# def analyze_credit(
#     customer_data
# ):

#     retriever = (
#         FraudRetriever()
#     )

#     memory = (
#         AdaptiveMemory()
#     )

#     rag_context = (
#         retriever.retrieve(
#             customer_data
#         )
#     )

#     memory_context = (
#         memory
#         .retrieve_similar_cases(
#             customer_data
#         )
#     )

#     agent = (
#         create_credit_agent()
#     )

#     task = Task(
#         description=f"""
#         Analyze customer
#         credit risk.

#         Customer Data:
#         {customer_data}

#         Credit Policies:
#         {rag_context}

#         Historical Cases:
#         {memory_context}

#         Return:

#         Credit Risk:
#         Confidence:
#         Default Probability:
#         Recommendation:
#         Reasoning:
#         """,

#         expected_output="""
#         Credit risk report
#         """,

#         agent=agent
#     )

#     crew = Crew(
#         agents=[agent],
#         tasks=[task],
#         verbose=True
#     )

#     result = (
#         crew.kickoff()
#     )

#     memory.store_case(
#         customer_data,
#         str(result)
#     )

#     return str(result)
print("CREDIT CREW STEP 1")

from crewai import (
    Crew,
    Task
)

print("CREDIT CREW STEP 2")

from agents.credit_risk_agent import (
    create_credit_agent
)

print("CREDIT CREW STEP 3")


# TEMP MOCKS
# reconnect real memory/rag later


class FraudRetriever:

    def retrieve(
        self,
        query
    ):

        print(
            "CREDIT RAG CALLED"
        )

        return """
        Customers with
        credit score below 600
        are high risk.

        Debt ratio above 0.5
        indicates repayment risk.

        Stable income
        lowers risk.
        """


class AdaptiveMemory:

    def retrieve_similar_cases(
        self,
        customer_data
    ):

        print(
            "CREDIT MEMORY"
        )

        return [
            """
            Similar customer:
            score 580,
            debt ratio 0.62,
            manual review triggered.
            """
        ]

    def store_case(
        self,
        customer_data,
        result
    ):

        print(
            "CREDIT MEMORY STORED"
        )


print("CREDIT CREW STEP 4")


def analyze_credit(
    customer_data
):

    print(
        "START CREDIT ANALYSIS"
    )

    retriever = (
        FraudRetriever()
    )

    memory = (
        AdaptiveMemory()
    )

    print(
        "GET CREDIT RAG"
    )

    rag_context = (
        retriever.retrieve(
            customer_data
        )
    )

    print(
        "GET CREDIT MEMORY"
    )

    memory_context = (
        memory
        .retrieve_similar_cases(
            customer_data
        )
    )

    memory_context = (
        "\n".join(
            memory_context
        )
        if memory_context
        else
        "No history"
    )

    print(
        "CREATE CREDIT AGENT"
    )

    agent = (
        create_credit_agent()
    )

    print(
        "CREATE CREDIT TASK"
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

    Return response ONLY in this format:

    ## Credit Risk Assessment

    **Risk Level:** LOW | MEDIUM | HIGH

    **Confidence Score:** %
    
    **Default Probability:** %

    **Recommendation:**
    APPROVE | REVIEW | REJECT

    ## Risk Factors
    - factor 1
    - factor 2
    - factor 3

    ## Reasoning
    Explain in concise way.

    ## Final Decision
    Short summary.
    """,

    expected_output=
    "Structured markdown report",

    agent=agent
    )

    print(
        "CREATE CREDIT CREW"
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    print(
        "RUN CREDIT CREW"
    )

    result = (
        crew.kickoff()
    )

    print(
        "CREDIT CREW DONE"
    )

    memory.store_case(
        customer_data,
        str(result)
    )

    return {
        "credit_result":
        str(result),

        "status":
        "success"
    }