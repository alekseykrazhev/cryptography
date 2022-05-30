# implement Berlekamp-Massey algorithm

from lfsr import lfsr


# Berlekamp-Massey algorithm
def BM(x):
    # x: input sequence
    # return: (r, c, d)
    # r: remainder sequence
    # c: correction sequence
    # d: degree of correction sequence
    n = len(x)
    r = [0] * n
    c = [0] * n
    d = 0
    for i in range(n):
        r[i] = x[i]
        for j in range(i):
            if r[j] == r[i]:
                c[i] = 1
                break
        if c[i] == 0:
            d = i
    return r, c, d


if __name__ == '__main__':
    fill = [1, 0, 1, 0, 0]
    register = lfsr({1, 2, 4, 5}, "10100")

    fout = open("sequence.bin", "w")
    while True:
        fout.write(str(register.make_shift()))
        fout.write("\n")
        # print(seed, register.register)
        if register.register == register.seed:
            # print(seed, register.register)
            break
    fout.close()

    fout = open("sequence.bin", "r")
    x = fout.readlines()
    fout.close()
    x = [int(i) for i in x]
    r, c, d = BM(x)
    print("r:", r)
    print("c:", c)
    print("d:", d)

