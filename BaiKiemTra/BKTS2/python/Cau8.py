def Cau8():
    print("cau 8")
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))
    z = int(input("Nhập z: "))
    tich = x * y * z
    dem = 0
    tam = abs(tich)
    if tam == 0:
        dem = 1
    else:
        while tam > 0:
            dem += 1
            tam = tam // 10
    print("Tích =", tich)
    print("Số chữ số =", dem)

