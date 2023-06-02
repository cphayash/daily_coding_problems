from typing import List
"""
This problem was asked by Google.

Given an array of integers, return a new array where each element in the new
array is the number of smaller elements to the right of that element in the
original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""

# Time: O(n^2) | n is len(array)
# Space: O(n) | n is len(array)
def getSmallerElementsToRight(array: List[int]) -> List[int]:
    smallerValueCount = []

    for i in range(len(array)):
        base = array[i]
        count = 0
        for j in range(i + 1, len(array)):
            if array[j] < base:
                count += 1
        smallerValueCount.append(count)

    return smallerValueCount


testCases = [
    {
        "input": [3, 4, 9, 6, 1],
        "expect": [1, 1, 2, 1, 0],
    },
]

testResults = []
for testCase in testCases:
    array = testCase["input"]
    expect = testCase["expect"]
    res = getSmallerElementsToRight(array)
    match = res == expect
    print(res)
    print(expect)
    print(match)
    testResults.append(match)

print(testResults)