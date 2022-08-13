class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        

def draw_point(p):
    print(".",end="")
    
    
class Line:
    def __init__(self,start,end) -> None:
        self.start = start
        self.end = end
        

class Rectangle(list):
    def __init__(self,x,y,width,height):
        super().__init__()
        
        self.append(Line(Point(x,y),Point(x+width,y)))
        self.append(Line(Point(x+width,y),Point(x,y+height)))
        self.append(Line(Point(x,y+height),Point(x+width,y+height)))
        self.append(Line(Point(x+width,y+height),Point(x,y)))
        
        
class LineToPointAdapter(list):
    count = 0
    def __init__(self,line) -> None:
        super().__init__()
        self.count += 1
        print(
            f"Drawing Line Number: {self.count}"
            f"[{line.start.x},{line.start.y}] ->"
            f"[{line.end.x},{line.end.y}]"
        )
        
        
        left = min(line.start.x,line.end.x)
        right = max(line.start.x,line.end.x)
        
        top = min(line.start.y,line.end.y)
        bottom = max(line.start.y,line.end.y)
        
        
        if right - left == 0:
            for y in range(top,bottom):
                self.append(Point(left,y))
        elif top - bottom == 0:
            for x in range(left,right):
                self.append(Point(x,top))
                
                
                
    
    
def draw_rectangles(rects):
    for r in rects:
        for line in r:
            adapter = LineToPointAdapter(line)
            
            for p in adapter:
                draw_point(p)



if __name__ == '__main__':
    rectangles = [
        Rectangle(1,1,5,3),
        Rectangle(10,10,7,7)
    ]
    
    draw_rectangles(rectangles)