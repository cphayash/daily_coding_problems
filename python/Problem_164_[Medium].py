from typing import List
"""
This problem was asked by Google.

You are given an array of length n + 1 whose elements belong to the
set {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate.
Find it in linear time and space.
"""

# Time: O(n) | n is len(array)
# Space: O(n) | n is len(array)
def findDuplicate(array: List[int]) -> int:
    seen = set()
    for value in array:
        if value in seen:
            return value
        seen.add(value)


testCases = [
    {
        "input": [1, 2, 3, 3, 4, 5],
        "expect": 3,
    },
    {
        "input": [1, 2, 7, 3, 4, 5, 1],
        "expect": 1,
    },
]


testResults = []

for testCase in testCases:
    array = testCase["input"]
    expect = testCase["expect"]
    res = findDuplicate(array)
    match = res == expect
    print(res)
    print(expect)
    print(match)
    testResults.append(match)

print(testResults)