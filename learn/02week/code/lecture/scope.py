
my_var = 42

print(my_var)

# func_var = None


def func():
    print(my_var)
    global func_var
    func_var = "hi mom"


func()

print(func_var)
