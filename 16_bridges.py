class Render:
    def draw_circle(self):
        pass
    
    
class PixelRender(Render):
    def draw_circle(self):
        print('Drawing with PixelRender')
        
        
class VectorRender(Render):
    def draw_circle(self):
        print('Drawing with VectorRender')
        
        

class Shape:
    def __init__(self,render) -> None:
        self.render = render
        
    def resize(self,val): pass
    def draw(self):pass
    
    
    
class Circle(Shape):
    def __init__(self, render,radius) -> None:
        super().__init__(render)
        self.radius = radius
        
    def resize(self, val):
        self.radius *= val
        
    def draw(self):
        self.render.draw_circle()
        
        
if __name__ == '__main__':
    vr = VectorRender()
    pr = PixelRender()
    
    c = Circle(vr,5)
    c.draw()