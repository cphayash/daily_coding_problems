from test_tools import runAllTests
from typing import List

"""
This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form
the largest possible integer. For example, given [10, 7, 76, 415], you should
return 77641510.
"""

class IdealizedInt(object):
    def __init__(self, value: int):
        self.value = str(value)

    def __lt__(self, other: "IdealizedInt") -> bool:
        if self.value == other.value:
            return False
        for char1, char2 in zip(self.value, other.value):
            if char1 > char2:
                return False
            elif char1 < char2:
                return True
            
        return len(self.value) > len(other.value)


def createLargestInt(array: List[int]) -> int:
    array = list(map(IdealizedInt, array))
    array.sort(reverse=True)
    return int("".join([item.value for item in array]))
    # return int("".join(map(lambda x: x.value, array)))


def main():
    testCases = [
        {
            "input": [10, 7, 76, 415],
            "expect": 77641510,
        },
        {
            "input": [10, 7, 76, 415, 86],
            "expect": 8677641510,
        },
        {
            "input": [10, 13, 76, 2, 86],
            "expect": 867621310,
        },
    ]

    runAllTests(createLargestInt, testCases)


if __name__ == "__main__":
    main()