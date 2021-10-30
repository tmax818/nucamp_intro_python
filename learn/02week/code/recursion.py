# [0,1,1,2,3,5,8,13]
# [0,1,2,3,4,5,6, 7]


def rFib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return rFib(n-1) + rFib(n-2)


rFib(4)
