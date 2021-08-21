

def domath(opt, val, f1, f2):
    if opt == 'sq':
        returnval = f1(val)
    elif opt == 'sqrt':
        returnval = f2(val)
    else:
        returnval = None
    return returnval


# print(domath('sq', 4, lambda num: num * num, lambda num: num ** .5))
print(domath('sqrt', 4, lambda num: num * num, lambda num: num ** .5))
# print(domath('sq', 4, lambda num: num * num, lambda num: num ** .5))
