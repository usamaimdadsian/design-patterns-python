# text = 'pakistan zindabad'

# print('<p>'+text+'</p>')

# words = ['hello', 'world']

# lines = ['<ul>']
# for w in words:
#     lines.append('<li>'+w+'</li>')
# lines.append('</ul>')

# print('\n'.join(lines))


class HtmlElement:
    indent_size = 2
    def __init__(self,name="",text="") -> None:
        self.name = name
        self.text = text
        
        self.children = []
        
    def __str(self,indent):
        lines = []
        lines.append(f"{' '*(self.indent_size*indent)}<{self.name}>")
        
        if self.text:
            lines.append(f"{' '*(self.indent_size*(indent+1))}{self.text}")
        
        for child in self.children:
            lines.append(child.__str(indent+1))
            
        lines.append(f"{' '*(self.indent_size*(indent))}</{self.name}>")
        return "\n".join(lines)
        
    def __str__(self) -> str:
        return self.__str(0)
    
    
    @staticmethod
    def create(root_name):
        return HtmlBuilder(root_name)
        
    

class HtmlBuilder:
    __root = HtmlElement()
    def __init__(self,root_name) -> None:
        self.root = root_name
        self.__root.name = root_name
        
    def add_child(self,child_name, child_text):
        self.__root.children.append(HtmlElement(child_name,child_text))
        
    def add_child_fluent(self,child_name, child_text):
        self.__root.children.append(HtmlElement(child_name,child_text))
        return self
    
        
    def __str__(self) -> str:
        return self.__root.__str__()
    
b = HtmlElement.create('ul')
b.add_child_fluent('li','hello').add_child_fluent('li','world')

print(b)