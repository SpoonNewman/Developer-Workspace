from enum import Enum
class CrateLocation(Enum):    
    PRIMARY = "dock",
    SECONDARY = "barracks",
    AUXILIARY = "Shitty Bathroom"

class Crate:
    def __init__(self, id_number: str, location: CrateLocation = CrateLocation.PRIMARY, x_size: int = 50, y_size: int = 50):
        self.id = id_number
        self.location = location
        self.x_size = x_size
        self.y_size = y_size
        self.validate_size_of_crate()

    # we need to make sure that if Location 3 is set then y_size cannot be more than 25 and x_size 32
    def validate_size_of_crate (self):
        if self.location == CrateLocation.AUXILIARY:
            try:
                assert self.y_size <= 25 and self.x_size <= 32, "The crate won't fit you dumb bitch"
            except AssertionError:
                raise ValueError(f"The value of the y_size and x_size is greater than we can handle. Please fix it")
            except Exception:
                raise Exception("Unexpected item in the bagging area, can't compute.")
        if self.location == CrateLocation.PRIMARY:
            try:
                assert self.y_size <= 50 and self.x_size <= 200, "The crate won't fit you dumb bitch"
            except AssertionError:
                raise ValueError(f"The value of the y_size and x_size is greater than we can handle. Please fix it")
            except Exception:
                raise Exception("Unexpected item in the bagging area, can't compute.")

some_crate = Crate(y_size=45, id_number="someId", location=CrateLocation.AUXILIARY)

list_of_crates: list[Crate] = []

def move_create_to_room (crate: Crate, location: CrateLocation):
    crate.location = location