def is_prime(num):
    if num <= 1:
        return False
    start = 2
    end = int(num**(1/2)) + 1
    for i in range(start, end):
        if num % i == 0:
            return False
    return True
        
        
# print(is_prime(0))
# print(is_prime(-7))
# print(is_prime(41))
print(is_prime(5099))
print(is_prime(45))
print(is_prime(2))
print(is_prime(3))
# print(is_prime(9))


# from math import sqrt
# def is_prime(num):
#     if num <= 1:
#         return False
#     i = 2
#     while i <= sqrt(num):    
#         if num%i == 0:
#             return False
#         i += 1
#     return True 