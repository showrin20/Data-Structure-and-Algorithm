# Bubble Sort

Bubble Sort is a simple, comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process continues until the list is sorted.

## Normal Bubble Sort
The basic version iterates through the list and performs swaps until all elements are in the correct order.

### Code:
```python
def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(lst)

# Example usage
lst = [22, 14, 12, 18, 9]
bubble_sort(lst)  # Output: [9, 12, 14, 18, 22]
```

## Optimized Bubble Sort
The optimized version includes a `swapped` flag that stops the algorithm early if no swaps are made during a pass, indicating that the list is already sorted.

### Code:
```python
def bubble_sort(lst):
    for i in range(len(lst) - 1):
        swapped = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    print(lst)

# Example usage
lst = [9, 12, 14, 18, 22]
bubble_sort(lst)  # Output: [9, 12, 14, 18, 22]
```

## Key Points
- **Time Complexity**:
  - Worst and average case: O(n²)
  - Best case with optimization: O(n)
- **Space Complexity**: O(1) (in-place sorting)
- **Stability**: Bubble Sort is a stable sorting algorithm.
- **Optimization**: The `swapped` flag helps reduce unnecessary passes when the list is already sorted.```
