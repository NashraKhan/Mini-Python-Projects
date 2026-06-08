from GeometryTools_2509399 import circle_area, rect_area

r = int(input('Enter Radius: '))
l = int(input('Enter Length: '))
b = int(input('Enter Breadth: '))

print(f' Area of Circle: {circle_area.circle(r)}')
print(f' Area of Rectangle: {rect_area.rectangle(l, b)}')
