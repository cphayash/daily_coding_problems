from typing import Dict, List, Optional
from test_tools import printExpect, printIsMatch, printResult, printTestResults
# , runTest


"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""


class Node(object):
    def __init__(self, value: int, next: Optional["Node"] = None):
        self.value = value
        self.next = next

    # def printLinkedList(self):
    #     vals = []
    #     cur = self
    #     while cur:
    #         print(type(cur))
    #         print(cur.next)
    #         vals.append(str(cur.value))
    #         cur = cur.next
    #     return " -> ".join(vals)

    def __str__(self):
        vals = []
        cur = self
        while cur:
            vals.append(str(cur.value))
            cur = cur.next
        return " -> ".join(vals)
        # return " -> " + str(self.value) + str(self.next) if self.next else ""


def swapEveryTwo(head: Node) -> Node:
    cur = head
    prev = None
    while cur:
        # print(cur.value)
        nextNode = cur.next
        nextNext = cur.next.next
        if prev:
            print("OOH!")
            print(nextNode.value)
            prev.next = nextNode
        cur.next = nextNext
        nextNode.next = cur
        print(nextNode.value, nextNode.next.value)
        if cur == head:
            head = nextNode
        cur = nextNext
        prev = nextNode

    return head


def buildLinkedList(nodeVals: List[Dict[str, int]]) -> Node:
    head = None

    next = None
    for value in nodeVals[::-1]:
        node = Node(value, next)
        if not head:
            head = node
        next = node

    return head
        



testCases = [
    {
        "input": [
            {
                "value": 1,
                "next": 2,
            },
            {
                "value": 2,
                "next": 3,
            },
            {
                "value": 3,
                "next": 4,
            },
            {
                "value": 4,
                "next": None,
            },
        ],
        "expect": "2 -> 1 -> 4 -> 3",
    },
]

testResults = []
for testCase in testCases:
    # testResults.append(runTest(swapEveryTwo, testCase))
    inputVal = testCase["input"]
    expect = testCase["expect"]
    # result = str(swapEveryTwo(inputVal))
    next = None
    for d in inputVal[::-1]:
        node = Node(d["value"], next)
        next = node
    # result = str(swapEveryTwo(next))
    result = swapEveryTwo(next)
    printResult(result)
    printExpect(expect)
    printIsMatch(result, expect)
    testResults.append(result == expect)
    print(result)
printTestResults(testResults)