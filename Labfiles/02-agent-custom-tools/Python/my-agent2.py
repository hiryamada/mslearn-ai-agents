import asyncio

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity import DefaultAzureCredential   
from dotenv import load_dotenv
import os

load_dotenv()
project_endpoint = os.getenv("PROJECT_ENDPOINT")
model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

async def main() -> None:
    client = FoundryChatClient(
        project_endpoint=project_endpoint,
        model=model_deployment,
        credential=DefaultAzureCredential()
    )
    agent = Agent(
        client=client,
        name="TestAgent",
        instructions="answer in Japanese"
    )
    result = await agent.run("What is the capital of France?")
    print(f"Agent: {result}")

if __name__ == "__main__":
    asyncio.run(main())