
"""
if we run something defined locally, then __name__ will be "__main__"
if we run something imported from other package __name__ will be the package name
"""



def dec(func):
    def wrapper(a,b):
        if b==0:
            print("Division by zero not allowed!")
            return
        return func(a,b)
    return wrapper

@dec
def div(a: float,b: float):
    print(a/b)
    
div(10,5)
div(3,0)

