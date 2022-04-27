from functools import reduce
from operator import xor


# implement the lfsr class
class lfsr():
    def __init__(self, taps, seed):
        assert max(taps) <= len(seed) and min(taps) > 0
        self.length = len(seed)
        self.taps = taps
        self.seed = int(seed, 2)
        self.register = self.seed

    def make_shift(self):
        new_bit = 0
        for tap in self.taps:
            new_bit ^= self.register >> tap - 1
        new_bit &= 1
        self.register = (self.register << 1) | new_bit
        self.register &= (1 << self.length) - 1
        return new_bit

    def get_period(self):
        result = 1
        self.make_shift()
        while self.register != self.seed:
            self.make_shift()
            result += 1
        return result


if __name__ == '__main__':
    fill = [1, 0, 1, 0, 0]
    register = lfsr({1, 2, 4, 5}, "10100")
    '''
    fill2 = [1, 0, 1, 1, 0, 0, 0]
    fill3 = [0, 1, 0, 0, 0, 1, 1, 0]
    seq2 = lfsr(fill=[1, 0, 1, 1, 0, 0, 0], taps={4, 5, 6, 7})
    seq3 = lfsr(fill=[0, 1, 0, 0, 0, 1, 1, 0], taps={2, 5, 6, 8})
    '''
    i = 0
    while True:
        print("step {}\n{}".format(i+1, register))
        register.make_shift()
        i += 1
        #print(seed, register.register)
        if register.register == register.seed:
            #print(seed, register.register)
            break

    print("period: {}".format(register.get_period()))
