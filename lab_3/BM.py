# implement Berlekamp-Massey algorithm

from lfsr import lfsr


# implementation of Berlekamp-Massey algorithm
def BerlMessi(sequence):
    # initialization
    n = len(sequence)
    r = [0] * n
    d = [0] * n
    d[0] = 1
    r[0] = 1
    r[1] = 1
    d[1] = 1
    # main loop
    for i in range(2, n):
        if sequence[i - 1] == sequence[i - 2]:
            r[i] = r[i - 1] + r[i - 2]
            d[i] = d[i - 1] + d[i - 2]
        else:
            r[i] = r[i - 1]
            d[i] = d[i - 1]
    # termination
    return r, d


if __name__ == '__main__':
    fill = [1, 0, 1, 0, 0]
    register = lfsr({1, 2, 4, 5}, "10100")

    fout = open("sequence.bin", "w")
    while True:
        fout.write(str(register.make_shift()))
        #fout.write("\n")
        # print(seed, register.register)
        if register.register == register.seed:
            # print(seed, register.register)
            break
    fout.close()

    fout = open("sequence.bin", "r")
    x = fout.readline()
    fout.close()
    #x = [int(i) for i in x]
    r, d = BerlMessi(x)
    print("r:", r)
    #print("c:", c)
    print("d:", d)

