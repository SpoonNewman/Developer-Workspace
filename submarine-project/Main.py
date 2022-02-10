from Services import LocationService

def main():
    print('Start of the program')
    # crate_service.processcrates()
    locationService = LocationService()
    locationService.get_all_locations()

if __name__ == '__main__':
    main()

# main()