
gvar = "G"
print('hello from global')


def func_a():
    avar = "A"
    print("hello from func_a")

    def func_b():
        bvar = "B"
        print("hello from func_b")

    print('printing from func_a')
    print(gvar)
    print(avar)
    func_b()
    print(bvar)


# calling func_a
func_a()
func_b()
