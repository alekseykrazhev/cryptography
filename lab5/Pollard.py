from RSA import gcd, fast_pow


def pollard_p(n: int, B: int) -> tuple[int, int]:
    """
    Finds a factors of n using the Pollard p-1 factorization algorithm.
    """
    b = 2

    for i in range(2, B):
        # b is updated as a mod power
        b = fast_pow(b, i, n)
        # d is gcd of b-1 and n
        d = gcd(b-1, n)

        # if d is not 1 or n then a factor has been found
        if 1 < d < n:
            return d, n // d
