import sys


def get_tip_value():
    fuck_alt = [
       .20,
       .25,
       .30, 
       .35,
       .40,
       .45,
       .50,
       .55,
       .60
    ]
 
    for position,tip in enumerate(fuck_alt):
        print(f"{position+1} - {int(tip*100)}%")

    selected_tip = input("Please select a tip percentage: ")
    if int(selected_tip) >= len(fuck_alt)+1:
        print("That option is invalid")
        sys.exit()
    return fuck_alt[int(selected_tip)-1]
    

def main():
    total_cost = int(input("What is your total bill:"))
    tip_value = get_tip_value()
    tip_total = total_cost*tip_value 
    print(tip_total)


if __name__ == "__main__":
    main()