
# The gcd function takes two integers and finds the greatest common divisor
def gcd(a, b):
    """
        Euclid's algorithm for determining the greatest common divisor
        """
    while b != 0:
        a, b = b, a % b
    return a


# The Pollard p-1 factorization algorithm
def pollard_p(n: int, B: int) -> tuple[int, int]:
    """
    Finds a factors of n using the Pollard p-1 factorization algorithm.
    """
    # start with b as 2 and user input upper bound
    b = 2

    # run through all values between 2 and bound
    for i in range(2, B):
        # b is updated as a mod power
        b = pow(b, i, n)
        # d is gcd of b-1 and n
        d = gcd(b-1, n)

        # if d is not 1 or n then a factor has been found
        if 1 < d < n:
            return d, n // d
