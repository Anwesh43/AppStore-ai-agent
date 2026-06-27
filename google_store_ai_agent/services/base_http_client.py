import requests 

class BaseHTTPClient:
    def __init__(self, baseURL : str):
        self.baseURL = baseURL

    def getCall(self, endpoint : str):
        response = requests.get(f"{self.baseURL}/{endpoint}")
        response.raise_for_status()
        return response.json()