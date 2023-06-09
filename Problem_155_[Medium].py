from typing import List
from collections import Counter
from test_tools import printTestResults, runTest
"""
This problem was asked by MongoDB.

Given a list of elements, find the majority element, which appears more than
half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""

# Time: O(n) | n is len(array)
# Space: O(n) | n is len(array)
def findMajElement(array: List[int]) -> int:
    halfLen = len(array) // 2
    counter = Counter(array)
    for val, count in counter.items():
        if count >= halfLen:
            return val
        

testCases = [
    {
        "input": [1, 2, 1, 1, 3, 4, 0],
        "expect": 1,
    },
    {
        "input": [1, 2, 1, 1, 3, 3, 3, 3, 3, 3, 4, 0],
        "expect": 3,
    },
]


testResults = []

for testCase in testCases:
    testResults.append(runTest(findMajElement, testCase))

printTestResults(testResults)