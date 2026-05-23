def gt (m):
    gt=1
    for i in range(1,m+1):
        gt=gt*i
    return gt
n = int(input("Nhập n: "))
print("%d! = %d" % (n, gt(n)))