from crewai import Agent
def create_agent():
    return Agent(role='GitRealAudit', goal='Autonomous Commercial Real Estate Cap Rate, Lease Escalation & Net Operating Income (NOI) Agent', backstory='Autonomous agent', verbose=True)
