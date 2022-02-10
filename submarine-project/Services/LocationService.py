import requests
from Models import Location

class LocationService():
    ############## 0. Fix the area capacities to be the `base-locations`
    # 1. Set a property to hold all the locations - This will be our in-memory state
    # 2. Flesh out `getLocationId()` to grab a specific location out of the list of locations
    # 3. Implement ability to get locations by group
    # 4. Add a property on the Location model of `list_of_crates_at_location`
    # 5. Implement the `isLocationCapacityAvailable(location_id: string)` which will look at the number of current cates,
    #   the number of crates we're trying to add, and max capacity. This function will return
    #   a boolean that determines whether the location has existing capacity.
    #   This function will take in a parameter of `location_id` which will be used with `getLocationById`
    #   Class is blueprint, instance is object (product of blueprint) oop
    all_locations = []
    
    def getlocations(self):
        apiaddress = 'https://my.api.mockaroo.com/base-locations.json'
        headers = {'X-API-Key': 'cf7bbbd0'}
        data = requests.get(apiaddress, headers=headers)
        return data.json()
    
    def getlocationid(self, keyword):
        return 'to be defined'
    
    def get_all_locations(self):
        locations = self.getlocations()
        for location in locations:
            self.all_locations.append(Location(location['id'], location['number_of_crates'], location['max_capacity_of_crates'], location['name'], location['group']))
        print(self.all_locations)