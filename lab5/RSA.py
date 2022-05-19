# implementation of RSA encryption and decryption


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor
    """
    while b != 0:
        a, b = b, a % b
    return a


def fast_pow(a, n, mod=1):
    """
    Algorithm for fast exponentiation using binary exponentiation
    """
    res = 1
    while n:
        if n & 1:
            res *= a % mod
        a *= a % mod
        n >>= 1
    return res % mod


def eea(a, b):
    if b == 0:
        return 1, 0
    (q, r) = (a//b, a % b)
    (s, t) = eea(b, r)
    return t, s - (q * t)


def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative inverse of two numbers
    """
    inv = eea(e, phi)[0]
    if inv < 1:
        inv += phi
    return inv


def is_prime(num):
    """
    Tests to see if a number is prime.
    """
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p: int, q: int, e: int) -> ((int, int), (int, int)):
    """
    Generates a public and private key pair.
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q

    phi = (p - 1) * (q - 1)

    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(pk, plaintext: int) -> int:
    """
    Encrypts a plaintext using a public key.
    """
    key, n = pk
    cipher = fast_pow(int(plaintext), key, n)
    return cipher


def decrypt(pk, ciphertext: int) -> int:
    """
    Decrypts a ciphertext using a private key.
    """
    key, n = pk
    plain = fast_pow(int(ciphertext), key, n)
    return plain
