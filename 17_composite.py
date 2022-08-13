class GraphicObject:
    def __init__(self,color=None):
        self.color = color
        self._name = "Group"
        self.children = []
        
        
    @property
    def name(self):
        return self._name
    
    
    def _print(self,items,depth):
        items.append("*"*depth)
        
        if self.color:
            items.append(self.color)
        
        items.append(f" {self.name}\n")

        for child in self.children:
            child._print(items,depth+1)


    def __str__(self) -> str:
        items = []
        self._print(items,0)
        return ''.join(items)
        
        
class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"

class Square(GraphicObject):
    @property
    def name(self):
        return "Square"
    
    
if __name__ == '__main__':
    drawing = GraphicObject()
    drawing.children.append(Circle('Blue'))
    drawing.children.append(Square('Green'))
    
    
    group = GraphicObject()
    group.children.append(Circle('Red'))
    group.children.append(Square('Yellow'))
    drawing.children.append(group)
    
    print(drawing)