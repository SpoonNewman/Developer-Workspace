import requests
from Models import Crate

class crate_service():
    def getcratenumbers(self):
        apiaddress = 'https://my.api.mockaroo.com/spoon-newman-crate-ids.json'
        headers = {'X-API-Key': 'cf7bbbd0'}
        data = requests.get(apiaddress, headers=headers)
        return data.json()

    def processcrates(self):
        print('Currently processing crates')
        crates = self.getcratenumbers()
        listOfCrateObjects = []
        for crate_data in crates:
            crateObj = Crate(crate_data['id'], crate_data['weight'], crate_data['height'], crate_data['material'], crate_data['assigned_crewman_id'], crate_data['load_time_elapsed'], crate_data['source_id'], crate_data['destination_id'], crate_data['is_volatile'], crate_data['is_quarantined'], crate_data['require'])
            listOfCrateObjects.push(crateObj)

    def storeinstoragecontainer(self, item) -> bool:
        print('Storing Crate into Storage Container...') 
        # if this fails we want to quarantine the item

    def quarantineitem(self, item) -> bool:
        return True
        # we assume this operation succeeds

    def senditemtoadmiral(self, item) -> bool:
        print('Sending crate to admiral...')
        # same thing as last time

    def sendtodistribution(self, item) -> bool:
        print('Sending container to distribution...')
        # if this fails item needs to be quarantined
