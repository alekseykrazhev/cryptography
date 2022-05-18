# cryptography lab3 var8 Krazhevskiy
from lfsr import lfsr


# implement the geffe generator class
class Geffe:
    def __init__(self, seq1 : lfsr, seq2 : lfsr, seq3 : lfsr):
        self.seq1 = seq1
        self.seq2 = seq2
        self.seq3 = seq3
    
    def step(self):
        s1 = self.seq1.make_shift()
        return (s1 & self.seq2.make_shift()) ^ ((s1 ^ 1) * self.seq3.make_shift())

    def periods(self) -> list:
        return [self.seq1.get_period(), self.seq2.get_period(), self.seq3.get_period()]


if __name__ == '__main__':
    fill1 = [1, 0, 1, 0, 0]
    fill2 = [1, 0, 1, 1, 0, 0, 0]
    fill3 = [0, 1, 0, 0, 0, 1, 1, 0]
    seq1 = lfsr(taps={5, 4, 2, 1}, seed="10100")
    seq2 = lfsr(taps={7, 6, 5, 4}, seed="1011000")
    seq3 = lfsr(taps={8, 6, 5, 2}, seed="01000110")

    geffe = Geffe(seq1, seq2, seq3)
    print('{} periods'.format(geffe.periods()))
    seq = [geffe.step() for _ in range(10000)]
    zeros = seq.count(0)

    print('{} zeros'.format(zeros))
    print('{} ones'.format(len(seq) - zeros))

    for i in range(1, 6):
        r = 0
        for j in range(0, 10000 - i, i):
            r += (-1) ** (seq[j] ^ seq[j + i])
        print("r_{}: {}".format(i, r), end=', ')
    
