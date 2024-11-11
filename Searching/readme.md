# Linear Search Algorithm

## Overview
Linear Search is a straightforward searching algorithm that checks each element in a list sequentially to find a specified key. It is simple and useful for small or unsorted datasets but is generally slower for large lists.

## Key Points
- **Algorithm Type**: Sequential Search
- **Time Complexity**: 
  - Best Case: O(1) (key is the first element)
  - Average and Worst Case: O(n)
- **Space Complexity**: O(1)
- **Use Case**: Useful for small, unsorted datasets or when simplicity is needed.

## How It Works
1. Iterate through each element of the list one by one.
2. Check if the current element matches the search key.
3. If a match is found, return or print the index.
4. If the entire list is traversed without finding the key, return or print `-1`.

## Implementation
```python
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(i)
            return
    print(-1)

# Example
arr = [11, 77, 55, 9, 3]
key = 9
linear_search(arr, key)
```

# Binary Search Algorithm

## Overview
Binary Search is an efficient search algorithm that works on sorted arrays. It repeatedly divides the search interval in half, significantly reducing the number of comparisons required to find a target value compared to linear search.

## Key Points
- **Algorithm Type**: Divide and Conquer
- **Time Complexity**: 
  - Best Case: O(1) (if the middle element is the key)
  - Average and Worst Case: O(log n)
- **Space Complexity**: O(1) (iterative) or O(log n) (recursive)
- **Requirement**: The array must be sorted.
- **Use Case**: Ideal for large, sorted datasets.

## How It Works
1. Set the initial search range from the start (`l`) to the end (`r`) of the array.
2. Find the middle index (`mid`) of the current range.
3. If the middle element is the target (`key`), return the index.
4. If the middle element is less than the target, narrow the search to the right half.
5. If the middle element is greater than the target, narrow the search to the left half.
6. Repeat steps 2-5 until the target is found or the search range is empty.

## Implementation
```python
def binary_search(arr, key):
    l = 0
    r = len(arr) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1

# Example with a sorted array
arr = [3, 9, 11, 55, 77]
key = 9
result = binary_search(arr, key)
print("Index of key:", result)




