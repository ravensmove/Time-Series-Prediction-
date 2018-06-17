import sys


class DataHolder(object):
    def __init__(self, n, m):
        self.x = []
        self.y = []
        self.m = m
        self.n = n

    def load_data(self, file):
        with open(file, 'r') as open_file:
            for line in open_file.readlines():
                self.x.append([float(i) for i in line.split('\t')])
                self.y.append(self.x[-1][-1])
                self.x[-1] = self.x[-1][: len(self.x[-1]) - 1]

    def evaluate_expression(self, expr):
        se_sum = 0
        try:
            for i in range(self.m):
                exp_val = expr.evaluate_expression(self.x[i])
                se_sum += (self.y[i] - exp_val) ** 2
            return se_sum / self.m
        except OverflowError:
            return sys.float_info.max
