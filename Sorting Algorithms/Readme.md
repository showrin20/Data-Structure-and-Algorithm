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


# Selection Sort Algorithm

## Overview
Selection Sort is a simple comparison-based sorting algorithm. It repeatedly selects the smallest element from the unsorted portion of the list and places it at the beginning, ensuring that the sorted portion grows one element at a time. It's intuitive but generally inefficient for large datasets compared to more advanced sorting algorithms.

## Key Points
- **Algorithm Type**: Comparison Sort
- **Time Complexity**: 
  - Best, Average, and Worst Case: O(n²)
- **Space Complexity**: O(1) (in-place)
- **Stability**: Not stable
- **Use Case**: Best suited for small datasets or when memory usage is a constraint.

## How It Works
1. Divide the array into a sorted and an unsorted portion.
2. Repeatedly find the smallest element in the unsorted portion and swap it with the first unsorted element.
3. The sorted portion grows from left to right, element by element, until the entire list is sorted.

## Implementation
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

# Example
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

