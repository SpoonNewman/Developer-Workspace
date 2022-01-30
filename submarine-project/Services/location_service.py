import requests

class location_service():
    def getlocations(self):
        apiaddress = 'https://my.api.mockaroo.com/spoon-newman-crate-ids.json'
        headers = {'X-API-Key': 'cf7bbbd0'}
        data = requests.get(apiaddress, headers=headers)
        return data.json()
    
    def getlocationid(self, keyword):
        return 'to be defined'