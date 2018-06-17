import random as rnd
import sexpdata as sp
from math import fabs, sqrt, log2, e, fmod, floor
from expression_generator import ExpressionGenerator as eg


class TreeExpression(object):
    def __init__(self):
        self.root = None
        self.children = []
        self.fitness = 0

    def from_s_expression(self, parsed_expr):
        if type(parsed_expr) == list:
            self.root = sp.dumps(parsed_expr[0])
            for elem in parsed_expr[1:]:
                child = TreeExpression().from_s_expression(elem)
                self.children.append(child)
        else:
            self.root = parsed_expr
            self.children = None
        return self

    def random_init(self, height):
        if height != 0:
            self.root = eg.random_operator()
            for i in range(eg.operators[self.root]):
                self.children.append(TreeExpression().random_init(height - 1))
        else:
            self.root = eg.random_terminal()
            self.children = None
        return self

    def mutate(self, chi):
        if rnd.uniform(0, 1) < chi:
            return TreeExpression().random_init(3)
        elif self.children is None:
            return self
        else:
            child = rnd.randint(0, len(self.children) - 1)
            self.children[child] = self.children[child].mutate(chi)
        return self

    def to_s_expression(self):
        if self.children is None:
            return self.root
        else:
            return '(' + self.root + ' ' + ' '.join([str(x.to_s_expression()) for x in self.children]) + ')'

    def evaluate_expression(self, x):
        if self.children is None:
            return self.root
        else:
            return self.eval_func(x, *[child.evaluate_expression(x) for child in self.children])

    def eval_func(self, x, *args):
        n = len(x)
        try:
            if self.root == 'add':
                return args[0] + args[1]
            elif self.root == 'sub':
                return args[0] - args[1]
            elif self.root == 'mul':
                return args[0] * args[1]
            elif self.root == 'div':
                return 0 if args[1] == 0 else args[0] / args[1]
            elif self.root == 'pow':
                return 0 if args[0] < 0 and int(args[1]) != args[1] or args[0] == 0 else args[0] ** args[1]
            elif self.root == 'sqrt':
                return sqrt(args[0]) if args[0] >= 0 else 0
            elif self.root == 'log':
                return log2(args[0]) if args[0] > 0 else 0
            elif self.root == 'exp':
                return e ** args[0]
            elif self.root == 'max':
                return max(args)
            elif self.root == 'ifleq':
                return args[2] if args[0] <= args[1] else args[3]
            elif self.root == 'data':
                return x[int(fmod(fabs(floor(args[0])), n))]
            elif self.root == 'diff':
                return x[int(fmod(fabs(floor(args[0])), n))] - x[int(fmod(fabs(floor(args[1])), n))]
            elif self.root == 'avg':
                k = int(fmod(fabs(floor(args[0])), n))
                l = int(fmod(fabs(floor(args[1])), n))
                if k == l:
                    return 0
                size = fabs(k - l)
                size = size if size != 0 else 1
                s = sum(x[min([k, l]): max([k, l])])
                return s / size
        except OverflowError:
            return 0
