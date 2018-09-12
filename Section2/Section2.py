#coding= utf-8
# python3练习第二章

import math
class Point:
    '这是一个坐标点'
    def __init__(self, x=0, y=0):
        '初始化方法'
        self.move(x,y)
        print "初始化方法"

    def move(self, x, y):
        '移动点'
        self.x = x
        self.y = y
        print "移动"

    def reset(self):
        '重制坐标为（0，0）'
        self.move(0,0)
    def calculate_distance(self,other_point):
        '''计算距离
        '计算俩个点之间的距离'''
        return math.sqrt(
            (self.x - other_point.x)**2 +(self.y - other_point.y)**2

        )

point1 = Point()
point2 = Point()


point2.move(10,5)

print (point1.x)
print(point1.calculate_distance(point2))