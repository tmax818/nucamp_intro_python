# Python 3: Fibonacci series up to n
def fib(n):
    fiblist = []
    a, b = 0, 1
    count = 0
    while count < n:
        fiblist.append(a)
        a, b = b, a + b
        count += 1
    print(fiblist)
    return fiblist[-1]

# def fib(n):


num = fib(10)
print(num)
