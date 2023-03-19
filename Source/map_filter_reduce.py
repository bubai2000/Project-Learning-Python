from functools import reduce

def is_prime(a: int):
    for i in range(2,round(a/2)):
        if a%i==0:
            return False
    return True

def do_square(a):
    if a%2==0:
        return a*a
    return a*a*a

def sum_odd(a,b):
    if b%2!=0:
        return a+b
    return a

def sum_even(a,b):
    if b%2==0:
        return a+b
    return a

numbers=[n for n in range(1,101)]

even=filter(lambda x: x%2==0, numbers)

prime=filter(is_prime, numbers)

square=map(do_square, numbers)

sum_of_odd=reduce(lambda a,b: sum_odd(a,b),numbers)

sum_of_even=reduce(lambda a,b: sum_even(a,b),numbers[1:])

print(list(even))

print(list(prime))

print(list(square))

print(f"Sum of even: {sum_of_even}\n Sum of odd: {sum_of_odd}")