while True:
    print("1. Cau 7")
    print("2. Cau 8")
    print("3. Cau 9")
    print("0. Thoat")

    chon = int(input("Nhap lua chon: "))

    if chon == 1:
        from python.Cau7 import Cau7
        Cau7()
    elif chon == 2:
        from python.Cau8 import Cau8
        Cau8()
    elif chon == 3:
        from python.Cau9 import Cau9
        Cau9()
    elif chon == 0:
        print("Ket thuc chuong trinh")
        break
    else:
        print("Lua chon khong hop le!")