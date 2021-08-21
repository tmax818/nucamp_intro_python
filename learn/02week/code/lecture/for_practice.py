start = 1
stop = 11
step = 1
my_list = [1, 2, 3, 4, 5]

for i in range(1, 11, 1):
    if i == 4:
        continue
    elif i == 7:
        break
    print(i)
