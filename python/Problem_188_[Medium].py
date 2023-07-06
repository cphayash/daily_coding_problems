from test_tools import printTestIteration, printTestResults
"""
This problem was asked by Google.

What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
How can we make it print out what we apparently want?
"""


def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist


def make_functions_fixed():
    flist = []

    for i in [1, 2, 3]:
        def print_i(i):
            print(i)
        flist.append((print_i, i))

    return flist


def run_make_functions():
    functions = make_functions()
    for f in functions:
        f()

def run_make_functions_fixed():
    functions = make_functions_fixed()
    for f, i in functions:
        f(i)


run_make_functions()

run_make_functions_fixed()