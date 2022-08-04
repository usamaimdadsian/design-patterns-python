class Person:
    def __init__(self) -> None:
        self.street_address = None
        self.post_code = None
        self.city = None
        
        
        self.company_name = None
        self.position = None
        self.earning = None
        
    def __str__(self) -> str:
        return f"Address = {self.street_address}, {self.post_code}, {self.city} - "+\
        f"Works at {self.company_name} as a {self.position} earning {self.earning}"
        
    @staticmethod
    def create():
        return PersonBuilder()
        
        

class PersonBuilder:
    def __init__(self,person=Person()) -> None:
        self.person = person
        
    @property
    def works(self):
        return PersonJobBuilder(self.person)
    
    
    @property
    def address(self):
        return PersonAddressBuilder(self.person)
    
    
    def build(self):
        return self.person.__str__()
        
        
        
class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)
        
    def street_address(self,street_address):
        self.person.street_address = street_address
        return self
    
    def post_code(self,post_code):
        self.person.post_code = post_code
        return self
    
    
    def city(self,city):
        self.person.city = city
        return self
    
    
class PersonJobBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)
        
    def company_name(self,company_name):
        self.person.company_name = company_name
        return self
    
    def position(self,position):
        self.person.position = position
        return self
    
    
    def earning(self,earning):
        self.person.earning = earning
        return self
    
    
    
p = Person.create()
p.works.company_name('temp name').position('Software Architect').earning(500000)
p.address.street_address('steen 9').post_code('23454').city('Lahore')

print(p.build())