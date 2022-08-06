from enum import Enum
from math import *


class PointType(Enum):
    CARTESIAN = 0
    POLAR = 1



class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return f"({self.x},{self.y})"
    
    
    @staticmethod
    def create_cartesian_point(x,y):
        return Point(x,y)
    
    
    @staticmethod
    def create_polar_point(rho,theta):
        x = rho * cos(theta)
        y = rho * sin(theta)
        
        return Point(x,y)
    
    
cp = Point.create_cartesian_point(3,4)
print(cp)

pp = Point.create_polar_point(10,45)
print(pp)