from typing import Any, Dict
import sys
"""
This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""

# Time: O(n) | n is number of elements in inputVal
# Space: O(n) | n is number of elements in inputVal
def flattenDict(inputVal, namespace=[]):
    newDict = {}
    tmpDicts = []
    for k in inputVal:
        newNamespace = namespace + [k]
        newKey = ".".join(newNamespace)
        val = inputVal[k]
        if isinstance(val, dict):
            tmpDicts.append(flattenDict(val, newNamespace))
        else:
            newDict[newKey] = val
    for tmpDict in tmpDicts:
        newDict.update(tmpDict)

    return newDict


testCases = [
    {
        "input": {
            "key": 3,
            "foo": {
                "a": 5,
                "bar": {
                    "baz": 8
                }
            }
        },
        "expect": {
            "key": 3,
            "foo.a": 5,
            "foo.bar.baz": 8
        }
    }
]


testResults = []
for testCase in testCases:
    output = flattenDict(testCase["input"])
    expect = testCase["expect"]
    result = output == expect
    print(output)
    print(expect)
    print(result)
    testResults.append(result)

print(testResults)