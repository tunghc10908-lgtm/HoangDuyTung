n = int(input("Nhap n: "))
tong = 0
dem = 0
for i in range(n):
    x = float(input(f"x[{i}] = ")) 
    if -1000 < x < -10:
        tong += x
        dem += 1
if dem > 0:
    print("Trung binh cong =", tong / dem)
else:
    print("Khong hop le")