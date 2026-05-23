f=open("C:\\Python27\\NNLTpython\\Chương 3\\16.4.26\\matran.txt","r")
ma=[]
ma=[dong.split() for dong in f]
print(ma)
s=0
for subma in ma:
    for j in subma:
        s = s + float(j)
print("Tổng các phần tử của ma trận là:", s)