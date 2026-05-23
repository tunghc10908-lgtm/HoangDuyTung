class Circle:
    pi = 3.141592
    def __init__(self, radius=1):
        self.bk = radius

    def Dientich(self):
        return Circle.pi * self.bk * self.bk
    
c= Circle(5)
print("Diện tích hình tròn là:", c.Dientich())