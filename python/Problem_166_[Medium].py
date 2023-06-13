"""
This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays,
and should implement the following methods:
    next(): returns the next element in the array of arrays. If there are no more
        elements, raise an exception.
    has_next(): returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next()
repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""

# Time: O(n) | n is the number of elements in arrays
# Space: O(n) | n is the number of elements in arrays
class TwoDIterator(object):
    def __init__(self, arrays) -> None:
        self.arrays = arrays
        self.outerArrayIdx = 0
        self.innerArrayIdx = -1

    def has_next(self) -> bool:
        if self.outerArrayIdx >= len(self.arrays):
            return False
        if self.innerArrayIdx >= len(self.arrays[self.outerArrayIdx]) - 1:
            self.outerArrayIdx += 1
            self.innerArrayIdx = -1
            return self.has_next()
        return True
    
    def next(self) -> int:
        if self.has_next():
            self.innerArrayIdx += 1
        else:
            raise Exception("No more values!")
        return self.arrays[self.outerArrayIdx][self.innerArrayIdx]
    

arrays = [[1, 2], [3], [], [], [4, 5, 6]]
twoDIterator = TwoDIterator(arrays)

for _ in range(7):
    nextVal = twoDIterator.next()
    print(nextVal)