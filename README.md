
# RSA Attacks

  

This repository contains implementations of attacks on RSA encryption. Each script demonstrates how RSA can be broken under specific conditions using number-theoretic techniques and algorithms.

  

> These implementations are for educational and research purposes only. Do **not** use them on systems without permission.

---
## Attack Summaries

  

### 🔹 Fermat’s Factorization

  

> Assumes `n = p * q` and works the best if `|p − q|` is small.

> Expresses `n = a² − b²`, then solves for `a` and `b` to recover `p` and `q`, which will be used to derive `d` (the RSA private key).

---
### 🔹 Pollard’s Rho

  

> Efficient probalistic factorization algorithm for finding non-trivial divisors of `n`, in order to be able to derive `d` (the RSA private key).

> Uses cycle detection in pseudorandom sequences defined by a function (e.g. `f(x) = x² + 1 mod N`).

  

---
  

### 🔹 Håstad’s Broadcast Attack

> If the same message is encrypted with the same small exponent `e` but different moduli,
 we can reconstruct the message using the Chinese Remainder Theorem (CRT).

Conditions:

* Same `m` sent to different recipients

* Same public exponent `e` 

* Enough ciphertexts (at least `e`)

---
### 🔹 Common Modulus Attack
>Exploits the reuse of the same RSA modulus `n` with different public exponents `e1`, `e2`.  
If ciphertexts `c1 = m^e1 mod n` and `c2 = m^e2 mod n` are known, and `e1` and `e2` are coprime, the original message `m` can be recovered using the Extended Euclidean Algorithm.
---
  

### 🔹 Shor’s Algorithm (Simulation)

  

> Quantum-computed algorithm that can factor a large integer `n` in polynomial time, which is way faster than all classical methods (including GNFS).
> The quantum part (period finding) is classically simulated for demonstration purposes in this implementation.

> Note: While Shor's algorithm is a threat to RSA, post-quantum cryptographic schemes (e.g. hash-based crypto) are being developed to withstand quantum attacks.

  

---

  

## Notes

  

* The scripts use **small key sizes** and **simplified logic** for demonstration only.

* In practice, RSA implementations use padding and long primes to make these attacks more difficult.
* All files contain an attack demonstration.



  

---

## References

* [RSA Cryptosystem](https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29)

* [Håstad's Broadcast Attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack)

* [Common Modulus Attack](https://www.rose-hulman.edu/class/ma/holden/Archived_Courses/Math479-0304/resources/attacks-rsa/)

* [Pollard’s Rho Algorithm](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm)

* [Fermat’s Factorization](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method)

* [Shor’s Algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm)

---

