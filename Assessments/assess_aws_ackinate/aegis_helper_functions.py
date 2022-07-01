import requests
import json

def get_iam_policies() -> list[dict]:
    apiaddress = 'https://my.api.mockaroo.com/pariah-iam-policies.json'
    headers = {'X-API-Key': 'cf7bbbd0'}
    data = requests.get(apiaddress, headers=headers)
    return data.json()