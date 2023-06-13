from typing import Dict, List, Tuple
from test_tools import *
"""
This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection.
If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
"""

# Time: O(nm) | n is max width, m is max height
# Space: O(n+m) | n is max width, m is max height
def getSizeOfIntersection(rectangles:List[Dict[str, Tuple[int]]]) -> int:
    masterSetX = set()
    masterSetY = set()

    for rectangle in rectangles:
        topLeft = rectangle["top_left"]
        dimensions = rectangle["dimensions"]
        xRange = set(range(topLeft[0], dimensions[0] + topLeft[0]))
        yRange = set(range(topLeft[1], dimensions[1] + topLeft[1]))
        if not masterSetX:
            masterSetX = xRange
        else:
            masterSetX = masterSetX.intersection(xRange)
        if not masterSetY:
            masterSetY = yRange
        else:
            masterSetY = masterSetY.intersection(yRange)

    return len(masterSetX) * len(masterSetY)


testCases = [
    {
        "input": [
            {
                "top_left": (1, 4),
                "dimensions": (3, 3) # width, height
            },
            {
                "top_left": (0, 5),
                "dimensions": (4, 3) # width, height
            },
        ],
        "expect": 6,
    }
]


testResults = []

for testCase in testCases:
    testResults.append(runTest(getSizeOfIntersection, testCase))
printTestResults(testResults)