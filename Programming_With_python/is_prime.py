import math
# ========function_1========
# def is_prime1(n):
#     if n < 2:
#         return False
#     prime = True

#     for i in range(2, n):
#         if n % i == 0:
#             print(n, "is divisible by", i)
#             prime = False
    
#     return prime

# ========function_2========
# def is_prime2(n):
#     if n < 2 :
#         return False
#     prime = True

#     for i in range(2, n):
#         if n % i == 0:
#             print(n, "is divisible by", i)
#             prime = False
#             return prime
        
#     return prime

# ========function_3========
# def is_prime3(n):
#     if n == 2:
#         return True # 2 is prime
#     if n % 2 == 0:
#         print(n, "is divisible by 2")
#         return False # All even numbers except 2 are not prime
#     if n < 2:
#         return False # numbers less than 2 are not prime
#     prime = True
#     for i in range(3, n, 2):
#         if n % i == 0:
#             print(n, "is divisible by", i)
#             prime = False
#             return prime
#     return prime

# ========function_3_alt========
# def is_prime3(n):
#     if n == 2:
#         return True # 2 is prime
#     if n % 2 == 0:
#         print(n, "is divisible by 2")
#         return False # All even numbers except 2 are not prime
#     if n < 2:
#         return False # numbers less than 2 are not prime
#     prime = True
#     m = (n // 2) + 1 # Any number n will not be divisible by any number between (n/2)+1 to n-1
#     for i in range(3, m, 2):
#         if n % i == 0:
#             print(n, "is divisible by", i)
#             prime = False
#             return prime
#     return prime

# ========function_4========
def is_prime4(n):
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



while True:
    number = input("Please enter a number (enter 0 to exit): ")
    number = int(number)

    if number == 0:
        break
    # prime = is_prime1(number)
    # prime = is_prime2(number)
    # prime = is_prime3(number)
    prime = is_prime4(number)
    

    if prime is True:
        print(number, "is a prime number. ")
    else:
        print(number, "is not a prime number. ")