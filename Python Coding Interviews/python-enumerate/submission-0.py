from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i, v in enumerate(nums):
        if v == 7:
            return i
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    first_index = None
    for i, v in enumerate(nums):
        if first_index is None and v == 7:
            first_index = i
        elif first_index is not None and v == 7:
            return i - first_index
    return -1


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
