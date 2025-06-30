# Common Modulus Attack assuming the same message m is encrypted with the same modulo n but different exponents e1 and e2, which are coprime
def common_modulus_attack(c1, c2, e1, e2, n):

    # Find a and b such that a * e1 + b * e2 = 1
    g, a, b = gcd_extended(e1, e2)

    if g != 1:
        raise Exception("e1 and e2 must be coprime")

    # Calculate m = c1^a * c2^b mod n
    # If a is negative, compute the modular inverse of c1 mod n and use a as the exponent
    if a < 0:
        _ ,c1, _ = gcd_extended(c1, n)
        a = -a

    # Same for b and c2
    if b < 0:
        _ ,c2, _ = gcd_extended(c2, n)
        b = -b

    m = (pow(c1, a, n) * pow(c2, b, n)) % n
    return m


# Calculate modulo inverse using the extended Euclidean algorithm
def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = gcd_extended(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y


# Attack demonstration

# Modulo 
n = 3233  

# Public exponents
e1 = 17
e2 = 13

# Plaintext to be encrypted and recovered (ensure m < n)
m = 13
    
# Encryption
c1 = pow(m, e1, n)
c2 = pow(m, e2, n)

print(f"Ciphertexts: {c1}, {c2}")

recovered_m = common_modulus_attack(c1, c2, e1, e2, n)
print("Recovered message:", recovered_m)
