# from test_tools import printTestResults, runTest
from test_tools import runAllTests
from typing import List
"""
This problem was asked by Uber.

Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand. Find the minimum element in O(log N) time. You may assume the
array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""

# Time: O(log n) | n is len(array)
# Space: O(1)
def findMinElement(array: List[int]) -> int:
    startIdx = 0
    endIdx = len(array) - 1

    while endIdx > startIdx:
        halfIdx = (endIdx + startIdx) // 2
        valFirst = array[startIdx]
        valMid = array[halfIdx]
        valEnd = array[endIdx]
        
        # Lowest value in the first half
        if valFirst > valMid and valMid < valEnd:
            endIdx = halfIdx
        # Lowest value in second half
        if valMid > valFirst and valMid > valEnd:
            startIdx = halfIdx
        else: # In this case, we have only 2 elements
            return array[startIdx] if array[startIdx] < array[endIdx] else array[endIdx]


testCases = [
    {
        "input": [5, 7, 10, 3, 4],
        "expect": 3,
    },
]

runAllTests(findMinElement, testCases)