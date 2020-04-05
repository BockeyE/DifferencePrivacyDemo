import math


class Laplace(object):
    def __init__(self):
        self.mtr = None

    def get_laplacian_random_variable(self, scale):
        loc = 0
        rnd = self.mtr.randExc()
        sign = 0
        uniform = 0.5 - rnd
        if uniform >= 0:
            sign = 1
        else:
            sign = -1
        return loc - scale * sign * math.log(1 - 2.0 * math.fabs(uniform))
