def main(n):
    if n > 104:
        raise AssertionError("Too many number")


    arr = []
    # ["1", "2", "Fizz", ..., "15", "Fizz", "Buzz", "FizzBuzz"]
    for num in range(1,n+1):
        if num % 5 == 0 or num % 3 == 0:
            if num % 3 == 0 and not num % 5 == 0:
                arr.append("Fizz")
            if num % 5 == 0 and not num % 3 == 0:
                arr.append("Buzz")
            if num % 3 == 0 and num % 5 == 0:
                arr.append("FizzBuzz")
        else:
            arr.append(str(num))



    return arr
        


if __name__ == '__main__':
    
    assert main(3) == ["1","2","Fizz"], 'No es bien'
    assert main(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"], 'No es bien'
    assert main(5) == ["1","2","Fizz","4","Buzz"], 'No es bien'
    # assert main(104)