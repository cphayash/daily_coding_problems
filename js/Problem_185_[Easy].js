const test_tools = require("./test_tools.js");
/*
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
*/

function buildArray(start, length) {
    let arr = [];
    for (let i = start; i < start + length; i++) {
        arr.push(i);
    }

    return arr;
}


function getSizeOfIntersection(rectangles) {
    let masterSetX = new Set();
    let masterSetY = new Set();

    for (const rectangle of rectangles) {
        const topLeft = rectangle.top_left;
        const dimensions = rectangle.dimensions;
        const rangeX = new Set(buildArray(topLeft[0], dimensions[0]));
        const rangeY = new Set(buildArray(topLeft[1], dimensions[1]));
        if (masterSetX.size === 0) {
            rangeX.forEach(val => {masterSetX.add(val)});
        } else {
            masterSetX = new Set([...masterSetX].filter(val => rangeX.has(val)));
        }
        if (masterSetY.size === 0) {
            rangeY.forEach(val => {masterSetY.add(val)});
        } else {
            masterSetY = new Set([...masterSetY].filter(val => rangeY.has(val)));
        }
    }

    return masterSetX.size * masterSetY.size;
}


testCases = [
    {
        "input": [
            {
                "top_left": [1, 4],
                "dimensions": [3, 3], // width, height
            },
            {
                "top_left": [0, 5],
                "dimensions": [4, 3], // width, height
            },
        ],
        "expect": 6,
    }
]


testResults = [];

for (testCase of testCases) {
    testResults.push(test_tools.runTest(getSizeOfIntersection, testCase));
}
test_tools.printTestResults(testResults);