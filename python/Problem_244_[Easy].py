from test_tools import runAllTests
from typing import List

"""
This problem was asked by Square.

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers
smaller than N. The method is to take increasingly larger prime numbers, and
mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...]
(multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we
have done this for all primes less than N, the unmarked numbers that remain will
be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without
taking N as an input).
"""

# Time: O(N^2)
# Space: O(N)
def sieveOfEratosthens(N: int) -> List[int]:
    primes = set()

    for potentialPrime in range(2, N): # O(N)
        isPrime = True
        for num in range(2, potentialPrime//2+1): # O(N/2) => O(N)
            isPrime = isPrime and not potentialPrime % num
            if not isPrime:
                break
        if isPrime:
            primes.add(potentialPrime)

    # It's faster to create a list comprehension than to sort
    # Creating the new list also uses O(N) space, which does not increase
    # space complexity
    return [val for val in range(2, N) if val in primes] # O(N)
        

def main():
    testCases = [
        {
            "input": 50,
            "expect": [
                2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
            ],
        },
        {
            "input": 100,
            "expect": [
                2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
            ],
        },
    ]

    runAllTests(sieveOfEratosthens, testCases)

if __name__ == '__main__':
    main()