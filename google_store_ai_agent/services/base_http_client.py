import requests 
from urllib.parse import urlencode 
from typing import Dict 

class BaseHTTPClient:
    def __init__(self, baseURL : str):
        self.baseURL = baseURL

    def getCall(self, endpoint : str, data : Dict):
        qs = urlencode(data)
        response = requests.get(f"{self.baseURL}/{endpoint}?{qs}")
        response.raise_for_status()
        return response.json()