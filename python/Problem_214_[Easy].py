import sys
from test_tools import runAllTests
"""
This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in
its binary representation.

For example, given 156, you should return 3.
"""

def getLongestRunOfOnes(val: int) -> int:
    base2 = bin(val)[2:] # This is a str now
    longestRun = 0
    count = 0
    for i in range(len(base2)):
        charVal = int(base2[i])
        prev = int(base2[i-1] if i > 0 else 0)
        if charVal == 1:
            if not prev:
                count = 0    
            count += 1
        if count > longestRun:
            longestRun = count
    return longestRun


def main():
    testCases = [
        {
            "input": 156,
            "expect": 3,
        },
        {
            "input": 1156,
            "expect": 1,
        },
        {
            "input": 317,
            "expect": 4,
        },
    ]

    runAllTests(getLongestRunOfOnes, testCases)


if __name__ == '__main__':
    main()