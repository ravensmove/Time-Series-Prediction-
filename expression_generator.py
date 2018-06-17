import random as rnd

class ExpressionGenerator(object):
    operators = {
        'add': 2,
        'sub': 2,
        'mul': 2,
        'div': 2,
        'pow': 2,
        'sqrt': 1,
        'log': 1,
        'exp': 1,
        'max': 2,
        'ifleq': 4,
        'data': 1,
        'diff': 2,
        'avg': 2
    }

    @staticmethod
    def random_operator():
        n = len(ExpressionGenerator.operators)
        return list(ExpressionGenerator.operators.keys())[rnd.randint(0, n - 1)]

    @staticmethod
    def random_terminal():
        return rnd.gauss(0, 2)
