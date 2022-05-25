# implementation of Elgamal encryption scheme

import random
from SHA_2 import sha256


def gcd(a, b):
    """
    Euclid's extended algorithm for finding the greatest common divisor of two numbers
    """
    while b:
        a, b = b, a % b
    return a


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


def generate_key(q: int) -> (int, int, int, int, int):
    """
    Generates a public and private key for the Elgamal encryption scheme.
    :param q: prime number
    :return: CP params, public key, private key
    """
    print('Generating key', end='')
    while True:
        print('.', end='')
        R = random.randint(2, 4 * (q + 1) - 5)
        if R % 2 != 0:
            R += 1

        p = R * q + 1
        if fast_pow(2, q * R, p) != 1 or fast_pow(2, R, p) == 1:
            pass
        else:
            print('Finally!')
            break

    while True:
        x = random.randint(1, p - 2)
        g = fast_pow(x, R, p)
        if g != 1:
            break

    d = random.randint(1, q - 2)
    e = fast_pow(g, d, p)

    return p, q, g, e, d


def sign(p: int, q: int, g: int, d: int, M: str) -> (int, int):
    """
    Signs the message m with the private key x.
    :param p: CP params
    :param q: CP params
    :param g: CP params
    :param d: private key
    :param M: message
    :return: signature
    """
    # count hash value of message
    m = sha256(M)

    while True:
        k = random.randint(1, p - 2)
        if gcd(k, p - 1) == 1:
            break

    r = fast_pow(g, k, p) % p
    temp = multiplicative_inverse(k, q)

    s = temp * (int(m, base=16) - r * d) % q
    return r, s


def verify(p: int, q: int, g: int, e: int, M: str, r: int, s: int) -> bool:
    """
    Verifies the signature of the message m with the public key e.:
    :param p: CP params
    :param q: CP params
    :param g: CP params
    :param e: public key
    :param M: message
    :param r: signature
    :param s: signature
    :return: True if signature is valid, False otherwise
    """
    if r < 1 or r > p or s < 1 or s > q:
        return False

    # count hash value of message M
    m = sha256(M)

    return (fast_pow(e, r, p) * fast_pow(r, s, p)) % p == fast_pow(g, int(m, base=16), p)

