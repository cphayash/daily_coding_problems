from typing import List

"""
This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Follow-up: What if you couldn't use any extra space?
"""

# Time: O(n) | n is num elements in matrix
# Space: O(n) | n is num elements in matrix

# def rotate90Deg(matrix: List[List[int]]) -> List[List[int]]:
#     newMatrix = []
#     for i in range(len(matrix)):
#         newMatrix.append([matrix[r][i] for r in range(len(matrix) - 1, -1, -1)])

#     return newMatrix
def rotate90Deg(matrix: List[List[int]]) -> List[List[int]]:
    return [
        [matrix[r][i] for r in range(len(matrix) - 1, -1, -1)]
        for i in range(len(matrix))
    ]


def printMatrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)
    print()

testCases = [
    {
        "input": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        "expect": [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ],
    }
]

testResults = []

for testCase in testCases:
    res = rotate90Deg(testCase["input"])
    expect = testCase["expect"]
    printMatrix(res)
    printMatrix(expect)
    testResults.append(res == expect)

print(testResults)