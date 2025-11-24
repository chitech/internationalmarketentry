from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from market_entry_agent.config import DEFAULT_MODEL, RETRY_CONFIG, SUMMARY_INSTRUCTION


def create_summary_agent() -> Agent:
    """Create the summary agent.
    
    Returns:
        Agent configured to synthesize research findings.
    """
    return Agent(
        name="SummaryAgent",
        model=Gemini(
            model=DEFAULT_MODEL,
            retry_options=RETRY_CONFIG
        ),
        instruction=SUMMARY_INSTRUCTION,
        tools=[],  # No tools needed - synthesizes existing findings
        output_key="final_report",
    )