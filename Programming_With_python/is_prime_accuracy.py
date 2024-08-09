import math

# ========function_4========
def is_prime4(n=1013):
    if n == 2:
        return True # 2 is prime
    if n % 2 == 0:
        print(n, "is divisible by 2")
        return False # All even numbers except 2 are not prime
    if n < 2:
        return False # numbers less than 2 are not prime
    m = math.sqrt(n)
    m = int(m) + 1
    for i in range(3, m, 2):
        if n % i == 0:
            print(n, "is divisible by", i)
            return False
    return True

# ========function_3========
def is_prime3(n=1013):
    if n == 2:
        return True # 2 is prime
    if n % 2 == 0:
        print(n, "is divisible by 2")
        return False # All even numbers except 2 are not prime
    if n < 2:
        return False # numbers less than 2 are not prime
    prime = True
    for i in range(3, n, 2):
        if n % i == 0:
            print(n, "is divisible by", i)
            prime = False
            return prime
    return prime

import timeit
t1 = timeit.timeit(is_prime3)
t2 = timeit.timeit(is_prime4)
print(t1, t2, t1/t2)