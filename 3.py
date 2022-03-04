#Anu Sunny
#21MCA_006
class Rectangle:
    def __init__(self, length,breadth):
        self.length = length
        self.breadth = breadth

    def cal_area(self):
        self.area=self.length * self.breadth
        print('Area : ',self.area)

    def __lt__(self, second):
        if self.area < second.area:
            return True
        else:
            return False
print('Enter length and breadth of rectangle 1:')
l,b=int(input()),int(input())
print('Enter length and breadth of rectangle 2:')
l2,b2=int(input()),int(input())
print('rectangle 1 area:')
r = Rectangle(l,b)
r.cal_area()
print('rectangle 2 area:')
r2 = Rectangle(l2,b2)
r2.cal_area()

if r < r2:
        print("\nRectangle two is large")
else:
        print("Rectangle one is large")

