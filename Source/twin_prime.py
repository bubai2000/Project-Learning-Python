# Twin Prime Numbers are the set of two prime numbers that have exactly one composite number between them.
def is_prime(a):
    if a==1:
        return False
    for i in range(2,a):
        if(a%i == 0):
            return False
    return True
    
def is_twin(b):
    return (is_prime(b) and is_prime(b+2))

limit = int(input("Enter the limit to find twin primes=>"))
for i in range(1,limit):
    if(is_twin(i)):
        print({i,i+2})
