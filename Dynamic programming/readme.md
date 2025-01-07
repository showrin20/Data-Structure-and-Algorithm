# 0/1 Knapsack Problem Solver

## Problem Statement

Given:
- A list of items, each with a specific value and weight.
- A knapsack with a maximum weight capacity.

Find the maximum value that can be achieved by selecting items without exceeding the knapsack's capacity, where each item can either be included in the knapsack or excluded.

## Algorithm

The solution uses **dynamic programming** to efficiently compute the maximum value:
- A 2D DP table (`dp[i][w]`) is used, where:
  - `i` represents the first `i` items considered.
  - `w` represents the weight capacity of the knapsack.
- The table is updated based on whether including the current item yields a higher value than excluding it.


### Code

```python
def knapsack(values, weights, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.
    
    :param values: List of item values
    :param weights: List of item weights
    :param capacity: Maximum capacity of the knapsack
    :return: Maximum value that can be obtained
    """
    n = len(values)
    # Create a 2D DP table to store the maximum value for each capacity and items
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:  # Can include the item
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:  # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = knapsack(values, weights, capacity)
print(f"The maximum value that can be obtained is: {max_value}")
