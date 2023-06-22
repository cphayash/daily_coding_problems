from typing import Any, List
from test_tools import printTestIteration, printTestResults
"""
This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the array,
rotate the array to the right k elements in-place.
"""

"""
The naive approach would be to rotate the array k times, one position each time.
However, it would be smarter to rotate only once, based on k
For

Example: [1,2,3,4], k = 1
Result:  [4,1,2,3]

Example: [1,2,3,4], k = 2
Result:  [3,4,1,2]

0,1,2,3
2,3,0,1

Example: [1,2,3,4,5,6], k = 2
Result:  [5,6,1,2,3,4]
0,1,2,3,4,5
4,5,0,1,2,3

To find new idx, for each i
we add len(array) - k if i < k
else (i == k), subtract k

Starting with [1,2,3,4,5,6]
i = 0 [5,2,3,4,1,6]
i = 1 [5,6,3,4,1,2]
i = 2 [5,6,3,4,1,2] # Now we need to shift the rest of the array left I think


Example: [1,2,3,4,5,6], k = 2
Result:  [5,6,1,2,3,4]

[1,2,3,4,_,6] tmp = 5
[5,2,3,4,_,6] tmp = 1
[5,2,1,4,_,6] tmp = 3
[5,2,1,4,3,6]
[5,2,1,4,3,_] tmp = 6
[5,6,1,4,3,_] tmp = 2
[5,6,1,2,3,_] tmp = 4
[5,6,1,2,3,4]


Example: [1,2,3,4,5,6,7,8], k = 2
Result:  [7,8,1,2,3,4,5,6]

[1,2,3,4,5,6,_,8] tmp = 7
[7,2,3,4,5,6,_,8] tmp = 1
# [7,2,1,4,5,6,_,8] tmp = 3
[7,2,1,4,3,6,_,8] tmp = 5
[7,2,1,4,3,6,5,8]
# [7,2,1,4,5,6,3,8]
[7,2,1,4,5,6,3,_] tmp = 8
[7,8,1,4,5,6,3,_] tmp = 2
[7,8,1,2,5,6,3,_] tmp = 4
[7,8,1,2,5,4,3,_] tmp = 6
[7,8,1,2,5,4,3,6]


Example: [1,2,3,4,5,6,7,8], k = 4
Result:  [5,6,7,8,1,2,3,4]

[1,2,3,4,_,6,7,8] tmp = 5
[5,2,3,4,_,6,7,8] tmp = 1
[5,2,3,4,1,6,7,8]
[5,2,3,4,1,_,7,8] tmp = 6
[5,6,3,4,1,_,7,8] tmp = 2
[5,6,3,4,1,2,7,8]
[5,6,3,4,1,2,_,8] tmp = 7
[5,6,7,4,1,2,_,8] tmp = 3
[5,6,7,4,1,2,3,8]
[5,6,7,4,1,2,3,_] tmp = 8
[5,6,7,8,1,2,3,_] tmp = 4
[5,6,7,8,1,2,3,4]


Example: [1,2,3,4,5,6,7,8], k = 3
Result:  [6,7,8,1,2,3,4,5]

#Starting from len(array) - k position
[1,2,3,4,5,_,7,8] tmp = 6
[6,2,3,4,5,_,7,8] tmp = 1
[6,2,3,1,5,_,7,8] tmp = 4
[6,2,3,1,5,_,4,8] tmp = 7
[6,7,3,1,5,_,4,8] tmp = 2
[6,7,3,1,2,_,4,8] tmp = 5
[6,7,3,1,2,_,4,5] tmp = 8
[6,7,3,8,2,_,4,5] tmp = 1
[6,7,3,8,1,_,4,5] tmp = 2
[6,7,3,8,1,2,4,5]


Example: [1,2,3,4,5,6,7,8], k = 3
Result:  [6,7,8,1,2,3,4,5]

[_,2,3,4,5,6,7,8] tmp = 1
[_,2,3,1,5,6,7,8] tmp = 4
[_,2,3,1,5,6,4,8] tmp = 7
[_,7,3,1,5,6,4,8] tmp = 2
[_,7,3,1,2,6,4,8] tmp = 5
[_,7,3,1,2,6,4,5] tmp = 8
[_,7,8,1,2,6,4,5] tmp = 3
[_,7,8,1,2,3,4,5] tmp = 6
[6,7,8,1,2,3,4,5]
"""

"""
Wow.  I looked up a solution on LeetCode and like I was thinking earlier, it's
way simpler than the approach I was taking. It just reverses the list, then
reverses array[k:] and reverses array[:k]
"""

# def rotateArray(array: List[Any]) -> None:
#     tmp = array[-1]
#     array[-1] = None
#     for i in range(len(array)-1, 0, -1):
#         # array[i], array[i-1] = array
#         array[i] = array[i-1]
#     array[0] = tmp

# O(n)
# def rotateArrayNTimes(array: List[Any], k: int) -> List[Any]:
#     i = 0
#     tmp = array[i]
#     for _ in range(len(array)):
#         i += k
#         if i >= len(array):
#             i -= len(array)
#         # print(i)
#         tmp, array[i] = array[i], tmp
#         print(array)

#     return array

# Time: O(n)
# Space: O(1)
def rotateArrayNTimes(array: List[Any], k: int) -> List[Any]:
    length = len(array)

    array.reverse()

    for i in range(k//2):
        array[i], array[k-1-i] = array[k-1-i], array[i]

    for i in range(k, (length+k)//2):
        array[i], array[length-1-i+k] = array[length-1-i+k], array[i]

    return array



testCases = [
    {
        "input": {
            "array": [1,2,3,4],
            "k": 1,
        },
        "expect": [4,1,2,3],
    },
    {
        "input": {
            "array": [1,2,3,4],
            "k": 2,
        },
        "expect": [3,4,1,2],
    },
    {
        "input": {
            "array": [1,2,3,4,5,6],
            "k": 2,
        },
        "expect": [5,6,1,2,3,4],
    },
    {
        "input": {
            "array": [1,2,3,4,5,6,7,8],
            "k": 2,
        },
        "expect": [7,8,1,2,3,4,5,6],
    },
    {
        "input": {
            "array": [1,2,3,4,5,6,7,8],
            "k": 3,
        },
        "expect": [6,7,8,1,2,3,4,5],
    },
]


testResults = []

for testCase in testCases:
    inputVal = testCase["input"]
    array = inputVal["array"]
    k = inputVal["k"]
    expect = testCase["expect"]
    result = rotateArrayNTimes(array, k)
    printTestIteration(inputVal, result, expect)
    testResults.append(result == expect)
printTestResults(testResults)