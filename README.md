# Data Structures and Algorithms

**Resources:**
## 1.[Strivers A2Z DSA Course/Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)
## 2.[Data Structures and Algorithm Coding Ninjas](https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms?utm_source=youtube&utm_medium=organic&utm_campaign=dsa_roadmap_20_apr)


## Arrays & Strings
1. Basic Array and String Questions
2. Traversal Based Problems
3. Rotation Based Problems
4. Sliding Window
5. Two Pointers
6. Kadane's Algorithm

### **Maximum Subarray Problem**
- **Problem Statement**: Find the contiguous subarray within a one-dimensional array of numbers that has the largest sum.  
- **Algorithm**: Kadane's Algorithm  
- **Key Points**:  
  - Initialize `max_current` and `max_global` to the first element of the array.  
  - Iterate through the array, updating `max_current` as `max(array[i], max_current + array[i])`.  
  - Update `max_global` whenever `max_current > max_global`.  
- **Attach Image/Diagram**:  
  *(Insert an image explaining the working of Kadane's Algorithm for Maximum Subarray)*

### **Code Implementation**
```python
def max_subarray(nums):
    max_current = nums[0]
    max_global = nums[0]

    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current

    return max_global

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", max_subarray(arr))
```
8. Dutch National Flag Algorithm
9. Multidimensional Arrays

## Recursion and Backtracking
1. Basic Recursion Questions
2. Divide and Conquer
3. Hard Recursion and Backtracking Questions

### **Divide and Conquer: Maximum Subarray Sum**
- **Problem Statement**: Find the contiguous subarray with the largest sum in an array using the Divide and Conquer approach.  
- **Key Idea**:
  - Divide the array into two halves.
  - Conquer each half recursively to find the maximum subarray sum in the left and right halves.
  - Combine the results by finding the maximum subarray sum that crosses the midpoint.  

![Simulation](max_subarray.png)

### **Code Implementation**
```python
def max_crossing_sum(nums, left, mid, right):
    # Find the maximum sum on the left half
    left_sum = float('-inf')
    temp_sum = 0
    for i in range(mid, left - 1, -1):
        temp_sum += nums[i]
        if temp_sum > left_sum:
            left_sum = temp_sum

    # Find the maximum sum on the right half
    right_sum = float('-inf')
    temp_sum = 0
    for i in range(mid + 1, right + 1):
        temp_sum += nums[i]
        if temp_sum > right_sum:
            right_sum = temp_sum

    # Return the sum of the left and right parts
    return left_sum + right_sum

def max_subarray_divide_and_conquer(nums, left, right):
    # Base case: only one element
    if left == right:
        return nums[left]

    # Find the middle point
    mid = (left + right) // 2

    # Recursively find the maximum subarray sum in left, right, and cross
    left_max = max_subarray_divide_and_conquer(nums, left, mid)
    right_max = max_subarray_divide_and_conquer(nums, mid + 1, right)
    cross_max = max_crossing_sum(nums, left, mid, right)

    # Return the maximum of the three
    return max(left_max, right_max, cross_max)

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum (Divide and Conquer):", max_subarray_divide_and_conquer(arr, 0, len(arr) - 1))
```
![a](0bdb096a-0065-4ebe-9ce2-dfaf527d8a72.jpeg)

### **Time Complexity**
- **Divide Step**: O(1) (Finding the middle index).  
- **Conquer Step**: Recursively solving two subproblems of size \(n/2\).  
- **Combine Step**: O(n) (Calculating the crossing sum).  
- **Total Complexity**: \(O(n \log n)\). 

## [Sorting Algorithms](https://github.com/showrin20/Data-Structure-and-Algorithm/tree/main/Sorting%20Algorithms)
1. Insertion Sort
2. Selection Sort
3. Merge Sort
4. Quick Sort
5. Heap Sort
6. Counting Sort
7. Radix Sort


## Linked Lists
1. Basic Linked List Operations
2. Reversal Problems
3. Sorting Problems
4. Slow and Fast Pointers
5. Modification in Linked List

## Stacks & Queues
1. Basic Stack and Queue Operations
2. Implementation Based Problems
3. Application Based Problems
4. Circular Queues
5. Deques - Hot Topic

## Hashmaps and Tries
1. Basic Hashmap Operations
2. Collision Resolution Techniques
3. Tries
4. Advanced Hashmap Problems

## Trees
1. Basic Tree Operations
2. Tree Traversals
3. Construction of Trees
4. Tree Views
5. Standard Problems
6. Binary Search Trees (BST)
   - Construction of BST
   - Conversion Based Problems
   - Modification in BST

## Heaps and Priority Queues
1. Basic Heap Operations
2. Implementation Based Problems
3. Conversion Based Problems
4. K Based Problems

## Graphs
1. Basic Graph Operations
2. Graph Traversals - BFS and DFS
3. Minimum Spanning Tree (MST)
4. Shortest Path Algorithms
5. Topological Sort
6. Graphs in Matrix

## Dynamic Programming
1. Basic DP Concepts
2. DP with Arrays
3. DP with Strings
4. DP with Mathematics
5. DP with Trees
6. Breaking and Partition Based Problems
7. Counting Based Problems

## Advanced Data Structures
1. Bit Manipulation
2. Greedy Algorithms
3. Doubly and Circular Linked Lists
4. String Algorithms like KMP and Z Algorithm



## Time Complexity
In this repository, we provide time complexity analysis for each algorithm based on different scenarios. The following scenarios are considered:

- **Worst Case**: This represents the scenario where the algorithm takes the maximum amount of time to run, typically occurring when the input data is in its most unfavorable state.

- **Best Case**: This represents the scenario where the algorithm takes the minimum amount of time to run, typically occurring when the input data is in its most favorable state.

- **Average Case**: This represents the scenario where the algorithm takes an average amount of time to run, typically occurring when the input data is randomly distributed.


# Master Theorem Overview

## Purpose
This guide explains the **Master Theorem**, a tool for solving recurrence relations in divide-and-conquer and subtract-and-conquer algorithms. It helps in analyzing algorithmic runtimes.



## Master Theorem for Divide and Conquer Recurrences
The general recurrence is:


![master](master.png)



### Examples
1. **Binary Search:**  
   **T(n) = T(n/2) + O(1)**  
   → **Θ(log(n))**

2. **Merge Sort:**  
   **T(n) = 2T(n/2) + O(n)**  
   → **Θ(n log(n))**

3. **T(n) = 3T(n/2) + n²**  
   → **Θ(n²)**


## Master Theorem for Subtract and Conquer Recurrences
The general recurrence is:

**T(n) = aT(n - b) + f(n)**  
Where:
- `a > 0`, `b > 0`, `f(n) = O(n^k)`

### Cases:
1. **If a < 1:**  
   **T(n) = O(n^k)**  
2. **If a = 1:**  
   **T(n) = O(n^(k+1))**  
3. **If a > 1:**  
   **T(n) = O(n^(k + a * n/b))**

## Limitations
The Master Theorem cannot be used if:
- **b ≤ 1** in **T(n) = aT(n/b) + c n^k**.
- The recurrence involves logarithms or non-polynomial functions.
- Subproblems are of unequal size.
- There are non-constant additive or non-polynomial growth terms.
- Multiple complex recurrences are combined.

## Examples
1. **Merge Sort**: **T(n) = 2T(n/2) + cn**
   - **a = 2, b = 2, k = 1**
   - Since **b^k == a**, **T(n) = Θ(n log n)** (Case 2).

2. **Binary Search**: **T(n) = T(n/2) + c**
   - **a = 1, b = 2, k = 0**
   - Since **b^k > a**, **T(n) = Θ(log n)** (Case 3).

