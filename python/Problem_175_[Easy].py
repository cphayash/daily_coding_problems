from random import random
from typing import Any, Dict, List, Tuple, Union

"""
This problem was asked by Google.

You are given a starting state start, a list of transition probabilities for a
Markov chain, and a number of steps num_steps. Run the Markov chain starting
from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following
transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce
{ 'a': 3012, 'b': 1656, 'c': 332 }
"""


def getProbabilities(
    start: str,
    transitions: List[Tuple[Union[str, float]]],
    num_steps: int,
) -> Dict[str, Union[int, float]]:
    probOptions = {}
    for t in transitions:
        key, dest, prob = t
        if key in probOptions:
            probOptions[key][dest] = prob
        else:
            probOptions[key] = {dest: prob}
    print(probOptions)

    result = {t[0]: 0 for t in transitions}

    cur = start
    for _ in range(num_steps):
        # probs = {t[1]: t[2] for t in transitions if t[0] == start}
        probs = probOptions[cur]
        rand = random()


getProbabilities(
    "a",
    [
        ('a', 'a', 0.9),
        ('a', 'b', 0.075),
        ('a', 'c', 0.025),
        ('b', 'a', 0.15),
        ('b', 'b', 0.8),
        ('b', 'c', 0.05),
        ('c', 'a', 0.25),
        ('c', 'b', 0.25),
        ('c', 'c', 0.5)
        ],
    5
)