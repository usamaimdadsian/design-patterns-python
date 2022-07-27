class Rectangle:
    def __init__(self,width, height) -> None:
        self._width = width
        self._height = height
        
    @property
    def width(self):
        return self._width
    
    @property
    def area(self):
        return self._width * self._height
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self,val):
        self._width = val
        
    @height.setter
    def height(self,val):
        self._height = val
        
class Square(Rectangle):
    def __init__(self, size) -> None:
        super().__init__(size, size)
        
    @Rectangle.width.setter
    def width(self,val):
        self._width = self._height = val
        
    @Rectangle.width.setter
    def height(self,val):
        self._width = self._height = val

def use_it(rc):
    width = rc.width
    rc.height = 10
    
    area = width * 10
    
    print(f'Expected Area: {area}, Calculated Area: {rc.area}')

r = Rectangle(5,3)
use_it(r)

s = Square(5)
use_it(s)