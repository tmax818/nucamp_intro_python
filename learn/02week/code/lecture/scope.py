

gvar = "G"
print('hello from global')
tyler = 'asdf'


def func_a():

    avar = "A"
    print("hello from func_a")

    def func_b():
        bvar = "B"
        print("printing avar inside b", avar)
        print("hello from func_b")
        print(tyler)

    print('printing from func_a')
    print(gvar)
    print(avar)
    func_b()
    # print(bvar)

# LEGB


# calling func_a
func_a()
# func_b()
