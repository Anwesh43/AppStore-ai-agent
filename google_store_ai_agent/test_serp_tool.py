from tools.serp_tool import getPlayStoreAppDescription, getPlayStoreApps
import json 
import time 
from typing import Dict 
import sys 
def saveFile(result : Dict, fileName : str):
    with open(fileName, "w") as f:
        f.write(json.dumps(result))

def test(query : str):
    result = getPlayStoreApps(query)
    saveFile(result, "playstoreAppDescription.json")
    print("Got result for apps")
    time.sleep(1)
    if len(result) > 0:
        productDescription = getPlayStoreAppDescription(result[0]["product_id"])
        saveFile(productDescription, f"product_{result[0]["product_id"]}.json")
        print("Got App results")


if __name__ == "__main__" and len(sys.argv) == 2:
    test(sys.argv[1])