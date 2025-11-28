from google.adk.agents import Agent
from google.adk.tools import google_search

recommendation_agent = Agent(
    name="recommendation_agent",
    model="gemini-2.0-flash-exp",
    description="Agent that generates actionable troubleshooting and optimization recommendations.",
    instruction="Use Google Search for latest firmware, bug fixes and community solutions.",
    tools=[google_search]
)
