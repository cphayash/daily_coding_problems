from typing import List
from test_tools import (
    printAllMatch,
    printExpect,
    printInput,
    printIsMatch,
    printResult,
    printTestResults,
)

"""
This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word.
For example, given the list:

dog
cat
apple
apricot
fish
Return the list:

d
c
app
apr
f
"""


class Trie(object):
    def __init__(self):
        self.children = {}
        self.count = 0

    def printAllChildren(self):
        for child in self.children:
            print(child)
            self.children[child].printAllChildren()


def addWord(root: Trie, word: str) -> None:
    cur = root

    for char in word:
        if char not in cur.children:
            cur.children[char] = Trie()
        cur = cur.children[char]
        cur.count += 1


def findUniquePrefix(root: Trie, word: str) -> str:
    prefix = ""
    cur = root

    for char in word:
        if cur.count == 1:
            return prefix
        cur = cur.children[char]
        prefix += char
    return prefix


def shortestPrefixes(array: List[str]) -> List[str]:
    root = Trie()
    results = []

    for word in array:
        addWord(root, word)

    for word in array:
        res = findUniquePrefix(root, word)
        results.append(res)

    return results


testCases = [
    {
        "input": [
            "dog",
            "cat",
            "apple",
            "apricot",
            "fish",
        ],
        "expect": [
            "d",
            "c",
            "app",
            "apr",
            "f",
        ],
    }
]


testResults = []

for testCase in testCases:
    inputVal = testCase["input"]
    expect = testCase["expect"]
    res = shortestPrefixes(inputVal)
    match = res == expect
    printResult(res)
    printExpect(expect)
    printIsMatch(res, expect)
    testResults.append(match)
printTestResults(testResults)