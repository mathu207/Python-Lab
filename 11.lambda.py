import math
rectanglearea=lambda length,breadth:(length*breadth)*2
circlearea=lambda radius: math.pi*radius*radius
trianglearea=lambda base,height:(base*height)/2
length = int(input("length of the rectangle "))
breadth = int(input("breadth of the rectangle "))
print("rectangle area:{}".format(rectanglearea(length,breadth)))
radius = int(input("radius of the circle "))
print("circlearea:{}".format(circlearea(radius)))
