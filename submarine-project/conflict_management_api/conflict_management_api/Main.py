from Registry import locationService, crateService
import jsonpickle
# Make sure to do a `pip install jsonpickle` if you don't already have it
def main():
    print('Start of the program')
    print('Initializing')
    initializer()
    
    # Using jsonpickle here to encode the location objects as JSON so it looks decent when we print it.
    # NOTE: This is just test code so we can ensure this works in place of setting up integration tests
    # This will get a single location, get all the crates at that location, look at their destination, and
    # transfer the crates to that destination
    location_id = locationService.get_all_locations()[0].id
    cratesatlocation = crateService.getcratesbylocation(location_id)
    cratesStored = []
    for crate in cratesatlocation:
         cratesStored.append(crateService.storeinstoragecontainer(crate, locationService))
    print(jsonpickle.encode(cratesStored, unpicklable=False))

def initializer():
    # Referential Data
    locationService.get_all_locations()
    crateService.getallcrates()
    # __private_variable = ''
    # _protected_variable = ''
    # another_variable = ''

if __name__ == '__main__':
    main()

# main()