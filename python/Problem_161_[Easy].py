from test_tools import (
    printAllMatch,
    printExpect,
    printInput,
    printIsMatch,
    printResult,
    printTestResults,
)


"""
This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
return 0000 1111 0000 1111 0000 1111 0000 1111.
"""

def reverseBinary(num: str) -> str:
    return num[::-1]


testCases = [
    {
        "input": "1111 0000 1111 0000 1111 0000 1111 0000",
        "expect": "0000 1111 0000 1111 0000 1111 0000 1111",
        # "expect": 252645135, # base10 representation of above "expect" value
    },
]

testResults = []

for testCase in testCases:
    res = reverseBinary(testCase["input"])
    expect = testCase["expect"]
    printInput(testCase["input"])
    printResult(res)
    printExpect(expect)
    printIsMatch(res, expect)
    testResults.append(res == expect)

printTestResults(testResults)