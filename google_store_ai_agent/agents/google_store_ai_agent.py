from tools.serp_tool import getProductDescriptionForPlayStoreApp, getPlayStoreApps, getAppleStoreApps, getProductStoreDescriptionForAppleStoreApp
from prompts.google_store_prompts import SYSTEM_PROMPT
from pydantic_ai import Agent 
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    system_prompt = SYSTEM_PROMPT,
    tools = [getProductDescriptionForPlayStoreApp, getPlayStoreApps, getAppleStoreApps, getProductStoreDescriptionForAppleStoreApp],
    model = "openai-chat:gpt-5.2"
)

async def getPlayStoreAppRecomendations(query : str):
    async with agent.run_stream(query) as result:
        async for token in result.stream_text(delta = True):
            print(token, end="")
