from test_tools import printTestIteration, printTestResults
from typing import List
"""
This problem was asked by Google.

You are given an array of nonnegative integers. Let's say you start at the
beginning of the array and are trying to advance to the end. You can advance at
most, the number of steps that you're currently on. Determine whether you can
get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices
0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""

# Time: O(n) | n is len(array)
# Space: O(1)
def endIsReachable(array: List[int]) -> bool:
    maxReach = array[0]
    idx = 0

    while idx < len(array) and idx <= maxReach:
        maxReach = max(maxReach, idx + array[idx])
        idx += 1

    return maxReach >= len(array) - 1



testCases = [
    {
        "input": [1, 3, 1, 2, 0, 1],
        "expect": True,
    },
    {
        "input": [1, 2, 1, 0, 0],
        "expect": False,
    },
]

testResults = []

for testCase in testCases:
    inputVal = testCase["input"]
    expect = testCase["expect"]
    result = endIsReachable(inputVal)
    testResults.append(result == expect)
    printTestIteration(inputVal, result, expect)
printTestResults(testResults)