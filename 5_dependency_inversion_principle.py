from enum import Enum

class Relations(Enum):
    PARENT= 0
    CHILD = 1
    SIBLING =2
    

class Person:
    def __init__(self,name):
        self.name = name
        
        
class Relationships: # Low level class
    def __init__(self) -> None:
        self.relations = []
        
    def add_parent_and_child(self,parent,child):
        self.relations.append((parent,Relations.PARENT,child))
        self.relations.append((child,Relations.CHILD,parent))
     
    def find_all_children(self,parent_name):
        for r in self.relations:
            if r[0].name == parent_name and r[1] == Relations.PARENT:
                yield r[2].name
        
        
    
        
        
class Research: # High level class
    # def __init__(self,rs) -> None:
    #     for r in rs.relations:
    #         if r[0].name == 'Jack' and r[1] == Relations.PARENT:
    #             print(f"Jack has a child called {r[2].name}")
    
    def __init__(self,rs) -> None:
        for r in rs.find_all_children('Jack'):
            print(f"Jack has a child called {r}")
        

parent = Person('Jack')
child1 = Person('Jane')
child2 = Person('Jacob')


rs = Relationships()
rs.add_parent_and_child(parent,child1)
rs.add_parent_and_child(parent,child2)


Research(rs)