from typing import List, Set, Tuple
from test_tools import printTestResults, runTest
"""
This problem was asked by Microsoft.

Given an array of positive integers, divide the array into two subsets such that
the difference between the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20},
which has a difference of 5, which is the smallest possible difference.
"""

def splitArray(array: List[int]) -> Tuple[int]:
    set1, set2 = set(), set()
    targetSum = sum(array) / 2

    flip = False
    while array:
        idx = -1 if flip else 0
        flip = not flip
        val = array.pop(idx)
        if (sum(set1) + val > targetSum) or (sum(set1) + val > sum(set2) + val):
            set2.add(val)
        else:
            set1.add(val)

    return (sum(set1), sum(set2))



testCases = [
    {
        "input": [5, 10, 15, 20, 25],
        "expect": (sum({10, 25}), sum({5, 15, 20})),
    },
]

testResults = []
for testCase in testCases:
    testResults.append(runTest(splitArray, testCase))
    
printTestResults(testResults)