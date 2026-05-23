n = int(input("Nhap n: "))
tich = 1
tam = n
while tam > 0:
    tich *= tam % 10
    tam //= 10
print("Tich chu so =", tich)
if tich % 2 == 0 and tich > 20:
    print("Dung")
else:
    print("Sai")