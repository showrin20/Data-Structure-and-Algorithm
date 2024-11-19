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
```
# Insertion Sort Algorithm

## Overview
Insertion Sort is a simple and efficient comparison-based sorting algorithm that builds the sorted array one item at a time by repeatedly inserting each element into its correct position relative to the already sorted part of the array. It is commonly used for small datasets or as part of more complex sorting algorithms.

## Key Points
- **Algorithm Type**: Comparison Sort
- **Time Complexity**:
  - Best Case: O(n) (when the array is already sorted)
  - Average and Worst Case: O(n²)
- **Space Complexity**: O(1) (in-place sorting)
- **Stable Sort**: Yes
- **Use Case**: Best for small datasets, nearly sorted arrays, or when simplicity is required.

## How It Works
1. Start from the first element and consider it "sorted."
2. For each element at position `i` in the array:
   - Store the element in a temporary variable (`temp`).
   - Compare it with elements before it in the sorted section of the array.
   - Shift elements larger than `temp` to the right.
   - Insert `temp` at the correct position once the sorted order is maintained.
3. Repeat this process until the entire array is sorted.

## Implementation
```python
def insertion_sort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    print(arr)

# Example usage
arr = [48, 99, 4, 60, 22]
insertion_sort(arr)  # Output: [4, 22, 48, 60, 99]
```


# Quick Sort Algorithm

## Overview
Quick Sort is an efficient, comparison-based, divide-and-conquer sorting algorithm. It works by selecting a 'pivot' element and partitioning the other elements into two groups - those less than the pivot and those greater. It then recursively sorts the partitions.

## Key Points
- **Algorithm Type**: Divide and Conquer, Comparison Sort
- **Time Complexity**:
  - Best and Average Case: `O(n log n)`
  - Worst Case: `O(n^2)` (occurs when pivot selection leads to unbalanced partitions)
- **Space Complexity**: `O(log n)` (due to recursive calls)
- **Stable Sort**: No
- **Use Case**: Efficient for large datasets, especially when in-place sorting is required.

## How It Works
1. Choose a pivot element from the array.
2. Partition the array around the pivot, placing smaller elements to the left and larger ones to the right.
3. Recursively apply this process to the left and right sub-arrays until the entire array is sorted.

## Code Example

```python
def partition(arr, l, h):
    pivot = l
    while l < h:
        while l < h and arr[l] <= arr[pivot]:
            l += 1
        while l < h and arr[h] >= arr[pivot]:
            h -= 1
        arr[l], arr[h] = arr[h], arr[l]
    arr[h], arr[pivot] = arr[pivot], arr[h]
    return h

def quick_sort(arr, l, h):
    if l < h:
        p_index = partition(arr, l, h)
        quick_sort(arr, l, p_index - 1)
        quick_sort(arr, p_index + 1, h)
    return arr

arr = [10, 7, 8, 9, 1, 5]
print("Unsorted Array:", arr)
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", sorted_arr)
```

## Example Output
```
Unsorted Array: [10, 7, 8, 9, 1, 5]
Sorted Array: [1, 5, 7, 8, 9, 10]
```





