from services.base_http_client import BaseHTTPClient
import os 
from dotenv import load_dotenv 

load_dotenv()

class SerpService:
    def __init__(self):
        self.client = BaseHTTPClient(baseURL=os.environ["SERP_BASE_URL"])
        self.googleProductIdDescriptionMap = {}
        self.appleProductIdDescriptionMap = {}
        


    def getPlayStoreApps(self, query : str):
        queryDict = {
            "engine": "google_play",
            "q": query,
            "api_key": os.environ["SERP_API_KEY"]
        }
        try:
            dataJSON = self.client.getCall(endpoint = "search", data = queryDict)
            result = []
            for k, v in dataJSON.items():
                print("KEY", k)
            print("organic_results" in dataJSON, "items" in dataJSON["organic_results"])
            #print("DATAJSON", dataJSON)
            if "organic_results" in dataJSON and len(dataJSON["organic_results"]) > 0:
               
                if "items" in dataJSON["organic_results"][0]:
                    print("ITEMS", dataJSON["organic_results"][0]["items"][0])
                    for data in dataJSON["organic_results"][0]["items"]:
                        resultDict = {}
                        for k, v in data.items():
                            if not (k == "description"):
                                resultDict[k] = v
                            else:
                                self.googleProductIdDescriptionMap[data["product_id"]] = data["description"]
                        result.append(resultDict)
            return result 
        except Exception as e:
            print("Error", e)
            return {}

    def getProductDescriptionForPlayStoreApp(self, productId : str):
        if not(productId in self.googleProductIdDescriptionMap):
            return {
                "status": "not found in productIdMap",
                "nextSteps": "Please call getPlayStoreApps with appropriate query, then call getProductDescription with product_id"
            }
        return {
            "result": self.googleProductIdDescriptionMap[productId]
        }
    
    def getAppleStoreApps(self, query : str):
        result = []
        queryDict = {
            "engine": "apple_app_store",
            "q": query,
        }
        response = self.client.getCall("search", queryDict)
        keysMap = {
            "description": True, 
            "screenshots": True,
            "supported_devices": True, 
            "logos": True,  
        }
        if "organic_results" in response:
            organicResults = response["organic_results"]
            respDict = {}
            for data in organicResults:
                for k, v in data.items():
                    if k not in keysMap:
                        respDict[k] = v
                    elif k == "description":
                        self.appleProductIdDescriptionMap[str(k["description"])] = v 
            result.append(respDict)
        return result 
    

    def getProductStoreDescriptionForAppleStoreApp(self, productId : str):
        if not(productId in self.appleProductIdDescriptionMap):
            return {
                "status": "not found in productIdMap",
                "nextSteps": "Please call getPlayStoreApps with appropriate query, then call getProductDescription with product_id"
            }
        return {
            "result": self.appleProductIdDescriptionMap[productId]
        }



                        

