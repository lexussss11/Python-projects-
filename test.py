def s(n):
    global k1
    global k2
    global m
    k1 = 0
    k2 = 0
    last = n % 10
    while n > 0:
        l = n % 10
        if l == 1:
            k1 += 1
        if l == 0:
            k2 += 1
        n = n // 10
    if k1 == k2:
        m += str(last)
    if k1 > k2:
        m += '0'
    if k2 > k1:
        m += '1'
    return m

N = int(input())
m = bin(N)[2:]
k1 = 0
k2 = 0
n = int(m)


print(m)
f = s(n)
print(f)
n1 = int(f)
print(n1)
f1 = s(n1)
print(f1)
n2 = int(f1)
f2 = s(n2)
print(f2)
v = int(f2, 2)
print(v)