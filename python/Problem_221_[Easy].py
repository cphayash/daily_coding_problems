
import sys
from test_tools import runAllTests

"""
This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of 7, or the
sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and
so on. Create an algorithm to find the nth sevenish number.
"""


def findNthSevenishNum(n: int) -> int:
    cur = 1
    curIter = 1
    while cur < n:
        curIter += 1
        cur += curIter

    cur -= curIter
    result = 7 ** (curIter - 1)
    curToAdd = 1

    for _ in range(n - cur - 1):
        result += curToAdd
        curToAdd *= 7
    return result


def main():
    testCases = [
        {
            "input": 1,
            "expect": 1,
        },
        {
            "input": 2,
            "expect": 7,
        },
        {
            "input": 3,
            "expect": 8,
        },
        {
            "input": 4,
            "expect": 49,
        },
        {
            "input": 5,
            "expect": 50,
        },
        {
            "input": 6,
            "expect": 57,
        },
    ]

    runAllTests(findNthSevenishNum, testCases)


if __name__ == '__main__':
    main()