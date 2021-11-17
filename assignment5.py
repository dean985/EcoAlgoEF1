#!/usr/bin/env python3
from typing import List
import random


class Agent:
    def value(self, item: int) -> float:
        return round(random.uniform(1, 100), 2)


def is_EF1(agents: List[Agent], bundles: List[int]) -> bool:
    # Def for EF1 :
    # For each two agents A, B
    # if we remove from the bundle of agent B
    # the item with most value for A, then A doesn't envy B

    # Local functions
    def sum_items(agent: Agent, items: List[int]) -> float:
        # Function to sum the item values of an agent
        sum = 0
        for it in items:
            sum = sum + agent.value(it)
        return sum

    def max_value(agent: Agent, items: List[int]) -> float:
        # Finds the value of the most valuable item
        max = 0
        for it in items:
            if agent.value(it) > max:
                max = agent.value(it)
        return max

    # Checking if EF1
    for A in agents:
        sum_A = sum_items(agents[A], bundles[A])
        for B in agents:
            if A != B:
                sum_B = sum_items(agents[A], bundles[B])
                max_value_item = max_value(agents[A], bundles[B])
                if sum_A < sum_B - max_value_item:
                    print("Not EF1")
                    return False
    print("EF1!")
    return True
