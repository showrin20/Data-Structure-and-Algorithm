![sort](sort.jpg)

![sort](sort1.png)

# Bubble Sort

Bubble Sort is a simple, comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process continues until the list is sorted.

## Normal Bubble Sort
The basic version iterates through the list and performs swaps until all elements are in the correct order.

### Code:
```python
def bubble_sort(lst):
    n = len(lst)  # Length of the list
    for i in range(n - 1):  # Loop through the list n-1 times
        for j in range(0, n - i - 1):  # Compare adjacent elements
            if lst[j] > lst[j + 1]:  # If the current element is greater, swap them
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(lst)  # Print the sorted list

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
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i < high and arr[i] <= pivot:
            i += 1
        while j > low and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)
        quick_sort(arr, low, pIndex - 1)
        quick_sort(arr, pIndex + 1, high)
    return arr

arr = [9, 4, 3, 15, 20, 2, 24, 30, 11, 35]
print("Unsorted Array:", arr)
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", sorted_arr)
```

## Example Output
```
Unsorted Array: [10, 7, 8, 9, 1, 5]
Sorted Array: [1, 5, 7, 8, 9, 10]
```
# Merge Sort Algorithm

## Overview
Merge Sort is a popular comparison-based sorting algorithm that employs the **divide and conquer** strategy. The array is repeatedly split into halves, and the halves are recursively sorted and then merged back together. This ensures that the entire array is sorted efficiently.

## Key Points
- **Algorithm Type**: Divide and Conquer, Comparison Sort
- **Time Complexity**:
  - Best, Average, and Worst Case: `O(n log n)` (The divide and merge process has a logarithmic depth)
- **Space Complexity**: `O(n)` (due to auxiliary storage for merging)
- **Stable Sort**: Yes
- **Use Case**: Suitable for large datasets where stability is important, but not ideal for in-place sorting.

## How It Works
1. The array is recursively divided into two halves until single-element arrays are obtained.
2. The single-element arrays are merged in sorted order, creating larger sorted arrays until the entire array is merged back.
3. During merging, the values are compared and appended to a result array to maintain order.

## Code Example

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Calculate the middle index
    mid = len(arr) // 2

    # Split the array into left and right halves
    left = arr[:mid]
    right = arr[mid:]

    # Recursively split and sort each half
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Merge the sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left or right halves
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted Array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)
```

## Example Output
```
Unsorted Array: [38, 27, 43, 3, 9, 82, 10]
Sorted Array: [3, 9, 10, 27, 38, 43, 82]
```

![Merge Sort](Merge-Sort.png)

# Counting Sort Algorithm

The **Counting Sort** algorithm sorts elements by counting their occurrences and placing them in the correct position based on cumulative counts. It is a non-comparison-based sorting algorithm suitable for sorting integers with a known range.

#### Implementation

```python
def count_sort(arr):
    n_max = max(arr)
    count = [0] * (n_max + 1)

    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return output

arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
print(count_sort(arr))
```
#### Key Information
- **Time Complexity**: \(O(n + k)\), where \(n\) is the size of the array and \(k\) is the range of elements.
- **Space Complexity**: \(O(k)\), for the count array.
- **Stability**: Counting Sort preserves the order of duplicate elements.
- **Limitation**: Efficient only for sorting integers or discrete values with a small range.


 #### Example Input and Output

```python
Input:  [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
Output: [1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6]
```

#### Usage in Projects

This algorithm is especially useful when:
- The range of numbers is known and small.
- Stable sorting is required for scenarios like sorting IDs or grades

### Counting Sort Algorithm (with Support for Negative Numbers)

Counting Sort can handle negative numbers by adjusting the range of the count array to include both negative and positive values. Here's how to implement it.

---

#### Implementation

```python
def count_sort(arr):
    n_min = min(arr)
    n_max = max(arr)
    range_size = n_max - n_min + 1

    count = [0] * range_size

    for num in arr:
        count[num - n_min] += 1
    for i in range(1, range_size):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - n_min] - 1] = arr[i]
        count[arr[i] - n_min] -= 1
    return output

arr = [4, -2, 2, 6, 3, -3, 1, 6, 5, -2, 3]
print(count_sort(arr))
```
#### Key Modifications for Negative Numbers
1. **Adjust Indexing**: Shift each number by subtracting the minimum value (\(n_{\text{min}}\)) to ensure all indices are non-negative.
2. **Count Array Range**: Define the range as `n_max - n_min + 1` to include both negative and positive numbers.
3. **Indexing in Count Array**: Use `num - n_min` to map elements correctly in the count array.

---

#### Key Information
- **Time Complexity**: \(O(n + k)\), where \(n\) is the size of the array and \(k\) is the range of elements.
- **Space Complexity**: \(O(k)\), for the count array.
- **Stability**: Maintains relative order of duplicates.
- **Limitation**: The algorithm's efficiency decreases with large ranges of numbers.

#### Example Input and Output

```python
Input:  [4, -2, 2, 6, 3, -3, 1, 6, 5, -2, 3]
Output: [-3, -2, -2, 1, 2, 3, 3, 4, 5, 6, 6]
```

#### Applications
- Sorting integers in datasets with mixed positive and negative values.
- Stable sorting for cases where duplicate ordering matters.

By extending Counting Sort to handle negatives, the algorithm becomes versatile for broader use cases




# **Bucket Sort Algorithm**  

## **Introduction**  
Bucket Sort is a **sorting algorithm** that distributes elements into multiple "buckets" and then sorts each bucket individually, either using another sorting algorithm or recursively applying bucket sort. It is particularly efficient when input values are **evenly distributed** over a range.  

## **Algorithm Steps**  
1. **Determine the bucket range**: Find the minimum and maximum values in the input array.  
2. **Create buckets**: Divide the range into a fixed number of buckets.  
3. **Distribute elements**: Place each element into the appropriate bucket.  
4. **Sort individual buckets**: Use **Insertion Sort** or any other efficient sorting algorithm.  
5. **Concatenate sorted buckets**: Merge the sorted values to form the final sorted array.  

## **Complexity Analysis**  
| Case          | Time Complexity  |  
|--------------|----------------|  
| Best Case    | \(O(n + k)\)   |  
| Average Case | \(O(n + k)\)   |  
| Worst Case   | \(O(n^2)\) (if all elements go into one bucket) |  

Where:  
- **n** is the number of elements,  
- **k** is the number of buckets.  

## **Implementation**  

### **Python Code**  
```python
def bucket_sort(arr):
    if len(arr) <= 1:
        return arr

    min_val, max_val = min(arr), max(arr)
    bucket_count = len(arr)  # Number of buckets
    bucket_size = (max_val - min_val) / bucket_count + 1

    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_val) / bucket_size)
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # Using Python's Timsort for sorting

    return sorted_arr

# Example usage
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
```

## **Example**  
**Input:**  
```bash
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
```
**Output:**  
```bash
[0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]
```

## **Advantages**
✅ **Fast** for uniformly distributed data.  
✅ **Linear time complexity** in the best case.  
✅ **Efficient for floating-point numbers.**  

## **Disadvantages**
❌ **Not suitable for small datasets.**  
❌ **Worst case can degrade to \(O(n^2)\).**  
❌ **Extra memory is needed for buckets.**  









