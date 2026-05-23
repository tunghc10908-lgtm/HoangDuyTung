a=float(input("Nhập vào số a: "))
b=float(input("Nhập vào số b: "))
if (a==0):
    if (b==0):
        print("phương trình có vô số nghiệm")
    else:
        print("phương trình vô nghiệm")
else:
    x=-b/a
    print("x=", x)