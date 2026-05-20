from crewai import Task, Crew
from agents.test_agent import create_test_agent

def run_test_crew(user_input):

    agent = create_test_agent()

    task = Task(
        description=f"""
        Analyze this banking input:

        {user_input}

        Give a short explanation.
        """,
        expected_output="Short banking analysis",
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    result = crew.kickoff()

    return str(result)