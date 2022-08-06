
import copy

class Address:
    def __init__(self,office, city, country) -> None:
        self.office = office
        self.city = city 
        self.country = country
        
    def __str__(self) -> str:
        return f"{self.office}, {self.city}, {self.country}"

class Person:
    def __init__(self,name, address) -> None:
        self.name = name
        self.address = address
        
    def __str__(self) -> str:
        return f"{self.name} live at {self.address}"
    
    

class PersonFactory:
        lahore_office = Person('',Address('','Lahore','Pakistan'))
        islamabad_office = Person('',Address('','Islamabad','Pakistan'))
        
        
        @staticmethod
        def __new_person(proto,name,office):
            result = copy.deepcopy(proto)
            result.name = name
            result.address.office = office
            return result
        
        @staticmethod
        def create_lahore_person(name, office):
            return PersonFactory.__new_person(PersonFactory.lahore_office,name, office)
        
        @staticmethod
        def create_islamabad_person(name, office):
            return PersonFactory.__new_person(PersonFactory.islamabad_office,name, office)

    
# john = Person('john', Address('street 9', 'Lahore', "Pakistan"))


# print(john)

# jane = copy.copy(john)

# jane.name = 'Jane'
# jane.address.street = "street 10"

# print('---'*5)
# print(jane)
# print(john)

usama = PersonFactory.create_lahore_person('usama',12)
print(usama)
fahad = PersonFactory.create_islamabad_person('fahad',50)
print(fahad)