
def fractional_knapsack(profits, weights, capacity):
    n = len(profits)
    items = []

    # Step 1: Create list of (value, weight, ratio)
    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append((profits[i], weights[i], ratio))

    # Step 2: Sort items by ratio (descending)
    def get_ratio(arr):
        return arr[2]
    items.sort(key=get_ratio, reverse=True)

    total_value = 0.0  # total value accumulated
    remaining_capacity = capacity

    # Step 3: Pick items
    for value, weight, ratio in items:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of the item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0  # now knapsack is full

    return total_value


# Example usage
profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = fractional_knapsack(profits, weights, capacity)
print(f"Maximum value in Knapsack = {max_value:.2f}")
