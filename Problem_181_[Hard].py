from typing import List
from test_tools import printAllMatch, printExpect, printResult, printTestResults
"""
This problem was asked by Google.

Given a string, split it into as few strings as possible such that each string
is a palindrome.

For example, given the input string racecarannakayak,
return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].
"""

def isPalindrome(string: str) -> bool:
    return string == string[::-1] and len(string) > 0


# Time: O(n^3) | n is len(string)
# Space: O(n) | n is len(string)
def splitString(string: str) -> List[str]:
    substrings = []

    startIdx = 0
    while startIdx < len(string):
        for endIdx in range(len(string), startIdx, -1):
            substring = string[startIdx:endIdx]
            if isPalindrome(substring):
                substrings.append(substring)
                startIdx = endIdx - 1
        startIdx += 1

    return substrings


testCases = [
    {
        "input": "racecarannakayak",
        "expect": ["racecar", "anna", "kayak"],
    },
    {
        "input": "abc",
        "expect": ["a", "b", "c"],
    },
    {
        "input": "abbc",
        "expect": ["a", "bb", "c"],
    },
]


testResults = []
for testCase in testCases:
    inputString = testCase["input"]
    res = splitString(inputString)
    expect = testCase["expect"]
    match = res == expect
    testResults.append(match)
    printResult(res)
    printExpect(expect)
    print(match)
    
printAllMatch(testResults)