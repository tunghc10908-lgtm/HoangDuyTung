a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
tam = b
min = 9
while tam > 0:
    cs = tam % 10
    if cs < min:
        min = cs    
    tam //= 10
print("Chu so nho nhat cua b =", min)
if min != 0 and a % min == 0:
    print("a chia het cho chu so nho nhat cua b")
else:
    print("a khong chia het cho chu so nho nhat cua b")