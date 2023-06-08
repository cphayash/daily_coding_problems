from collections import Counter
from test_tools import (
    printTestIteration,
    printTestResults,
)

"""
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form
racecar, which is a palindrome. daily should return false, since there's no
rearrangement that can form a palindrome.
"""


def couldBePalindrome(string: str) -> bool:
    counter = Counter(string)
    oneCount = sum([item if item == 1 else 0 for item in counter.values()])
    return oneCount <= 1


testCases = [
    {
        "input": "carrace",
        "expect": True,
    },
    {
        "input": "daily",
        "expect": False,
    },
]

testResults = []

for testCase in testCases:
    inputVal = testCase["input"]
    expect = testCase["expect"]
    res = couldBePalindrome(inputVal)
    printTestIteration(inputVal, res, expect)
    testResults.append(res == expect)

printTestResults(testResults)