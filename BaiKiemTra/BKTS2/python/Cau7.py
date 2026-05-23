def Cau7():
    print("cau 7")
    n = int(input("Nhập n: "))
    tong = 0
    def la_so_nguyen_to(x):
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True
    for i in range(n):
        x = int(input("Nhập phần tử thứ %d: " % (i + 1)))
        if la_so_nguyen_to(x):
            tong += x
    print("Tổng các số nguyên tố =", tong)
    if tong % 2 != 0 and tong > 50:
        print("Tổng là số lẻ và lớn hơn 50")
    else:
        print("Tổng không thỏa điều kiện")


