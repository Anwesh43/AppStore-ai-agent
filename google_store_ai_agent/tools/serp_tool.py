from services.serp_service import SerpService 

serpService = SerpService()

def getPlayStoreApps(query : str):
    print(f"Calling getPlayStoreApps toll {query}")
    return serpService.getPlayStoreApps(query=query)

def getProductDescriptionForPlayStoreApp(productId : str):
    print(f"Calling getPlayStoreAppDescription {productId}")
    return serpService.getProductDescriptionForPlayStoreApp(productId=productId)

