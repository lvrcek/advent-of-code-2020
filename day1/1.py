with open('in.txt') as f:
    numbers = list(map(int, f.readlines()))

flag = False

for i in numbers:
    for j in numbers:
        if i + j == 2020:
            print(i * j)
            flag = True
            break
    if flag:
        break

flag = False

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                 print(i * j * k)
                 flag = True
                 break
        if flag:
            break
    if flag:
        break