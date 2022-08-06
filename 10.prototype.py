
import copy

class Address:
    def __init__(self,street, city, country) -> None:
        self.street = street
        self.city = city 
        self.country = country
        
    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.country}"

class Person:
    def __init__(self,name, address) -> None:
        self.name = name
        self.address = address
        
    def __str__(self) -> str:
        return f"{self.name} live at {self.address}"
    
    
    
john = Person('john', Address('street 9', 'Lahore', "Pakistan"))


print(john)

jane = copy.copy(john)

jane.name = 'Jane'
jane.address.street = "street 10"

print('---'*5)
print(jane)
print(john)
