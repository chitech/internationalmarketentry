"""Configuration for market entry research agents."""

import os
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is required")

# Model Configuration
DEFAULT_MODEL = "gemini-2.5-flash-lite"

# Retry Configuration
RETRY_CONFIG = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

# Agent Configuration
MARKET_RESEARCH_INSTRUCTION = """You are a market research specialist.

Use google_search to find exactly 3 key facts about:
1. Target market size and purchasing power in Miami/South Florida
2. E-commerce or industry-specific competition landscape
3. Business opportunities for international companies in the sector

Output: Bullet points only. Max 150 words total. Include source links."""

LEGAL_RESEARCH_INSTRUCTION = """You are a business law specialist.

Use google_search to find for the entrepreneur's country of origin:
1. Best visa option (E-2, L-1, or other)
2. Recommended business entity (LLC vs C-Corp)
3. Key requirements for foreign-owned business in Florida

Output: Bullet points only. Max 100 words total. Include source links."""

SUMMARY_INSTRUCTION = """Create a brief market entry report.

Read market_findings and legal_findings from the session state.

Output format (MAX 300 words total):
- Executive Summary (2 sentences)
- Top 3 Opportunities (bullet points)
- Top 3 Challenges (bullet points)
- Recommended First Steps (3 steps)
- Estimated Timeline (1 sentence)

Be concise and actionable."""