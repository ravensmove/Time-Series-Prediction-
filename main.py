import sexpdata as spd
import argparse
import sys
from data_holder import DataHolder
from genetic_algorithm import GeneticAlgorithm
from tree_expr import TreeExpression
import csv


def main():
    parser = argparse.ArgumentParser(description='Genetic programming.')
    parser.add_argument('-question', help='Question number', type=int, required=True)
    parser.add_argument('-n', type=int)
    parser.add_argument('-m', type=int)
    parser.add_argument('-x', type=str)
    parser.add_argument('-expr', type=str)
    parser.add_argument('-data', type=str)
    parser.add_argument('-lambda', type=int)
    parser.add_argument('-time_budget', type=int)

    args = parser.parse_args()
    question = args.question

    if question == 1:
        x = [float(i) for i in args.x.split(' ')]
        expr = spd.loads(args.expr)
        tree_exp = TreeExpression().from_s_expression(expr)
        print(tree_exp.evaluate_expression(x))
    elif question == 2:
        data_holder = DataHolder(args.n, args.m)
        data_holder.load_data(args.data)
        expr = spd.loads(args.expr)
        tree_exp = TreeExpression().from_s_expression(expr)
        print(data_holder.evaluate_expression(tree_exp))
    elif question == 3:
        lmbd = int(get_argument_value('-lambda', sys.argv[1:]))
        data_holder = DataHolder(args.n, args.m)
        data_holder.load_data(args.data)
        ga = GeneticAlgorithm(lmbd=lmbd, n=args.n, m=args.m, k=5, chi=0.3, max_height=5, time_budget=args.time_budget,
                              data=data_holder)

        # print(ga.run_ga().fitness)
        print(ga.run_ga().to_s_expression())



def get_argument_value(argument, args_list):
    return args_list[args_list.index(argument) + 1]


if __name__ == '__main__':
    main()
