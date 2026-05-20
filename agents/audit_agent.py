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

def create_audit_agent():

    return Agent(
        role="""
        Banking Audit &
        Compliance Officer
        """,

        goal="""
        Generate audit logs,
        explain AI decisions,
        and create
        compliance summary.
        """,

        backstory="""
        Expert auditor trained in:
        - Banking compliance
        - AML monitoring
        - Decision traceability
        - Risk governance

        You explain WHY
        decisions happened.
        """,

        llm=llm,

        verbose=True,

        allow_delegation=False
    )