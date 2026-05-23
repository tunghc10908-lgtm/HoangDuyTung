def Sum(a, b,*p):
    s= a+b
    for i in p:
        s=s+i
    return s
print(Sum(1,2))
print(Sum(1,2,3))
print(Sum(1,2,3,4,5,6))