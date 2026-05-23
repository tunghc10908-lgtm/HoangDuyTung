x = int(input("Nhập x:"))
print("Các số hoàn hảo là:")
for num in range(1,x+1):
    tong=0
    for i in range(1,num):
        if num%i==0:
            tong+=i
    if tong==num:
        print(num)