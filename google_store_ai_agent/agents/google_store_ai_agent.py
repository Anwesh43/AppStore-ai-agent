from tools.serp_tool import getPlayStoreAppDescription, getPlayStoreApps
from prompts.google_store_prompts import SYSTEM_PROMPT
from pydantic_ai import Agent 
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    system_prompt = SYSTEM_PROMPT,
    tools = [getPlayStoreAppDescription, getPlayStoreApps],
    model = "openai-chat:gpt5.1"
)

async def getPlayStoreAppRecomendations(query : str):
    async with agent.run_sync(query) as result:
        async for token in result.stream_text(delta = True):
            print(token, end="")
