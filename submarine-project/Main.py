from Registry import locationService, crateService
import jsonpickle
# Make sure to do a `pip install jsonpickle` if you don't already have it
def main():
    print('Start of the program')
    print('Initializing')
    initializer()
    
    # Using jsonpickle here to encode the location objects as JSON so it looks decent when we print it.
    location_id = locationService.get_all_locations()[0].id
    # .get_all_locations -> [...]
    # len(someList) -> number of elements in the list
    # print(len(locationService.get_all_locations()))
    cratesatlocation = crateService.getcratesbylocation(location_id)
    cratesStored = []
    for crate in cratesatlocation:
         cratesStored.append(crateService.storeinstoragecontainer(crate, locationService))
    print(jsonpickle.encode(cratesStored, unpicklable=False))

def initializer():
    locationService.get_all_locations()
    crateService.getallcrates()

if __name__ == '__main__':
    main()

# main()