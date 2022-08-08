class Singleton(type):
    __instances = {}
    def __call__(cls, *args, **kwds):
        # return super().__call__(*args, **kwds)
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton,cls).__call__(*args,**kwds)
        return cls.__instances[cls]
    

class Database(metaclass=Singleton):
    def __init__(self) -> None:
        print('Database loaded')
        
        
d1 = Database()
d2 = Database()

print(d1 == d2 )