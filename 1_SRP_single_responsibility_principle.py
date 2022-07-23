class Basket:
    def __init__(self) -> None:
        self.items = []
        self.counter = 0
    
    def add_item(self,item):
        self.items.append(item)
        self.counter += 1
    
    def remove_item(self,index):
        del self.items[index]
        self.counter -= 1
        
    def __str__(self) -> str:
        return '\n'.join(self.items)
    
    # def save_items(self,filename):
    #     with open(filename,'w') as f:
    #         f.write(str(self))
    #         f.close()
        
        
        
class PersistanceMethod:
    @staticmethod
    def save_to_file(obj,filename):
        with open(filename,'w') as f:
            f.write(str(obj))
            f.close()   
        
b = Basket()
b.add_item('Apple')
b.add_item('Orange')
b.add_item('Mango')

print(b)
    
    
# b.save_items('basket_info.txt')
PersistanceMethod.save_to_file(b,'baket_items.txt')
    