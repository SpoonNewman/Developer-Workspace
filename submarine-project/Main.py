from Registry import locationService
import jsonpickle
# Make sure to do a `pip install jsonpickle` if you don't already have it

def main():
    print('Start of the program')
    # crate_service.processcrates()
    
    # Using jsonpickle here to encode the location objects as JSON so it looks decent when we print it.
    locations = jsonpickle.encode(locationService.get_all_locations(), unpicklable=False)
    print(locations)

if __name__ == '__main__':
    main()

# main()