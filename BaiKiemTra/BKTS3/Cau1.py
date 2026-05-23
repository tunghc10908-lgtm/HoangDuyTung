n = int(input("Nhap n: "))
tong = 0
dem = 0
for i in range(n):
    k = float(input(f"k[{i}] = "))
    if 0 < k < 1000:
        tong += k
        dem += 1
if dem > 0:
    print("Trung binh cong =", tong / dem)
else:
    print("Khong hop le")