

user_input = int(input("Please type what number you would like to check:"))

def main(n):
    non_prime = []
    for num in range(2, n):
        if n % num == 0:
            non_prime.append(num)
    if  len(non_prime) > 0:
        print(f"{n} Is not a prime number. {n} was evenly divided by {non_prime}")
        return False
    else:
        print(f"{n} Is a prime number")
        return True

    
    
        
    
            


        
# # Get the input from user//
# Take that input and check if it is a prime number
    # user_input = 14
    # if user_input % 2 == 0
    # if user_input % 3 == 0
    # if user_input % 4 == 0
    # ...
    # if user_input % user_input - 1 == 0
# If it is a prime number print it out 
# If it isn't a prime number print out what the number can be divided by

if __name__ == '__main__':
    main(user_input)
    assert main(5) is True
    assert main(6) is False
    assert main(23) is True
    assert main(24) is False
