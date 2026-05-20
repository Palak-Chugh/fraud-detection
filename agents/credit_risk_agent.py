# from crewai import Agent


# def create_credit_agent():

#     return Agent(
#         role="""
#         Senior Credit Risk Analyst
#         """,

#         goal="""
#         Assess customer
#         creditworthiness
#         and predict
#         financial risk.
#         """,

#         backstory="""
#         Expert banking analyst
#         specializing in
#         loan default prediction,
#         credit scoring,
#         and repayment behavior.
#         """,

#         verbose=True,

#         allow_delegation=False
#     )
from crewai import (
    Agent,
    LLM
)

from dotenv import (
    load_dotenv
)

import os

load_dotenv()

print("CREDIT AGENT LOADING")


llm = LLM(
    model="gpt-4o-mini",
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def create_credit_agent():

    print(
        "CREATING CREDIT AGENT"
    )

    return Agent(
        role=
        "Senior Credit Risk Analyst",

        goal="""
        Assess customer
        creditworthiness
        and financial risk.
        """,

        backstory="""
        Expert banking
        credit analyst
        specialized in:

        - loan risk
        - repayment analysis
        - debt ratio
        - customer risk profiling
        - financial behavior
        """,

        llm=llm,

        verbose=True,

        allow_delegation=False
    )