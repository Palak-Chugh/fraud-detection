from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="gpt-4o-mini",
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def create_fraud_agent():

    return Agent(
        role="Senior Fraud Detection Specialist",

        goal="""
        Detect fraudulent
        banking transactions
        and explain risk.
        """,

        backstory="""
        Expert banking fraud
        investigator trained
        in anomaly detection,
        AML, suspicious activity,
        device fraud,
        and behavioral analysis.
        """,

        llm=llm,

        verbose=True,

        allow_delegation=False
    )