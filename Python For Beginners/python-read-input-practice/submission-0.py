def add_two_numbers() -> int:
    numbers_str = input()
    numbers_str_arr = numbers_str.split(',')
    return int(numbers_str_arr[0]) + int(numbers_str_arr[1])



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
