# lab 5 var 8 RSA encryption and decryption by Aleksey Krazhevskiy

from RSA import *


if __name__ == '__main__':
    p = 1102914252601991
    q = 571301412050021
    e = 624840313709071966800768010501
    x1 = 267222621555915275276288463243
    y2 = 291064433434228628162063527294

    print(f"p = {p}")
    print(f"q = {q}")

    # key[0] = public key, key[1] = private key
    key = generate_keypair(p, q, e)
    print('Public key (key, n):', key[0])
    print('Private key (key, n):', key[1])

    y1 = encrypt(key[0], x1)
    print(f"Encrypted y1 = {y1}")

    x1_ = decrypt(key[1], y1)
    print(f"Decrypted x1 = {x1_}")
    print(f"Check x1: {x1 == x1_}")

    x2 = decrypt(key[1], y2)
    print(f"Decrypted x2 = {x2}")
    print(f"y2 = {y2}")
