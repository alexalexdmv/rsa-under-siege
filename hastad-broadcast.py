# Håstad’s Broadcast Attack assuming same message encrypted under different moduli with same exponent e.
# Arguments:
# - cipher_list: list of ciphertexts (c_i = m^e mod n_i), intercepted from different recipients
# - n_list: list of the corresponding RSA moduli n_i
# - e: the common public exponent (intentionally small for demonstration)
def hastad_broadcast(cipher_list, n_list, e):

    x = crt(cipher_list, n_list)

    m = nthRoot(e, x)


    return m

# Calculate the Chinese Remainder Theroem in order to reconstruct m^e modulo N, where N is the product of all moduli
# Note: the different moduli have to be pairwise coprime
def crt(cipher_list, n_list):
    
    N = 1

    for n in n_list:
        N *= n
    
    result = 0

    for c_i, n_i in zip(cipher_list, n_list):

        N_i = N // n_i
        _, inv, _ = inverse(N_i, n_i)
        result += c_i * N_i * inv

    return result % N

# Calculate the modulo inverse using the extended Euclidean algorithm
def inverse(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = inverse(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Compute the n-th root
def nthRoot(n, m):

    low, high = 1, m

    while low <= high:

        mid = (low + high) // 2
        power = mid ** n

        if power == m:

            return mid
        
        elif power < m:

            low = mid + 1

        else:

            high = mid - 1

    return high  




# Attack demonstration

#Small public exponent
e = 3

#
n_list = [61, 67, 71]

# Plaintext message to be encrypted and recovered in the attack (ensure m^e < product of all n_i)
m = 59

cipher_list = [pow(m, e, n) for n in n_list]
print("Ciphertexts:", cipher_list)

recovered_m = hastad_broadcast(cipher_list, n_list, e)
print("Recovered message:", recovered_m)

