import datetime
x = datetime.datetime(2021,6,17)
print(x)
import datetime
now = datetime.datetime.now()
print(now)
s=now.strftime("%d-%m-%Y %H:%M:%S")
print("ngay gio hien tai:", s)
s1=now.strftime("%d-%m")
print("ngay thang hien tai:", s1)