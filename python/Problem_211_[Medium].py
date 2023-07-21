from test_tools import printTestIteration, printTestResults
from typing import List


"""
This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of
the pattern in the string. For example, given the string "abracadabra" and the
pattern "abr", you should return [0, 7].
"""


def findStartPositions(string: str, pattern: str) -> List[int]:
    results = []
    for i in range(len(string)-len(pattern)):
        if string[i:i+len(pattern)] == pattern:
            results.append(i)

    return results


def main():
    testCases = [
        {
            "input": {
                "string": "abracadabra",
                "pattern": "abr",
            },
            "expect": [0, 7],
        },
        {
            "input": {
                "string": "loveydovey",
                "pattern": "ve",
            },
            "expect": [2, 7],
        },
    ]

    testResults = []

    for testCase in testCases:
        inputVal = testCase["input"]
        expect = testCase["expect"]
        string = inputVal["string"]
        pattern = inputVal["pattern"]
        result = findStartPositions(string, pattern)
        testResults.append(result == expect)
        printTestIteration(inputVal, result, expect)
    printTestResults(testResults)


if __name__ == "__main__":
    main()