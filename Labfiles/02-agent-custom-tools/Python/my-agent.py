import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
import openai

from dotenv import load_dotenv

load_dotenv()
project_endpoint = os.getenv("PROJECT_ENDPOINT")
model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

project = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential())

agent = project.agents.create_version(
    agent_name='test',
    definition=PromptAgentDefinition(
        model=model_deployment,
        instructions='answer in Japanese'
    )
)
print(f"Agent created (id: {agent.id}, name: {agent.name}, version: {agent.version})")

openai = project.get_openai_client()

conversation = openai.conversations.create()

response = openai.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": agent.name, "type": "agent_reference"}},
    input='what is the capital in Japan?'
)
print(response.output_text)