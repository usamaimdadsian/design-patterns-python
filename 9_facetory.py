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
    


    class PointFactory:
        def create_cartesian_point(self,x,y):
            return Point(x,y)
        
        
        def create_polar_point(self,rho,theta):
            x = rho * cos(theta)
            y = rho * sin(theta)
            
            return Point(x,y)
    
    factory = PointFactory()
    
cp = Point.factory.create_cartesian_point(3,4)
print(cp)

pp = Point.factory.create_polar_point(10,45)
print(pp)