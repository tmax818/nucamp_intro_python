import time


def display_args(*args):
    print("the_list", args[3])
    print("pivot: ", "index: ", args[0], "item", args[3][args[0]])
    print("upper: ", "index: ", args[1], "item", args[3][args[1]])
    print("lower: ", "index: ", args[2], "item", args[3][args[2]])


def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        time.sleep(5)
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]
        display_args(pivot, upper_bound, lower_bound, the_list)

        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1
    return -1


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(test_list, 10))
# print(binary_search(test_list, 4))
print(binary_search(test_list, 33))
