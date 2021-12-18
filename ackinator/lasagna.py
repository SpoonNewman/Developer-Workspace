# 1. Define expected bake time in minutes
# 2. Calculate remaining bake time in minutes
# 3. Calculate preparation time in minutes (takes in number of layers as arg, returns number of mins of prep. Each layer takes 2 minutes)
# 4. Calculate total elapsed cooking time (prep + bake) in minutes

## Because we have 4 tasks, in our case we should have a minimum of 4 functions.

BAKETIME = 40

def bake_time_remaining (time_we_have_cooked: int) -> int:
    time = BAKETIME - time_we_have_cooked
    return time


def preptime (layers: int) -> int:
    time = layers * 2 
    return time 

def total_elapsed_time (layers: int, elapsed_baketime: int) -> int: 
    return bake_time_remaining(elapsed_baketime) + preptime(layers) 

print('We have 6 layers and 10 minutes cooktime: ', total_elapsed_time(6,10)) # expect 42
assert(total_elapsed_time(6,10) == 42)

print('We have 20 layers and 13 minutes cooktime', total_elapsed_time(20,13)) # expect 27
assert(total_elapsed_time(20,13) == 67)

# assert(total_elapsed_time(24,13) == 27)