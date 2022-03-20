import random
import math
from bitarray import bitarray


def fermat(n, presicion):
    for a in range(presicion):
        a = random.randint(1, n-1)

        if math.gcd(a, n) != 1:
            return False

        if (a ** (n-1)) % n != 1:
            return False

    return True


def miller_rabin(n, presicion = 1):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(presicion):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break

            if x == 1:
                return False

        return False

    return True


def mersen(n):
    return 2 ** n - 1


def luke_lemer(mersen, p):
    s = 4
    k = 1

    while k != p - 1:
        s = ((s ** 2) - 2) % mersen
        k += 1

    if s == 0:
        return True
    else:
        return False


def high_border(num):
    counter = 1
    for _ in range(1, num):
        counter *= 2
        counter += 1
    return counter


def less_border(num):
    counter = 1
    for _ in range(1, num):
        counter *= 2
    return counter


def generate(b_size, high, less):
    n = bitarray(b_size)
    for i in range(len(n)):
        n[i] = random.randint(0, 1)
    #num = int(struct.unpack("<L", n)[0])
    num = int(n.to01(), 2)
    if num < 0:
        num *= -1
    cent = high - less + 1
    num %= cent
    num += less
    return num


if __name__ == '__main__':
    b_size = int(input('Enter bit size:'))

    high = high_border(b_size)
    less = less_border(b_size)
    num = generate(b_size, high, less)
    counter = 0

    while not miller_rabin(num):
        num = generate(b_size, high, less) 
        counter += 1

    print('Generated number = ', num, ' whithin ', counter, 'tries.')

    print('Test results:')
    print('\tMiller-Rabin test: ', miller_rabin(num, 40))
    print('\tFermet test: ', fermat(num, 30))

    mersen_num = int(input('Enter pow of mersen number (prime):'))
    n = mersen(mersen_num)
    print('Mersen number = ', n)
    print('\tLuke-Lemer test for mersen number: ', luke_lemer(n, mersen_num))

