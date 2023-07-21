from test_tools import runAllTests
from typing import List

"""
This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not the sum of
a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
"""


def findSmallestUnique(array: List[int]) -> int:
    runningSum = 1
    for val in array:
        if val <= runningSum:
            runningSum += val
        else:
            return runningSum
        

def main():
    testCases = [
        {
            "input": [1, 2, 3, 10],
            "expect": 7,
        },
        {
            "input": [1, 2, 5, 10],
            "expect": 4,
        },
    ]

    runAllTests(findSmallestUnique, testCases)


if __name__ == "__main__":
    main()