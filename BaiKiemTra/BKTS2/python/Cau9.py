def Cau9():
    print("cau 9")
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    c = int(input("Nhập c: "))
    tong = a + b + c
    dem_chan = 0
    tam = abs(tong)
    if tam == 0:
        dem_chan = 1
    else:
        while tam > 0:
            if (tam % 10) % 2 == 0:
                dem_chan += 1
            tam = tam // 10
    print("Tổng =", tong)
    print("Số chữ số chẵn =", dem_chan)