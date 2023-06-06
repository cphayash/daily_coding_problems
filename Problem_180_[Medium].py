from typing import List
from test_tools import printAllMatch, printExpect, printResult, printTestResults

"""
This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the
second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue
from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3].
If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
"""


def interleaveArray(array: List[int]) -> List[int]:
    halfLen = int(len(array) / 2)
    stack = array[:halfLen][::-1]
    queue = array[halfLen:]

    # print(stack)
    # print(queue)
    newArr = []
    while stack or queue:
        stackVal = stack.pop() if stack else None
        queueVal = queue.pop()
        if stackVal is not None:
            newArr.append(stackVal)
        newArr.append(queueVal)

    return newArr


testCases = [
    {
        "input": [1, 2, 3, 4, 5],
        "expect": [1, 5, 2, 4, 3],
    },
    {
        "input": [1, 2, 3, 4],
        "expect": [1, 4, 2, 3],
    },
]

testResults = []

for testCase in testCases:
    res = interleaveArray(testCase["input"])
    expect = testCase["expect"]
    match = res == expect
    printResult(res)
    printExpect(expect)
    print(match)
    testResults.append(match)
printAllMatch(testResults)