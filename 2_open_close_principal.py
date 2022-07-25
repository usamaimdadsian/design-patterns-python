from enum import Enum

class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    
class Size(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

class Product:
    def __init__(self,name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size
        
    def __str__(self) -> str:
        return f"Name: {self.name}, Color: {self.color}, Size: {self.size}"
    
    
class ProductFilter:
    def filter_by_color(self,products,color):
        for product in products:
            if product.color == color:
                yield product
    
    def filter_by_size(self,products,size):
        for product in products:
            if product.size == size:
                yield product
                
                
    def filter_by_color_and_size(self,products,color,size):
        for product in products:
            if product.size == size and product.color == color:
                yield product
                
     
class Specification:
    def is_satisfied(self,item):
        pass
    
    def __and__(self,other):
        return AndSpecification(self,other)
    
class Filter:
    def filter(self,items,spec):
        pass
    
    
class ColorSpecification(Specification):
    def __init__(self,color) -> None:
        self.color = color
    
    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self,size) -> None:
        self.size = size
    
    def is_satisfied(self, item):
        return item.size == self.size
    
class AndSpecification(Specification):
    def __init__(self,spec1,spec2) -> None:
        self.spec1 = spec1
        self.spec2 = spec2
    
    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)

    
class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item
                
    
    
apple = Product('Apple',Color.RED,Size.SMALL)
car = Product('Car',Color.BLUE,Size.MEDIUM)
house = Product('House',Color.BLUE,Size.LARGE)


p = [apple, car, house]

pf = ProductFilter()

# for p in pf.filter_by_color(p,Color.BLUE):
#     print(p)


cs = ColorSpecification(Color.BLUE)
bf = BetterFilter()

for item in bf.filter(p,cs):
    print(item)
    
print("\n","=="*50)
ss = SizeSpecification(Size.LARGE)
for item in bf.filter(p,ss):
    print(item)


print("\n","=="*50)
# ss = AndSpecification(cs,ss)
ast = cs and ss
for item in bf.filter(p,ss):
    print(item)
    