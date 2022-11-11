
"""
if we run something defined locally, then __name__ will be "__main__"
if we run something imported from other package __name__ will be the package name
"""



def intdiv(func):
    def inner(a,b):
        if(a<b):
            return "Division not possible!"
        else:
            return func(a,b)
    return inner

@intdiv #below function uses intdiv decorator
def division(a,b):
    return a/b

print(division(10,5))
print(division(2,3))