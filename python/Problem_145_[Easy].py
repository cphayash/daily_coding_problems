from typing import Dict, List, Optional
from test_tools import printExpect, printIsMatch, printResult, printTestResults


"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""


class Node(object):
    def __init__(self, value: int, next: Optional["Node"] = None):
        self.value = value
        self.next = next

    def __str__(self):
        vals = []
        cur = self
        while cur:
            vals.append(str(cur.value))
            cur = cur.next
        return " -> ".join(vals)


# Time: O(n) | n is number of nodes in the linked list
# Space: O(n) | n is number of nodes in the linked list
def swapEveryTwo(head: Optional[Node]) -> Node:
    if not head:
        return None
    returnHead = head.next

    n1 = head
    n2 = n1.next
    n3 = n2.next
    n2.next = n1
    n1.next = swapEveryTwo(n3)

    return returnHead


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
    inputVal = testCase["input"]
    expect = testCase["expect"]
    next = None
    for d in inputVal[::-1]:
        node = Node(d["value"], next)
        next = node
    
    result = swapEveryTwo(next)
    printResult(str(result))
    printExpect(expect)
    printIsMatch(result, expect)
    testResults.append(str(result) == expect)
printTestResults(testResults)