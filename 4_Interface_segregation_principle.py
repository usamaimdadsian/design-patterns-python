#ISP -  INTERFACE SEGREGATION PRINCIPLE

# class Machine:
#     def print(self,document):
#         raise NotImplementedError
#     def scan(self,document):
#         raise NotImplementedError
#     def fax(self,document):
#         raise NotImplementedError
    
    
# class MultiFunctionPrinter(Machine):
#     def print(self,document):
#         pass
#     def scan(self,document):
#         pass
#     def fax(self,document):
#         pass
    
    

# class OldFashionPrinter(Machine):
#     def print(self,document):
#         pass
#     def scan(self,document):
#         raise NotImplementedError('Not implemented!!')
    
#     def fax(self,document):
#         raise NotImplementedError('Not implemented!!')
    
    
from abc import abstractmethod


class Printer:
    @abstractmethod
    def print(self,document):
        pass

class Scanner:
    @abstractmethod
    def scan(self,document):
        pass
    
class OldFashionPrinter(Printer):
    def print(self,document):
        pass
    
    
class NewFashionPrinter(Printer,Scanner):
    def print(self,document):
        pass
    
    def scan(self,document):
        pass
