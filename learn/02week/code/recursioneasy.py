# def countdown(n):
#     for i in range(n, 0, -1):
#         print(i)


def r_countdown(n):
    print(n)
    if n > 0:
        r_countdown(n-1)


# countdown(5)
r_countdown(5)
