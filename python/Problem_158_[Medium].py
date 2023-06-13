from typing import List
from test_tools import printTestIteration, printTestResults
"""
This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner,
how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents
a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
"""

def traverseMatrix(matrix: List[List[int]]) -> int:
    finalIdx = [len(matrix)-1, len(matrix[0])-1]
    return move(matrix, [0, 0], finalIdx, 0)


def move(
    matrix: List[List[int]],
    curIdx: List[int],
    finalIdx: List[int],
    count: int,
) -> int:
    print(curIdx)
    print(count)
    # if curIdx == finalIdx or curIdx[0] >= finalIdx[0] or curIdx[1] >= finalIdx[1]:
    if curIdx == finalIdx:
        # return count
        return 1
    # elif matrix[curIdx[0]][curIdx[1]]:
    if curIdx[0] >= finalIdx[0] or curIdx[1] >= finalIdx[1] or matrix[curIdx[0]][curIdx[1]]:
        return 0
    # else:
    #     count += 1
    
    if curIdx[0] < finalIdx[0]:
        count += move(matrix, [curIdx[0] + 1, curIdx[1]], finalIdx, count)
    
    if curIdx[1] < finalIdx[1]:
        count += move(matrix, [curIdx[0], curIdx[1] + 1], finalIdx, count)

    return count


testCases = [
    {
        "input": [
            [0, 0, 1],
            [0, 0, 1],
            [1, 0, 0],
        ],
        "expect": 2,
    },
]


testResults = []

for testCase in testCases:
    inputVal = testCase["input"]
    expect = testCase["expect"]
    result = traverseMatrix(inputVal)
    printTestIteration(inputVal, result, expect)
    testResults.append(result == expect)
printTestResults(testResults)