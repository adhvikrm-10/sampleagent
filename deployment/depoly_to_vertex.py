import os
import vertexai
from vertexai import agent_engines
from dotenv import load_dotenv
load_dotenv()

def deploy_agent():
    vertexai.init(project=os.getenv("GOOGLE_CLOUD_PROJECT"), location=os.getenv("GOOGLE_CLOUD_LOCATION"), staging_bucket=os.getenv("STAGING_BUCKET"))
    from agents.root_agent import root_agent
    remote_agent = agent_engines.create(agent_engine=root_agent, requirements=["google-adk"], config={"display_name":"IoT Health Monitor"})
    print(f"Deployment successful: {remote_agent.resource_name}")
    return remote_agent

if __name__ == "__main__":
    deploy_agent()
