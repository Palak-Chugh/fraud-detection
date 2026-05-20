from crewai import Agent

def create_test_agent():
    return Agent(
        role="Banking AI Assistant",
        goal="Help analyze banking transactions",
        backstory=(
            "You are a banking assistant helping "
            "analyze financial transactions."
        ),
        verbose=True
    )