import time
import random

# Interpolation Search
def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and key >= arr[low] and key <= arr[high]:

        comparisons += 1

        if arr[high] == arr[low]:
            if arr[low] == key:
                return low, comparisons
            return -1, comparisons

        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == key:
            return pos, comparisons

        elif arr[pos] < key:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


# Binary Search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid, comparisons

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


# Performance Analysis
def performance_analysis():

    print(f"{'Size':>10}{'IS Time(ms)':>15}{'BS Time(ms)':>15}{'IS Comparisons':>20}{'BS Comparisons':>20}")
    print("-" * 80)

    for size in [100, 1000, 5000, 10000, 50000]:

        arr = list(range(size))
        key = random.choice(arr)

        # Interpolation Search
        start = time.perf_counter()
        _, is_comp = interpolation_search(arr, key)
        is_time = (time.perf_counter() - start) * 1000

        # Binary Search
        start = time.perf_counter()
        _, bs_comp = binary_search(arr, key)
        bs_time = (time.perf_counter() - start) * 1000

        print(f"{size:>10}{is_time:>15.6f}{bs_time:>15.6f}{is_comp:>20}{bs_comp:>20}")


# Driver Code
arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
key = 35

index, comparisons = interpolation_search(arr, key)

print("Array:", arr)
print("Searching for:", key)

if index != -1:
    print(f"Found at index: {index}, Comparisons: {comparisons}")
else:
    print("Element not found")

print()
performance_analysis()