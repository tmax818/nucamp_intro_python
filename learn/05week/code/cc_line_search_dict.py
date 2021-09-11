

def linear_search_dictionary(the_dict, target):
    for k, v in the_dict.items():
        if v == target:
            print(f"Found at key {k}")
            return k
    print("Target is not in the dictionary")
    return None


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
