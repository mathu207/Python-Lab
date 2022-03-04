#Anu Sunny
#21MCA_006
class Rectangle:
    def __init__(self, length,breadth):
        self.length = length
        self.breadth = breadth


    def cal_area(self):
        area=self.length * self.breadth
        print('Area : ',area)

    def cal_perimeter(self):
        perimeter= 2 * (self.length + self.breadth)
        print('perimeter ', perimeter)

print('Enter length and breadth of rectangle 1:')
l,b=int(input()),int(input())

print('Enter length and breadth of rectangle 2:')
l2,b2=int(input()),int(input())

print('rectangle 1:')
r = Rectangle(l,b)
r.cal_area()
r.cal_perimeter()

print('\nrectangle 2:')
r2 = Rectangle(l2,b2)
r2.cal_area()
r2.cal_perimeter()