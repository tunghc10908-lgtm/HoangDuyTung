m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
tong = 0
tam = n
while tam > 0:
    tong += tam % 10
    tam //= 10
print("Tong chu so cua n =", tong)
if m % tong == 0:
    print("m chia het cho n")
else:
    print("m khong chia het cho n")