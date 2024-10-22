

# Fractional Knapsack Problem

# Problem Statement: Given a set of items, each with a weight and value, and a knapsack with a 
# maximum weight capacity, maximize the total value in the knapsack when you can take fractions 
# of items.

def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    items.sort(key=lambda x: x[0], reverse=True)  # Sort by value-to-weight ratio
    
    total_value = 0
    for ratio, weight, value in items:
        if capacity == 0:
            break
        take_weight = min(weight, capacity)
        total_value += take_weight * ratio
        capacity -= take_weight
    
    return total_value

# Example usage:
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print(fractional_knapsack(weights, values, capacity))  # Output: 240.0
