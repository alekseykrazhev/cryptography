# cryptography lab3 var8 Krazhevskiy
from lfsr import lfsr


# implement the geffe generator class
class Geffe:
    def __init__(self, seq1 : lfsr, seq2 : lfsr, seq3 : lfsr):
        self.seq1 = seq1
        self.seq2 = seq2
        self.seq3 = seq3
    
    def step(self):
        return (self.seq1.step() & self.seq2.step()) ^ ((self.seq1.step() ^ 1) * self.seq3.step())

    def periods(self, fill1, fill2, fill3):
        return [self.seq1.period(fill1), self.seq2.period(fill2), self.seq3.period(fill3)]


if __name__ == '__main__':
    fill1 = [1, 0, 1, 0, 0]
    fill2 = [1, 0, 1, 1, 0, 0, 0]
    fill3 = [0, 1, 0, 0, 0, 1, 1, 0]
    seq1 = lfsr(fill=fill1.copy(), taps={5, 4, 2, 1})
    seq2 = lfsr(fill=fill2.copy(), taps={7, 6, 5, 4})
    seq3 = lfsr(fill=fill3.copy(), taps={8, 6, 5, 2})

    geffe = Geffe(seq1, seq2, seq3)
    seq = [geffe.step() for _ in range(10000)]
    zeros = seq.count(0)

    print('{} zeros'.format(zeros))
    print('{} ones'.format(len(seq) - zeros))
    print('{} periods'.format(geffe.periods(fill1, fill2, fill3)))

    for i in range(1, 6):
        r = 0
        for j in range(0, 10000 - i, i):
            r += (-1) ** (seq[j] ^ seq[j + i])
        print("r_{}: {}".format(i, r))
    
