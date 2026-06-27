from agents.google_store_ai_agent import getPlayStoreAppRecomendations
import sys 
import asyncio 
if __name__ == "__main__" and len(sys.argv) > 1:
    query = " ".join(sys.argv[1:])
    asyncio.run(getPlayStoreAppRecomendations(query=query))