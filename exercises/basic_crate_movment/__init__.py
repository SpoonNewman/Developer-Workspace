
import json
# from enum import Enum
# class CrateLocation(Enum):    
#     PRIMARY = "Mess Hall"
#     SECONDARY = "Barracks"
#     AUXILIARY = "Shitty Bathroom"
#     IN_TRANSIT = "Currently being transported"
configfile = open("configuration.json")
CrateLocation = json.load(configfile)["Crate_Locations"]
class Crate:

    Owner = "Johnson"
    def __init__(self, id_number: str, location: str, x_size: int = 50, height_size: int = 50, cargo = [""]):
        self.id = id_number
        self.location = location
        self.x_size = x_size
        self.y_size = height_size
        self.validate_size_of_crate()
        self.cargo = cargo


    # we need to make sure that if Location 3 is set then height_size cannot be more than 25 and x_size 32
    def validate_size_of_crate (self):
        if self.location == CrateLocation["AUXILIARY"]:
            self.self_check(Max_xvalue= 25, Max_yvalue= 32)
        if self.location == CrateLocation['PRIMARY']:
            self.self_check(Max_xvalue= 50, Max_yvalue= 200)
        if self.location == CrateLocation['SECONDARY']:
            self.self_check(Max_xvalue= 25, Max_yvalue= 25)
    def self_check(self, Max_xvalue, Max_yvalue):
        try:
            assert self.y_size <= Max_yvalue and self.x_size <= Max_xvalue, "The crate won't fit you dumb bitch"
        except AssertionError:
            raise ValueError(f"The value of the height_size and x_size is greater than we can handle. Please fix it")
        except Exception:
            raise Exception("Unexpected item in the bagging area, can't compute.")


some_crate = Crate(height_size=25, x_size=25, id_number="someId", location=CrateLocation['SECONDARY'], cargo = ["Iphone 14 pro"])
another_crate = Crate(height_size=15, x_size=15, id_number="1231231", location=CrateLocation['OTHER'], cargo = ["Mobi Huge"])

list_of_crates: list[Crate] = []
list_of_crates.append(some_crate)

def move_create_to_room (crate: Crate, location: str):
    crate.location = location
    print(f"Crate is currently being rerouted: {location}")
    
def destruction(crate: Crate):
    crate.x_size = 0
    crate.y_size = 0

def cargo_manifest(crate: Crate):
    for item in crate.cargo:
        print(item)

move_create_to_room(some_crate, CrateLocation['IN_TRANSIT'])
move_create_to_room(some_crate, CrateLocation['PRIMARY'])
move_create_to_room(some_crate, CrateLocation['OTHER'])
destruction(some_crate)
cargo_manifest(some_crate)
cargo_manifest(another_crate)
print("Crate has reached its destination")
print("By the way wyoming isnt a real place say goodbye to all of your materials")
configfile.close()


# TODO:
# FINISHED make a function and additional location to move the the crate to the new location "OTHER"
# FINISHED make a function to destroy the crate by setting it's x_size and height_size to 0
# FINISHED Modify the Crate class to have a property called "cargo" that should be a list of strings.
# FINISHED For example, we should be able to set cargo on a crate and retrieve the cargo by doing something like self.cargo or some_crate.cargo
# FINISHED make a function that returns the cargo list from a crate. Refer to the `move_create_to_room()` for inspiration on how to do this.