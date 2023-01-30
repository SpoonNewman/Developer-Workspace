def exchange_money(budget: float, exchange_rate: float):
    pass

def get_change(budget: float, exchanging_value: float):
    pass

def get_value_of_bills(denomination: int, number_of_bills: int):
    pass

def get_number_of_bills(budget: float, denomination: int):
    pass

def get_leftover_of_bills(budget: float, denomination: int):
    pass

if __name__ == "__main__":
    assert exchange_money(127.5, 1.2) == 106.25

    assert get_change(127.5, 120) == 7.5

    assert get_value_of_bills(5, 128) == 640

    assert get_number_of_bills(127.5, 5) == 25

    assert get_leftover_of_bills(127.5, 20) == 7.5
    assert get_leftover_of_bills(164.3, 10) == 4.300000000000011