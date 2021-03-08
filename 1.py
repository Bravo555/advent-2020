f = open('input1.txt', 'r')

data = list(map(int, f.read().split('\n')))
print(repr(data))


for i in data:
    for j in data:
        for k in data:
            sum1 = i + j + k
            if sum1 == 2020:
                print('Liczby to:', i, j, k)
                print(i * j * k)
                exit()

