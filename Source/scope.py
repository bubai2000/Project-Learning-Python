# Four types of scope 1. Builtin, 2. Global, 3. Local, 4. Non-local
# Built-in scope for keywords like print(), False, True, lambda, continue, while, all these are accessible when python interpreter starts, can use them anywhere in code
# Global scope is file wide, can be used anywhere inside file

x=1
y=1
a=5
b=5

# Example 1 if a function can't find a variable in local scope it goes to one step outer and so on until it finds the variable
def foo():
    print(x)
foo()
print(x)

#Example 2 if a function 
def foo2():
    x=5
    print(x)
foo2()
print(x)

def foo3():
    global y
    y=2
    print(y)
foo3()
print(y)

