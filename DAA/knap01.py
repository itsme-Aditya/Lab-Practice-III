def knapsack_01(profits, weights, capacity):
    n = len(profits)
    
    # Create a (n+1) x (capacity+1) DP table initialized to 0
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):          # items
        for w in range(1, capacity + 1):   # weights
            if weights[i-1] <= w:
                # Item can be included
                dp[i][w] = max(
                    profits[i-1] + dp[i-1][w - weights[i-1]],  # take item
                    dp[i-1][w]                                # skip item
                )
            else:
                # Item too heavy to include
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]  # max value at full capacity


# Example usage
profits = [1, 2, 5, 6    ]
weights = [2, 3, 4, 5]
capacity = 8

max_value = knapsack_01(profits, weights, capacity)
print(f"Maximum value in 0/1 Knapsack = {max_value}")
