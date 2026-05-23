n = int(input("Nhap n: "))
tong = 0
tam = n
while tam > 0:
    tong += tam % 10
    tam //= 10
print("Tong chu so =", tong)
if tong % 3 == 0:
    print("Chia het cho 3")
else:
    print("Khong chia het cho 3")