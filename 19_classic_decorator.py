class Shape:
    def __str__(self) -> str:
        return ""
    
    
class Circle(Shape):
    def __init__(self,radius) -> None:
        self.radius = radius
        
        
    def __str__(self) -> str:
        return f"Circle with {self.radius} radius"
    
class Square(Shape):
    def __init__(self,side) -> None:
        self.side = side
        
        
    def __str__(self) -> str:
        return f"Square with {self.side} side"
    
    
    
    
class ColorShape:
    def __init__(self,shape,color) -> None:
        self.shape = shape
        self.color = color
    
    def __str__(self) -> str:
        return f"{self.shape} with color {self.color}"
    
class TransparentShape:
    def __init__(self,shape,transparent) -> None:
        self.shape = shape
        self.transparent = transparent
    
    def __str__(self) -> str:
        return f"{self.shape} with transparency {self.transparent * 100}%"
    
    
    
if __name__ == '__main__':
    c1 = Circle(5)
    
    print(c1)
    
    dc1 = ColorShape(c1,'Green')
    print(dc1)
    
    dtc1 = TransparentShape(c1,0.6)
    print(dtc1)
    
    
