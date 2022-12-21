# ? + 10 = 17 
# ? + 15 = 17
# 7 + 10 = 17
# 10 + 15 = 25
# 7 + 15 = 22
numbers = [10, 15, 3, 7]


K = 17

def addition(K, numbers):
    for number in numbers:
        if K - number in numbers:
            # print('We found it!')
            return True
        
            


# addition()

# if __name__ == "__main__":
#     test_numbers_set = [
#         (17, [10, 15, 3, 7]),
#         (12, [3, 8, 4, 22]),
#         (24, [4, 1, -8, 18, 15, 20]),
#         (12, [2, 2, 4, 8, 7])
#     ]
#     for k, test_numbers in test_numbers_set:
#         assert addition(k, test_numbers), "Failed to get the k"
