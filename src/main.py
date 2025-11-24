"""Simple launcher for the Market Entry Agent using uvicorn."""
import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

if __name__ == "__main__":
    import uvicorn
    from google.adk.cli.adk_web_server import AdkWebServer
    from google.adk.sessions import InMemorySessionService
    from google.adk.memory import InMemoryMemoryService
    from google.adk.artifacts import InMemoryArtifactService
    from google.adk.credentials import InMemoryCredentialService
    from google.adk.evals import EvalSetsManager, EvalSetResultsManager
    from market_entry_agent.agent import root_agent
    from google.adk.common import AgentLoaderImpl

    # Create the web server
    web_server = AdkWebServer(
        agent_loader=AgentLoaderImpl(root_agent),
        session_service=InMemorySessionService(),
        memory_service=InMemoryMemoryService(),
        artifact_service=InMemoryArtifactService(),
        credential_service=InMemoryCredentialService(),
        eval_sets_manager=EvalSetsManager(),
        eval_set_results_manager=EvalSetResultsManager(),
        agents_dir=project_root,
    )

    uvicorn.run(web_server.app, host="127.0.0.1", port=8000)
