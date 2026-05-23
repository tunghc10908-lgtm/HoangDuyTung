a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
tong = a + b
print("Tong =", tong)
max = 0
tam = tong
while tam > 0:
    cs = tam % 10  
    if cs > max:
        max = cs    
    tam //= 10
print("Chu so lon nhat =", max)