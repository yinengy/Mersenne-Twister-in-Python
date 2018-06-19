# MT19937
(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 1812433253
# make a arry to store the state of the generator
MT = [0 for i in range(n)]
index = n+1
lower_mask = int(bin(1 << r), 2) - 0b1
upper_mask = int(str(-~lower_mask)[-w:])


class Random():
    def __init__(self, c_seed=0):
        self.c_seed = c_seed
        self.seed(c_seed)

    def seed(self, num):
        """initialize the generator from a seed"""
        global w, n, m, r, a, u, d, s, b, t, c, l, f, MT, index, lower_mask, upper_mask
        MT[0] = num
        index = n
        for i in range(1, n):
            temp = f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i
            MT[i] = int(str(temp)[-w:])

    def twist(self):
        """ Generate the next n values from the series x_i"""
        global w, n, m, r, a, u, d, s, b, t, c, l, f, MT, index, lower_mask, upper_mask
        for i in range(0, n):
            x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
            xA = x >> 1
            if (x % 2) != 0:
                xA = xA ^ a
            MT[i] = MT[(i + m) % n] ^ xA

    def extract_number(self):
        """ Extract a tempered value based on MT[index]
            calling twist() every n numbers
        """
        global w, n, m, r, a, u, d, s, b, t, c, l, f, MT, index, lower_mask, upper_mask
        if index >= n:
            self.twist()
            index = 0

        y = MT[index]
        y = y ^ ((y >> u) & d)
        y = y ^ ((y << t) & c)
        y = y ^ ((y << s) & b)
        y = y ^ (y >> l)

        index += 1
        return int(str(y)[-w:])

    def random(self):
        """ return uniform ditribution in [0,1) """
        return self.extract_number() / 10**32

    def randint(self, a, b):
        """ return random int in [a,b) """
        n = self.random()
        return int(n/(1/(b-a)) + a)

    def shuffle(self, X):
        """ shuffle the sequence """
        newX = list(X)
        for i in range(10*len(X)):
            a = self.randint(0, len(X))
            b = self.randint(0, len(X))
            newX[a], newX[b] = newX[b], newX[a]

        return newX

    def choice(self, X, replace=True, size=1):
        """ choice an element randomly in the sequence 
            size: the number of element to be chosen
        """
        newX = list(X)
        if size == 1:
            return newX[self.randint(0, len(newX))]
        else:
            if replace:
                return [newX[self.randint(0, len(newX))] for i in range(size)]
            else:
                l = []
                for i in range(size):
                    if len(newX) != 0:
                        a = self.randint(0, len(newX))
                        l += [newX[a]]
                        newX.remove(newX[a]) 
                return l

    def bern(self, p):
        """ generate a Bernoulli Random Variable
            p: the probability of True
        """
        return self.random() <= p

    def binomial(self, N, p):
        """ generate a Binomial Random Variable
            N: total times
            p: probability of success
        """
        a = [self.bern(p) for n in range(N)]
        return a.count(True)

    def geometric(self, p):
        """ generate a Geometric Random Variable
            p: probability of success
        """
        u = self.random()
        b = 0
        k = 1
        while b < u:
            b += (1-p)**(k-1)*p
            k += 1

        return k - 1
