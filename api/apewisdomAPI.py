import requests
import json
import pandas as pd

class ApiWisdom:
    def __init__(self):
        pass

    def getData(self, url):
        response = requests.get(url)
        res = json.loads(response.text)
        result = []

        for values in res['results']:
            result.append(values['ticker'].replace('.X',''))

        return result

    def __del__(self):
        pass

API = ApiWisdom()
url = "https://apewisdom.io/api/v1.0/filter/all-crypto/page/1"
topCrypto = API.getData(url)
print(topCrypto)
