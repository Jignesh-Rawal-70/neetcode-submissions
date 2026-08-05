from typing import List

def read_integers() -> List[int]:
    input_str = input()
    #print(input_str)
    input_list = input_str.split(',')
    return [int(x) for x in input_list]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
