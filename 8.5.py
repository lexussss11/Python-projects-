def ss(n,base):
    new = ''
    if n==0:
        new+='0'
    else:
        while n>0:
            new+=str(n%base)
            n//=base
    return new[::-1] 

maxi = -999999999

for i in range(1,10000):
    n = ss(i,3)
    if i%3==0:
        n = '1'+n+'02'
    else:
        ost = ss((i%3)*4,3)
        n+=ost
    m = int(n,3)
    if m<199 and i>maxi:
        maxi = i
print(maxi)
