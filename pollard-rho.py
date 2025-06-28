from math import gcd
import random

def pollardRho(n: int, f=lambda x: x**2 + 1):

    # Initialize two pointers with the same random value
    x = y = random.randint(1, n-1)
    result = 1

    #Handle trivial case
    if n % 2 == 0:
        return 2


    # Repeat until a non-trivial factor is found
    while result == 1:
        x = f(x) % n
        y = f(f(y)) % n

        # Compute GCD of |x - y| and n
        result = gcd(abs(x-y), n)

    # Return the non-trivial factor
    if result != n:
        return result
    
    else:
        raise ValueError("Failed to find a non-trivial prime factor. Try another function or different starting values")
