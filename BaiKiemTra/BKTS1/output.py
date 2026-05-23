obj = open("C:\\Python27\\NNLTpython\\Chương 3\\23.4.26\\input.txt", "r")
s1 = obj.read()
obj.close()

so = ""
chu = ""

for i in s1:
    if i.isdigit():
        so += i
    elif i.isalpha():
        chu += i

open("outso.txt", "w").write(so)
open("outchu.txt", "w").write(chu)

print("So:", so)
print("Chu:", chu)