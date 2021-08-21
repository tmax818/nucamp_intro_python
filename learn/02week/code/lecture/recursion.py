def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


print(factorial(5))


# number = 5

# for i in range(1, number):
#     number *= i

# print(number)
