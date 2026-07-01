from services.serp_service import SerpService 

serpService = SerpService()

def getPlayStoreApps(query : str):
    print(f"Calling getPlayStoreApps toll {query}")
    return serpService.getPlayStoreApps(query=query)

def getProductDescriptionForPlayStoreApp(productId : str):
    print(f"Calling getPlayStoreAppDescription {productId}")
    return serpService.getProductDescriptionForPlayStoreApp(productId=productId)

def getAppleStoreApps(query : str):
    print(f"Calling getAppleStoreApps tool {query}")
    return serpService.getAppleStoreApps(query=query)

def getProductStoreDescriptionForAppleStoreApp(productId : str):
    print(f"Calling getProductStoreDescriptionForAppleStoreApp tool {product_id}")
    return serpService.getProductStoreDescriptionForAppleStoreApp(productId=productId)