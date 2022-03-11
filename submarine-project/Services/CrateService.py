import requests
import jsonpickle
from Models import Crate

class CrateService():
    all_crates = []
    
    def getcratenumbersfromAPI(self):
        apiaddress = 'https://my.api.mockaroo.com/spoon-newman-crate-ids.json'
        headers = {'X-API-Key': 'cf7bbbd0'}
        data = requests.get(apiaddress, headers=headers)
        return data.json()

    def getallcrates(self):
        print('Currently processing crates')
        crates = self.getcratenumbersfromAPI()
        listOfCrateObjects = []
        # Map the raw data to the crates
        for crate_data in crates:
            crateObj = Crate(crate_data['id'], crate_data['weight'], crate_data['height'], crate_data['material'], crate_data['assigned_crewman_id'], crate_data['load_time_elapsed'], crate_data['source_id'], crate_data['destination_id'], crate_data['is_volatile'], crate_data['is_quarantined'], crate_data['required_machinery'], crate_data['current_location'])
            self.all_crates.append(crateObj)
        return self.all_crates
    
    def getcratesbylocation(self, locationid):
        cratesatlocation = []
        for crate in self.all_crates:
            if crate.current_location == locationid:
                cratesatlocation.append(crate)

        return cratesatlocation

    def storeinstoragecontainer(self, item, locationService) -> bool:
        list_of_storage_containers = locationService.getlocationbygroup('Storage')
        # print(len(list_of_storage_containers), jsonpickle.encode(list_of_storage_containers, unpicklable=False))
        return self.transferCrateToDestination(item, list_of_storage_containers)

    def transferCrateToDestination (self, item, list_of_locations_in_group):
        # We need to know which storage container
        # We want the Crate's `current_location` to equal the `destination_id`
        # We want to look through the location_group to see which location has capacity
        # for us to put the crate inside
        item.current_location = list_of_locations_in_group[0].id
        return item

    def quarantineitem(self, item) -> bool:
        return True
        # we assume this operation succeeds

    def senditemtoadmiral(self, item) -> bool:
        print('Sending crate to admiral...')
        # same thing as last time

    def sendtodistribution(self, item) -> bool:
        print('Sending container to distribution...')
        # if this fails item needs to be quarantined
