from string import ascii_uppercase
import sys
from test_tools import runAllTests
from typing import List

"""
This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns:
"A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1,
return "A". Given 27, return "AA".
"""

def getAlphaColumnID(val: int) -> str:
    newVals = []
    convertToBase26(val, newVals)
    return "".join(newVals[::-1])


def convertToBase26(val: int, array: List[str] = []) -> None:
    array.append(ascii_uppercase[(val % 26) - 1])
    div = val // 26
    if div == 0:
        return
    convertToBase26(div, array)


def convertFromBase26(val: str, power: int = 0) -> int:
    val = list(val)
    newVal = (ascii_uppercase.find(val.pop()) + 1) * (26**power)
    if val:
        newVal += convertFromBase26("".join(val), power+1)
    return newVal


def main():
    testCases = [
        {
            "input": 11157,
            "expect": "PMC",
        },
        {
            "input": 1157,
            "expect": "ARM",
        },
    ]

    runAllTests(getAlphaColumnID, testCases)
    

if __name__ == '__main__':
    main()