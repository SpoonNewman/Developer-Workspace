
money = []

def exchange_money(budget: float, exchange_rate: float):
    exchanged_money = budget / exchange_rate 
    money.append(exchanged_money)
    return exchanged_money

def get_change(budget: float, exchanging_value: float):
    change = budget % exchanging_value
    money.append(change)
    return change

def get_value_of_bills(denomination: int, number_of_bills: int):
    value = denomination * number_of_bills
    money.append(value)
    return value

def get_number_of_bills(budget: float, denomination: int):
    number_of_bills = budget // denomination
    money.append(number_of_bills)
    return number_of_bills

def get_leftover_of_bills(budget: float, denomination: int):
    leftovers = budget % denomination
    money.append(leftovers)
    return leftovers

if __name__ == "__main__":
    assert exchange_money(127.5, 1.2) == 106.25 # assert True == 106.25

    assert get_change(127.5, 120) == 7.5

    assert get_value_of_bills(5, 128) == 640

    assert get_number_of_bills(127.5, 5) == 25
 
    assert get_leftover_of_bills(127.5, 20) == 7.5
    assert get_leftover_of_bills(164.3, 10) == 4.300000000000011
    assert money == [106.25, 7.5, 640, 25, 7.5, 4.300000000000011]
    print(money)