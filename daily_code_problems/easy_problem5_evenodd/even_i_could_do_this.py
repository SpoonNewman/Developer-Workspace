user_inputg = int(input("Please input any number: "))

# even = 2n
# odd = 2n+1

def get_evens(n):
    even_int = []
    for num in range(0, (n*2), 2):
        even_int.append(num)
    print(even_int)


def get_odds(n):
    odd_int = []
    for num in range(1, (n*2)+1, 2):
        odd_int.append(num)
    print(odd_int)



def even_odd_handler(user_inputl):
    is_even = input(f"Would you like{user_inputg} even integers or {user_inputg} odd integers?: ")
    
    if is_even == "even":
        get_evens(user_inputl)
    elif is_even == "odd":
        get_odds(user_inputl)
    else:
        raise ValueError("Please type either 'even' or 'odd'")









if __name__ == '__main__':
    even_odd_handler(user_inputg)
    