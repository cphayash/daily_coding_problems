from time import sleep
"""
This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99
should become -3 -> 1 -> 4 -> 99.
"""

class Node(object):
    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next

    def toString(self) -> str:
        cur = self
        values = []
        while cur:
            values.append(str(cur.value))
            cur = cur.next
        return " -> ".join(values)

    def printLL(self) -> None:
        print(self.toString())


def sortLinkedList(head: Node) -> Node:
    cur = head
    prev = None
    while cur.next:
        if cur.next.value < cur.value:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = tmp
            if prev:
                prev.next = cur
            if cur.next == head:
                head = cur
            cur = prev if prev else head
            prev = None
            # cur = head
        else:
            prev = cur
            cur = cur.next
    return head



testCases = [
    {
        "input": [4, 1, -3, 99],
        "expect": "-3 -> 1 -> 4 -> 99",
    }
]

testResults = []

for testCase in testCases:
    reversedForInstantiation = testCase["input"][::-1]
    nextNode = None
    for value in reversedForInstantiation:
        head = Node(value, nextNode)
        nextNode = head
    head.printLL()
    result = sortLinkedList(head)
    print()
    result.printLL()
    expect = testCase["expect"]
    print(expect)
    match = result.toString() == expect
    testResults.append(match)
print(testResults)