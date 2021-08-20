def rFib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return rFib(n-1) + rFib(n-2)


rFib(4)


# def fib_seq(n):
#     fib_list = []
#     for i in range(n + 1):
#         fib_list.append(rFib(i))

#     return fib_list


# print(fib_seq(5))
