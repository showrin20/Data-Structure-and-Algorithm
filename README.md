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
![Simulation](max_subarray.png)
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

## [Sorting Algorithms](https://github.com/showrin20/Data-Structure-and-Algorithm/tree/main/Sorting%20Algorithms)
1. Insertion Sort
2. Selection Sort
3. Merge Sort
4. Quick Sort
5. Heap Sort
6. Counting Sort
7. Radix Sort
8. Binary Search Applications
   - Binary Search on Arrays
   - Binary Search on Matrix

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




