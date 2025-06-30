import random
from math import gcd

# This function simulates the quantum computed part of Shor's algorithm
def find_period_sim(a: int, n: int) -> int:
    # Find the smallest r such that a^r ≡ 1 mod N
    r = 1
    value = pow(a, r, n)
    
    while value != 1 and r < n:
        r += 1
        value = pow(a, r, n)
    
    # If no period found, fail
    if pow(a, r, n) != 1:
        raise ValueError("No period found (r)")
    
    return r

def shor_classical(n: int, max_attempts: int = 10):
    
    # Trivial case: n is even
    if n % 2 == 0:
        return 2, n // 2

    for _ in range(max_attempts):

        # Choose random base a
        a = random.randint(2, n - 2)
        print(f"Trying a = {a}")

        # Early exit if gcd(a,n) is not 1 [Found a non-trivial factor]
        d = gcd(a, n)

        if d > 1:
            print(f"Found factor gcd({a}, {n}) = {d}")
            return d, n // d

        try:
            # Simulate period finding
            r = find_period_sim(a, n)
            print(f"Found period r = {r}")

        except ValueError:
            continue

        # Period must be even
        if r % 2 != 0:
            print(f"r = {r} is odd, trying another base a")
            continue

        # Compute x = a^(r/2) mod n
        x = pow(a, r // 2, n)

        # Reject trivial roots of unity
        if x == n - 1 or x == 1:
            print("Trivial root of unity, trying another base a")
            continue

        # Return factors
        p = gcd(x + 1, n)
        
        if 1 < p < n:
            return p, n // p

    # If no factors found in all attempts
    raise ValueError(f"Failed to factor n = {n} after {max_attempts} attempts.")

# Attack demonstration

# Public exponent N
N = 1357
print(f"Factoring N = {N} using Shor's algorithm")

try:
    p, q = shor_classical(N)
    print(f"\nSuccess! Factors of {N}: {p} × {q}")

except ValueError as e:
    print(str(e))
