from crewai import Agent


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

        verbose=True,

        allow_delegation=False
    )