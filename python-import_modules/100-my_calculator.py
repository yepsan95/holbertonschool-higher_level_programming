#!/usr/bin/python3
if __name__ == '__main__':

    from calculator_1 import add, sub, mul, div
    from sys import argv as argv
    from sys import exit as exit

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op_check = 0
    operators = [["+", add], ["-", sub], ["*", mul], ["/", div]]
    for op in operators:
        if op[0] == argv[2]:
            func = op[1]
            a = int(argv[1])
            b = int(argv[3])
            print("{} {} {} = {}".format(a, op[0], b, func(a, b)))
            op_check = 1
    if op_check == 0:
        print("Unknown operator. Available operators: +, -, * and /")
