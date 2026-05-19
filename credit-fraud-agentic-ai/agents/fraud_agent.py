from crewai import Agent
from config.settings import (
    OPENAI_API_KEY,
    MODEL_NAME
)

llm = LLM(
    model=MODEL_NAME,
    api_key=OPENAI_API_KEY
)

def create_fraud_agent():

    return Agent(
        role="""
        Senior Banking Fraud
        Detection Specialist
        """,

        goal="""
        Detect fraudulent banking
        transactions using
        fraud policies,
        historical memory,
        behavioral signals,
        and intelligent reasoning.
        """,

        backstory="""
        You are an expert fraud
        investigator specializing in:

        - AML
        - Banking fraud
        - Transaction anomalies
        - Device fraud
        - Behavioral analysis
        - Explainable fraud decisions

        You always justify
        your reasoning.
        """,

        verbose=True,

        allow_delegation=False
    )