from crewai import Agent


def create_fraud_agent():

    return Agent(
        role="Senior Fraud Detection Analyst",

        goal="""
        Detect suspicious transactions,
        identify fraud risk,
        and explain reasoning.
        """,

        backstory="""
        You are an expert banking fraud
        investigator trained in anomaly
        detection, behavioral analysis,
        suspicious patterns, AML,
        and fraud prevention.
        """,

        verbose=True,

        allow_delegation=False
    )