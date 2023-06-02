"""
This problem was asked by Airbnb.

Given a linked list and a positive integer k, rotate the list to the right
by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2,
it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3,
it should become 3 -> 4 -> 5 -> 1 -> 2.
"""

class Node(object):
    def __init__(self, value: int, nextNode=None) -> None:
        self.value = value
        self.next = nextNode

    def __str__(self) -> str:
        return str(self.value)
    
    def getLinkedListValues(self) -> str:
        values = []
        cur = self
        while cur:
            values.append(str(cur))
            cur = cur.next
        return " -> ".join(values)


def rotateLinkedList(head: Node) -> Node:
    tail = None
    cur = head
    prev = None
    while cur.next:
        prev = cur
        cur = cur.next
    prev.next = None
    cur.next = head
    return cur

# Time: O(nk) | n is length of linked list, k is number of rotations
# Space: O(n) | n is length of linked list
def rotateLinkedListByK(head: Node, k: int) -> Node:
    for _ in range(k):
        head = rotateLinkedList(head)

    return head


testCases = [
    {
        "input": {
            "values": [7, 7, 3, 5],
            "k": 2,
        },
        "expect": "3 -> 5 -> 7 -> 7",
    },
    {
        "input": {
            "values": [1, 2, 3, 4, 5],
            "k": 3,
        },
        "expect": "3 -> 4 -> 5 -> 1 -> 2",
    },
]


testResults = []

for testCase in testCases:
    values = testCase["input"]["values"]
    k = testCase["input"]["k"]
    nextNode = None
    for value in values[::-1]:
        head = Node(value, nextNode)
        nextNode = head
    res = rotateLinkedListByK(head, k)
    expect = testCase["expect"]
    match = res.getLinkedListValues() == expect
    print(res.getLinkedListValues())
    print(expect)
    print(match)
    testResults.append(match)

print(testResults)