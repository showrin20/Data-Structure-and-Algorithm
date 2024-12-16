## [Codes of Graphs](https://docs.google.com/document/d/1aSFCw0m3sRzeHuRBBFoL8GCcObWVmqjEwuaE84P96lw/edit?usp=sharing)
# Graph Representation
## Adjacency Matrix
```python
# Read input and output file handles
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

# Read the number of nodes (n) and edges (m)
n, m = [int(x) for x in f1.readline().split()]

# Create an adjacency matrix initialized with zeros
adj_matrix = [[0] * (n + 1) for _ in range(n + 1)]

# Fill adjacency matrix with edge weights
for _ in range(m):
    u, v, w = [int(x) for x in f1.readline().split()]
    adj_matrix[u][v] = w

# Write the adjacency matrix to the output file
for row in adj_matrix:
    f2.write(" ".join(map(str, row)) + "\n")

# Close input and output files
f1.close()
f2.close()
```

---

### Key Points:
1. **Adjacency Matrix Initialization**:  
   A 2D matrix of size `(n+1) x (n+1)` is created to include 1-based indexing.

2. **Edge Weight Assignment**:  
   Each edge is read, and the weight `w` is placed at position `[u][v]` in the matrix.

3. **Output Formatting**:  
   The adjacency matrix rows are converted to space-separated strings using `" ".join(map(str, row))`, ensuring clean output.


### Input (`input.txt`):
```
4 3
1 3 8
3 2 5
1 4 2
```

### Output (`output.txt`):
```
0 0 0 0 0
0 0 0 8 2
0 0 0 0 0
0 0 5 0 0
0 0 0 0 0
``` 


### Explanation of Output:
- The first row and column correspond to the 0-indexed dummy entries (for clarity with 1-based indexing).
- Edge `(1, 3)` has weight `8`, so `adj_matrix[1][3] = 8`.
- Edge `(3, 2)` has weight `5`, so `adj_matrix[3][2] = 5`.
- Edge `(1, 4)` has weight `2`, so `adj_matrix[1][4] = 2`.  
All other positions remain `0` since no edges exist for those pairs.


### **Adjacency List Representation of an Undirected Graph**

This code reads an undirected graph from an input file and generates its adjacency list representation. The graph's nodes (vertices) and edges are read as input, and the adjacency list is saved in an output file. 

---

### **Description**

- **Input**: 
  - The input file contains two integers `n` (number of nodes) and `m` (number of edges) on the first line. 
  - The following `m` lines contain two integers `u` and `v`, representing an undirected edge between node `u` and node `v`.

- **Output**: 
  - The adjacency list is written to an output file, where each line corresponds to a node. 
  - Each line starts with a node followed by a list of its neighbors (connected nodes).



### **Code**

```python
# Open input and output files
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

# Read the number of nodes (n) and edges (m)
n, m = [int(i) for i in f1.readline().split()]

# Initialize the adjacency list as a dictionary
adj_list = {}

# Read each edge and update the adjacency list
for i in range(m):
    u, v = [int(i) for i in f1.readline().split()]
    
    if u not in adj_list:
        adj_list[u] = []  # Initialize list if 'u' is not already in adj_list
    adj_list[u].append(v)
    
    if v not in adj_list:
        adj_list[v] = []  # Initialize list if 'v' is not already in adj_list
    adj_list[v].append(u)

# Write the adjacency list to the output file
for key in adj_list:
    f2.write(f"{key}: ")
    for val in adj_list[key]:
        f2.write(f"{val} ")
    f2.write("\n")

# Close the input and output files
f1.close()
f2.close()
```

---

### **Input File: `input.txt`**

```
9 8
1 2
1 3
1 4
2 5
4 6
4 7
6 8
3 9
```

---

### **Output File: `output.txt`**

```
1: 2 3 4 
2: 1 5 
3: 1 9 
4: 1 6 7 
5: 2 
6: 4 8 
7: 4 
8: 6 
9: 3 
```



### **Explanation**

1. **Input Breakdown**:
   - `n = 9` (number of nodes), `m = 8` (number of edges).
   - Edges: 
     - (1, 2), (1, 3), (1, 4), (2, 5), (4, 6), (4, 7), (6, 8), (3, 9)

2. **Adjacency List Representation**:
   - For each node, the code maintains a list of its neighbors (connected nodes).
   - For example:
     - Node `1` is connected to nodes `2`, `3`, and `4`.
     - Node `2` is connected to nodes `1` and `5`.

3. **Output**:
   - Each line starts with a node followed by the list of its connected nodes.


# Graph traversal

### Breadth-First Search (BFS)

The BFS algorithm explores a graph in layers, starting from a given node and systematically visiting all its neighbors before moving to the next layer. It ensures that each node is visited only once, using a queue for tracking nodes to explore and a visited list to avoid revisiting nodes.

1. **Adjacency List Representation**: The graph is represented as a dictionary, where keys are nodes, and values are lists of neighboring nodes.
2. **Visited Tracking**: A list ensures nodes are not revisited, maintaining the BFS traversal order.
3. **Queue**: The `Deque` (double-ended queue) ensures nodes are processed in the correct order.
4. **Traversal Order**: The result reflects the BFS traversal sequence, level by level.


### **Python Code Implementation**

```python
from collections import deque

def bfs(adj_list, start):
    visited = []  # To track visited nodes
    queue = deque([start])  # Initialize the queue with the starting node
    traversal = []  # To store BFS traversal order
    
    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            visited.append(node)  # Mark the node as visited
            traversal.append(node)  # Add to traversal order
            for neighbor in adj_list[node]:  # Explore neighbors
                if neighbor not in visited:
                    queue.append(neighbor)  # Enqueue unvisited neighbors
    return traversal

```
### **Sample Input**

```
9 8
1 2
1 3
1 4
2 5
4 6
4 7
6 8
3 9
```


### **Output**

[1, 2, 3, 4, 5, 9, 6, 7, 8]


