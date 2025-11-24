"""Legal research sub-agent."""

from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from market_entry_agent.config import DEFAULT_MODEL, RETRY_CONFIG, LEGAL_RESEARCH_INSTRUCTION


def create_legal_research_agent() -> Agent:
    """Create the legal research agent.
    
    Returns:
        Agent configured for legal/visa research using Google Search.
    """
    return Agent(
        name="LegalResearchAgent",
        model=Gemini(
            model=DEFAULT_MODEL,
            retry_options=RETRY_CONFIG
        ),
        instruction=LEGAL_RESEARCH_INSTRUCTION,
        tools=[google_search],
        output_key="legal_findings",
    )