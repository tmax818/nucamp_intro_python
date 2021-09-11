my_list = [4, 3, 6, 7, 2, 8, 1, 9, 5]


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    else:
        pivot_index = 0
        pivot = arr[pivot_index]
        storeIndex = pivot_index + 1

        for i in range(1, len(arr) - 1):
            if arr[i] < pivot:
                swap(arr, i, storeIndex)
                storeIndex += 1
                print(arr, storeIndex)


quick_sort(my_list)
