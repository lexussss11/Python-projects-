mini = 999999999
for i in range(1,1000):
    n = bin(i)[2:]
    m = int(n)
    n += str(m % 10)
    k1 = 0
    while m > 0:
        l = m % 10
        if l == 1:
            k1 += 1
        m //= 10
    if k1 % 2 == 0:
        n += '0'
    if k1 % 2 != 0:
        n += '1'
    m = int(n)
    k1 = 0
    while m > 0:
        l = m % 10
        if l == 1:
            k1 += 1
        m //= 10
    if k1 % 2 == 0:
        n += '0'
    if k1 % 2 != 0:
        n += '1'
    if int(n, 2) > 114 and int(n, 2) < mini:
        mini = int(n, 2)
print(mini)