def shitty_function(day: int) -> str:
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"
    else:
        return "It fucked up"

def better_function(day: int) -> str:
    if day > 7 or day < 1:
        return "It fucked up"
    list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return list_of_days[day-1]

for arg in [1,2,3,4,5,6,7,8,9,10,11, 12, 13, 14, 16, 0, -3]:
    assert shitty_function(arg) == better_function(arg)