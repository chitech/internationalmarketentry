"""Main market entry research agent coordinator."""

from google.adk.agents import SequentialAgent
from market_entry_agent.sub_agents import (
    create_market_research_agent,
    create_legal_research_agent,
    create_summary_agent,
)


def create_market_entry_agent() -> SequentialAgent:
    """Create the main market entry research agent.
    
    This agent coordinates three sub-agents in sequence:
    1. Market Research Agent - Gathers market intelligence
    2. Legal Research Agent - Identifies legal/visa requirements
    3. Summary Agent - Synthesizes findings into actionable report
    
    Returns:
        SequentialAgent configured with all sub-agents.
    """
    # Create sub-agents
    market_agent = create_market_research_agent()
    legal_agent = create_legal_research_agent()
    summary_agent = create_summary_agent()
    
    # Create sequential coordinator
    return SequentialAgent(
        name="MarketEntryResearchPipeline",
        sub_agents=[
            market_agent,
            legal_agent,
            summary_agent
        ],
    )


# Export the main agent
root_agent = create_market_entry_agent()