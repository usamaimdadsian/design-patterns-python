import time

def time_it(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        
        print(f"{func.__name__} took {(end-start)*1000}ms.")
    
    return wrapper



@time_it
def some_op():
    print('Starting the process')
    time.sleep(1)
    print('Process complete')
    
    
    
if __name__ == '__main__':
    # time_it(some_op)()
    some_op()