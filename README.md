In this repository, you will find Python implementations of popular data structures and algorithms. These implementations serve as examples and learning resources for those interested in understanding how these concepts work and how they can be implemented in Python.

## [Strivers A2Z DSA Course/Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)

## Data Structures

The repository currently includes implementations of the following data structures:

- Array
- Linked List
- Stack
- Queue
- Binary Tree
- Heap
- Hash Table
- Graph

Each data structure is implemented as a separate Python module and includes the necessary operations and functionalities associated with that particular data structure.

## Algorithms

The repository also includes implementations of various algorithms, including:

- Sorting Algorithms (e.g., Bubble Sort, Merge Sort, Quick Sort)
- Searching Algorithms (e.g., Linear Search, Binary Search)
- Graph Algorithms (e.g., Breadth-First Search, Depth-First Search, Dijkstra's Algorithm)
- Dynamic Programming Algorithms (e.g., Fibonacci Sequence, Knapsack Problem)

Similar to the data structures, each algorithm is implemented as a separate Python module and includes the necessary functions and methods to perform the desired operations.

Understanding the time complexity of algorithms is crucial for evaluating their efficiency and performance. In this repository, we provide time complexity analysis for each algorithm based on different scenarios. The following scenarios are considered:

- **Worst Case**: This represents the scenario where the algorithm takes the maximum amount of time to run, typically occurring when the input data is in its most unfavorable state.

- **Best Case**: This represents the scenario where the algorithm takes the minimum amount of time to run, typically occurring when the input data is in its most favorable state.

- **Average Case**: This represents the scenario where the algorithm takes an average amount of time to run, typically occurring when the input data is randomly distributed.

The time complexity analysis for each algorithm is provided in the respective module's documentation. It includes a discussion of the algorithm's time complexity in each of the scenarios mentioned above, allowing you to evaluate the algorithm's performance characteristics and make informed decisions based on your specific use case.

# **Bubble sort:** 
**repeatedly compares adjacent elements and swaps them if they are in the wrong order**
Bubble sort is a simple sorting algorithm that repeatedly steps through the list,compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm gets its name from the way smaller or larger elements "bubble" to the top of the list as the sort progresses. 
<br>While it is easy to understand and implement, bubble sort is not efficient for large data sets as its **time complexity is O(n^2)**.

# **selection sort:** 
**repeatedly selects the smallest or largest element and places it at the beginning or end of the list**

The **time complexity of selection sort is O(n^2)** as it involves nested loops to find the minimum element and swap it with the current element.

The space complexity of selection sort is O(1) as it only requires a single temporary variable for swapping elements and does not require any additional memory allocation.



