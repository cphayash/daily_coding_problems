from typing import Optional
from test_tools import (
    printTestIteration,
    printTestResults,
)


"""
This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is
no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef",
return null.
"""

def findFirstRecurrance(string: str) -> Optional[str]:
    seen = set()
    for char in string:
        if char in seen:
            return char
        seen.add(char)

    return None


testCases = [
    {
        "input": "acbbac",
        "expect": "b",
    },
    {
        "input": "abcdef",
        "expect": None,
    },
]


testResults = []

for testCase in testCases:
    inputVal = testCase["input"]
    expect = testCase["expect"]
    res = findFirstRecurrance(inputVal)
    printTestIteration(inputVal, res, expect)
    testResults.append(res == expect)

printTestResults(testResults)