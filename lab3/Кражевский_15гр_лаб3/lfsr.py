from functools import reduce
from operator import xor


# implement the lfsr class
class lfsr():
    def __init__(self, fill, taps):
        self.seed = fill
        self.register = fill
        self.taps = taps
        self.len = len(fill)

    def step(self):
        new_bit = reduce(xor, [self.register[(len(self.register)-1)-t]
                         for t in self.taps])
        del self.register[0]
        self.register.append(new_bit)
        return self.register[-1]

    def period(self, fill):
        per = 1
        self.step()
        while self.register != fill:
            per += 1
            self.step()
        return per

    def __str__(self):
        return "{}".format(''.join(map(str, self.register)), self.taps)


if __name__ == '__main__':
    fill = [1, 0, 1, 0, 0]
    register = lfsr(fill=[1, 0, 1, 0, 0], taps={1, 2, 4, 5})

    i = 0
    while True:
        print("Step {}\n{}".format(i+1, register))
        register.step()
        i += 1
        #print(seed, register.register)
        if str(register.register) == str(fill):
            #print(seed, register.register)
            break
    