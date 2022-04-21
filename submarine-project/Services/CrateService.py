import requests
import jsonpickle
from Models import Crate, Location

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

    def transferCrateToDestination (self, crate: Crate, list_of_locations_in_group: list[Location]) -> bool:
        """
        Transfer crate to a destination within a certain group. This method will analyze
        and figure out which location within the destination group has capacity and transfer the crate
        to that destination.

        Args:
            item (Crate): A crate object that we are transferring to a location
            list_of_locations_in_group (list[Location]): A list of locations that our crate can be transferred to

        Returns:
            bool: A status of the result of attemping to transfer the crate to a destination
        """
        
        destination: Location | None = self._get_storage_location_by_capacity(list_of_locations_in_group)
        status_result: bool = self._transfer_crate(crate, destination)
        return status_result
        
    def _transfer_crate(crate: Crate, destination: Location) -> bool:
        # change current location to destination
        result = False
        if (crate.current_location is not destination.id):
            # Transfer the crate
            crate.current_location = destination.id
            if (crate not in destination.listofcratesatlocation):
                destination.listofcratesatlocation.append(crate)
                destination.number_of_crates = destination.number_of_crates + 1 

                result = True
        return result

    def _get_storage_location_by_capacity(list_of_locations: list[Location]) -> Location | None:
        # NOTE: We are treating number of crates and max_capacity_crates in units of 1.
        # In effect, a crate that is 30'x30' counts for one unit.
        # A crate that is 1'x1' counts as one unit.
        # No matter the size or properties of a crate it is treated as one unit
        for location in list_of_locations:
            if location.number_of_crates < location.max_capacity_crates: 
                return location

        return None
        

    def quarantineitem(self, item) -> bool:
        return True
        # we assume this operation succeeds

    def senditemtoadmiral(self, item) -> bool:
        print('Sending crate to admiral...')
        # same thing as last time

    def sendtodistribution(self, item) -> bool:
        print('Sending container to distribution...')
        # if this fails item needs to be quarantined
