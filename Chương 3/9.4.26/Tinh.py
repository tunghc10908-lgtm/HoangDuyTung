import CT

a=int(input("Nhập bán kính hình tròn: "))
b=int(input("Nhập chiều dài hình chữ nhật: "))
c=int(input("Nhập chiều rộng hình chữ nhật: "))
d=int(input("Nhập cạnh hình vuông: "))
print("Diện tích hình tròn là:", CT.sht(a))
print("Diện tích hình chữ nhật là:", CT.shcn(b, c)) 
print("Diện tích hình vuông là:", CT.shv(d))
print("Chu vi hình chữ nhật là:", CT.cvhcn(b, c))