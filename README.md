# 🌎 International Market Entry Research Agent

Multi-agent system helping international entrepreneurs research US market entry opportunities via Miami.

## Overview

This agent automates comprehensive market entry research that traditionally takes 2-3 weeks, delivering results in minutes. Built with Google's Agent Development Kit (ADK), it uses sequential multi-agent coordination to gather, analyze, and synthesize market intelligence.

## Features

- **Market Research Agent**: Gathers real-time data on target markets, competition, and opportunities
- **Legal Requirements Agent**: Identifies visa options, business formation needs, and regulatory requirements
- **Summary Agent**: Synthesizes findings into actionable market entry reports

## Technical Stack

- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash Lite
- Google Search integration
- Sequential multi-agent architecture

## Requirements

- Python 3.11+
- Google AI API key
- ADK dependencies (see requirements.txt)

## Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/international-market-entry-agent.git
cd international-market-entry-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

## Usage
```bash
# Run the agent
python src/main.py
```

## Example Output

See `examples/sample_output.md` for a complete example of agent research results.

## Capstone Project

This project was developed for the Google AI Agents Intensive Capstone (November 2025).

**Concepts Demonstrated:**
- Multi-agent systems (sequential coordination)
- Tool integration (Google Search)
- Sessions & Memory management
- Real-world business application

## Business Value

- **Time Savings**: 2-3 weeks → 10 minutes
- **Cost Savings**: $2,000+ in consulting fees per research
- **Target Market**: International entrepreneurs entering US via Miami
- **Scalability**: Can serve hundreds of entrepreneurs annually

## License

MIT License

## Author

Christine Brown Clayton
- Microsoft AI-102 Certified
- Unieros Tech Services
- [tech.unieros.com](https://tech.unieros.com)
 
## Running locally (development)

- **Activate virtualenv**: `source venv/bin/activate`
- **Install dependencies**: `pip install -r requirements.txt`
- **Run the app (development)**: `python src/main.py`
- **Or with auto-reload**: `uvicorn src.main:app --reload`

Open `http://127.0.0.1:8000` in your browser; POST to `/run` to trigger the pipeline (see `src/main.py`).

## GitHub

- This repository includes a basic CI workflow at `.github/workflows/ci.yml` that performs an import check.
- Add the project to GitHub and push your initial commit using the commands below (adjust remote creation to your preferred method):

```bash
git init
git add .
git commit -m "Initial project import"
# Create GitHub repo (using gh CLI) and push, or create the repo on the website and add the remote.
gh repo create YOUR_USERNAME/international-market-entry-agent --public --source=. --remote=origin
git push -u origin main
```