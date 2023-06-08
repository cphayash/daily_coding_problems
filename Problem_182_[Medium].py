from test_tools import printTestIteration, printTestResults, runTest
from typing import Any, Dict, List, Optional, Union
"""
This problem was asked by Facebook.

A graph is minimally-connected if it is connected and there is no edge that can
be removed while still leaving the graph connected. For example, any binary tree
is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. You can
choose to represent the graph as either an adjacency matrix or adjacency list.
"""

class Node(object):
    def __init__(
        self,
        value: int,
        connections: List[Union[int, "Node"]] = [],
    ) -> "Node":
        self.value = value
        self.connections = []
        [self.addConnection(node) for node in connections]

    def addConnection(self, node: List[Union[int, "Node"]]) -> None:
        if isinstance(node, int):
            node = Node(node)
        self.connections.append(node)
        # node.connections.append(self)

    # def findExistingConnection(self, value: int) -> Optional["Node"]:
    #     for node in self.connections:
    #         if node.value == value:
    #             return node



def checkIfMinimallyConnected(root: Node) -> bool:
    seen = set()

    stack = [root]
    cur = None
    while stack and cur not in seen:
        # print(seen)
        cur = stack.pop()
        # print(cur.connections)
        seen.add(cur)
        stack += cur.connections
        # print(stack)

    return not bool(stack)


def buildGraph(nodeData: List[Dict[Any, Any]]) -> Node: # Returns root
    nodes = {}
    root = None

    # Populate nodes dict
    for nodeDict in nodeData:
        node = nodeDict["node"]
        value = node.value
        nodes[value] = node
        if nodeDict["root"]:
            root = node

    # Add connections
    for nodeDict in nodeData:
        node = Node(nodeDict["node"])
        for connection in nodeDict["connections"]:
            # print(connection, nodes[connection])
            node.addConnection(nodes[connection])
        # print(node.connections)

    return root


testCases = [
    {
        "input": [
            {
                "node": Node(1),
                "connections": [2, 3],
                "root": True,
            },
            {
                "node": Node(2),
                "connections": [],
                "root": False,
            },
            {
                "node": Node(3),
                "connections": [4],
                "root": False,
            },
            {
                "node": Node(4),
                "connections": [],
                "root": False,
            },
        ],
        "expect": True,
    },
    {
        "input": [
            {
                "node": Node(1),
                "connections": [2, 3],
                "root": True,
            },
            {
                "node": Node(2),
                "connections": [],
                "root": False,
            },
            {
                "node": Node(3),
                "connections": [4],
                "root": False,
            },
            {
                "node": Node(4),
                "connections": [1],
                "root": False,
            },
        ],
        "expect": False,
    },
]


testResults = []

for testCase in testCases:
    inputVals = testCase["input"]
    expect = testCase["expect"]
    root = buildGraph(inputVals)
    print(f"root connections: {root.connections}")
    result = checkIfMinimallyConnected(root)
    printTestIteration(inputVals, result, expect)
    testResults.append(result == expect)

printTestResults(testResults)