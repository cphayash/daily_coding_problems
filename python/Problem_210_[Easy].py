from test_tools import printTestIteration, printTestResults
"""
This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any
positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test
this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
"""


def computeCollatzSequence(n: int) -> int:
    if n < 2:
        return n
    if n % 2: # value is odd
        return computeCollatzSequence(3 * n + 1)
    else:
        return computeCollatzSequence(n / 2)
    

def checkIfCollatzEqualsOne(n: int) -> bool:
    return computeCollatzSequence(n) == 1


testCases = [
    {
        "input": 5,
        "expect": True,
    },
    {
        "input": 1,
        "expect": True,
    },
    {
        "input": 17,
        "expect": True,
    },
    {
        "input": 77,
        "expect": True,
    },
]


testResults = []

for testCase in testCases:
    inputVal = testCase["input"]
    expect = testCase["expect"]
    result = checkIfCollatzEqualsOne(inputVal)
    testResults.append(result == expect)
    printTestIteration(inputVal, result, expect)
printTestResults(testResults)