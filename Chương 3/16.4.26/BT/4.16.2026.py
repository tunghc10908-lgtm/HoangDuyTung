a = []
n = int (input("Nhập số phần tử của dãy số:"))
for i in range(1,n+1):
	k = int(input("Nhap phần tử thứ "+str(i)+":"))
	a.append(k)
obj=open("C:\\Python27\\NNLTpython\\Chương 3\\16.4.26\\dulieu.txt","w")
for i in a:
	obj.write(str(i)+"  ")
obj.close()