from pathlib import Path

p = Path(__file__).with_name('shape.txt')

class Shape:
    def getArea(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def getArea(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w
    
class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def getArea(self):
        return 0.5 * self.b * self.h
    
with p.open('r') as f:
    for line in f:
        # print(line)
        shape = line.split(',')
        if shape[0] == 'Circle':
            c = Circle(float(shape[1]))
            print('Circle area: %.2f' % c.getArea())
        elif shape[0] == 'Rectangle':
            r = Rectangle(float(shape[1]), float(shape[2]))
            print('Rectangle area: %.2f' % r.getArea())
        elif shape[0] == 'Triangle':
            t = Triangle(float(shape[1]), float(shape[2]))
            print('Triangle area: %.2f' % t.getArea())

