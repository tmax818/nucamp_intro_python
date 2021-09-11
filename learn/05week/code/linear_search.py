'''
A linear search algorithm is one that looks through the items in a data set such as a list, item by item, and compares it to a value being searched. It is the most simple kind of search - you start at the beginning of the data set and go until you reach the end, or you find a match.
'''


def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print("Found at index", x)
            return x
    print("Target is not in the list")
    return -1


my_list = [6, 3, 4, 2, 5, 7]
linear_search(my_list, 5)
# linear_search(my_list, 3)
linear_search(my_list, 8)
