from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from market_entry_agent.config import DEFAULT_MODEL, RETRY_CONFIG, MARKET_RESEARCH_INSTRUCTION


def create_market_research_agent() -> Agent:
    """Create the market research agent.
    
    Returns:
        Agent configured for market research using Google Search.
    """
    return Agent(
        name="MarketResearchAgent",
        model=Gemini(
            model=DEFAULT_MODEL,
            retry_options=RETRY_CONFIG
        ),
        instruction=MARKET_RESEARCH_INSTRUCTION,
        tools=[google_search],
        output_key="market_findings",
    )