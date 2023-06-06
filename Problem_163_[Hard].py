from typing import List, Union
from test_tools import printAllMatch, printExpect, printResult, printTestResults
"""
This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a program to
evaluate it.

The expression is given as a list of numbers and operands.
For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
should return 5,
since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""

def evaluateRPN(array: List[Union[int, str]]) -> int:
    operators = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    stack = []

    for item in array:
        print(stack)
        if item not in operators:
            stack.append(int(item))
        else:
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(operators[item](v1, v2))

    return stack[-1]


def evalRPN(self, tokens: List[Union[int, str]]) -> int:
    operands = []
    operators = {'+', '-', '*', '/'}
    for item in tokens:
        if item not in operators:
            operands.append(int(item))
        else:
            v2 = operands.pop()
            v1 = operands.pop()
            match item:
                case '+':
                    operands.append(v1 + v2)
                case '-':
                    operands.append(v1 - v2)
                case '*':
                    operands.append(v1 * v2)
                case '/':
                    operands.append(int(v1/v2))
    return operands[-1]


def add(v1: int, v2: int) -> int:
    return v1 + v2

def subtract(v1: int, v2: int) -> int:
    return v1 - v2

def multiply(v1: int, v2: int) -> int:
    return v1 * v2

def divide(v1: int, v2: int) -> int:
    return int(v1 / v2)

testCases = [
    {
        "input": [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'],
        "expect": 5,
    },
    # {
    #     "input": ["2","1","+","3","*"],
    #     "expect": 9,
    # },
]

testResults = []
for testCase in testCases:
    array = testCase["input"]
    expect = testCase["expect"]
    # res = evaluateRPN(array)
    res = evalRPN(array)
    match = res == expect
    testResults.append(match)
    printResult(res)
    printExpect(expect)
    print(match)

printTestResults(testResults)
printAllMatch(testResults)