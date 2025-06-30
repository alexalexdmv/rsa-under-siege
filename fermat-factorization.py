from math import isqrt

def fermatFactor(n: int):

    # Handle trivial case
    if n % 2 == 0:
        return 2
    
    # Start with the ceiling of the square root of n
    a = isqrt(n)
    if a*a < n:

        a = a + 1

    # Compute b^2 = a^2 - n
    b_squared = a * a - n

    # Increment a until b_squared becomes a perfect square
    while not is_perfect_square(b_squared):

        a += 1
        b_squared = a * a - n

    # Once b_squared is a perfect square, compute b = sqrt(b_squared)
    b = isqrt(b_squared)

    # Return the two non-trivial factors: (a - b) and (a + b)
    return (a-b, a+b)

# Helper function
def is_perfect_square(x: int):
    
    y = isqrt(x)

    return y * y == x  


# Attack demonstration

# Public modulo n
n = 8567

p, q = fermatFactor(n)

print(f"The factors are {p} and {q}")