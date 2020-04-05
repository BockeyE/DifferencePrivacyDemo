import math
import time


class MTRand(object):

    def __init__(self):
        self.N = 624
        self.SAVE = self.N + 1
        self.M = 397
        self.pNext = 0
        self.state = []
        self.left = 0

    def rand(self):
        return float(self.randInt()) * (1.0 / 4294967295.0)

    def rand1(self, n):
        return self.rand() * n

    def randInt(self):
        if self.left == 0:
            self.reload()
        self.left = self.left - 1

        s1 = 0
        self.pNext = self.pNext + 1
        s1 = self.pNext
        s1 = s1 ^ (s1 >> 11)
        s1 = s1 ^ (s1 << 7) & 0x9d2c5680
        s1 ^= (s1 << 15) & 0xefc60000
        return s1 ^ (s1 >> 18)

    def randInt1(self, n):
        used = n
        used |= used >> 1
        used |= used >> 2
        used |= used >> 4
        used |= used >> 8
        used |= used >> 16
        i = self.randInt1() & used
        while i > n:
            i = self.randInt1() & used
        return i

    def randNorm(self, mean, variance):
        r = math.sqrt(-2.0 * math.log(1.0 - self.randDblExc())) * variance
        phi = 2.0 * 3.14159265358979323846264338328 * self.randExc()
        return mean + r * math.cos(phi);

    def randDblExc1(self, n):
        return self.randDblExc1() * n

    def randDblExc(self):
        return (float(self.randInt1())) * (1.0 / 4294967296.0)

    def randExc1(self, n):
        return self.randExc1() * n

    def randExc(self):
        return (float(self.randInt1()) + 0.5) * (1.0 / 4294967296.0)

    def rand53(self):
        a = self.randInt() >> 5
        b = self.randInt() >> 6
        return (a * 67108864.0 + b) * (1.0 / 9007199254740992.0)

    def seed(self):
        return self.seed1(self.hash())

    def seed1(self, oneseed):
        self.initialize(oneseed)
        self.reload()
        return

    def seed2(self, bigSeed, seedLength):
        self.initialize(19650218)
        i = 1
        j = 0
        k = max(self.N, seedLength)
        self.state[0] = 0x80000000
        self.reload()
        return

    def initialize(self, seed):
        s = self.state
        r = self.state

        s[1] = seed & 0xffffffff

        for i in range(1, self.N):
            s[i] = (1812433253 * (r[i] ^ (r[i] >> 30)) + i) & 0xffffffff

    def reload(self):
        i = self.N - self.M
        while i > 0:
            self.state = self.twist(self.state[self.M], self.state[0], self.state[1]);
            i = i - 1
        i = self.M
        while i > 0:
            self.state = self.twist(self.state[self.M - self.N], self.state[0], self.state[1]);
            i = i - 1
        left = N, pNext = self.state;

    def load(self, loadArray):
        s = self.state;
        la = loadArray;
        i = self.N;

    def hash(self):
        return int(time.time()) ^ 3
