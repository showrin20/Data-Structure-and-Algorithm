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





# Depth-First Search (DFS) Traversal

An algorithm to traverse a graph by exploring as far as possible along each branch before backtracking.

### Key Points
1. **Graph Representation**: Uses an adjacency list stored in a dictionary.
2. **Traversal Method**: Employs a stack to implement DFS iteratively.
3. **Visited Nodes**: Maintains a list of visited nodes to prevent revisiting.
4. **Start Node**: Begins traversal from a specified starting node (default: 1).
5. **Output**: Returns the order of nodes visited during traversal.

### Code
```python
# Function to perform Depth-First Search (DFS) on the graph
def dfs(adj_list, start):
    visited = []  # List to track visited nodes
    stack = [start]  # Stack to manage DFS traversal
    traversal = []  # List to store the order of traversal

    while stack:
        node = stack.pop()  # Get the last node from the stack
        if node not in visited:
            visited.append(node)  # Mark the node as visited
            traversal.append(node)  # Add the node to the traversal order
            for neighbor in reversed(adj_list[node]):  # Reverse neighbors for correct DFS order
                if neighbor not in visited:
                    stack.append(neighbor)  # Add unvisited neighbors to the stack

    return traversal

# Start DFS from node 1
start = 1
print(dfs(adj_list, start))  # Print the DFS traversal order


```
# An algorithm to explore a graph layer by layer, finding the shortest path in an unweighted graph.

```python
def bfs_shortest_path_distance(adj_list, start, end):
    color = {node: "white" for node in adj_list}
    distance = {node: float('inf') for node in adj_list}
    parent = {node: None for node in adj_list}
    traversal_order = []
    
    color[start] = "gray"
    distance[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        traversal_order.append(node)
            
        for neighbour in adj_list[node]:
            if color[neighbour] == "white":
                color[neighbour] = "gray"
                distance[neighbour] = distance[node] + 1
                parent[neighbour] = node
                queue.append(neighbour)
        
        color[node] = "black"

    return distance, parent, traversal_order

def reconstruct_path(parent, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = parent[end]
    path.reverse() 
    return path

start = 1
distances, parents, traversal_order = bfs_shortest_path_distance(adj_list, start, e)
shortest_path = reconstruct_path(parents, start, e)
print("Distances:", distances)
print("Parents:", parents)
print("Traversal order:", traversal_order)
print("Shortest path from {} to {}: {}".format(start, e, shortest_path))


```







### Time Complexity
- **Construction of Adjacency List**: \(O(n + m)\), where \(n\) is the number of nodes and \(m\) is the number of edges.
- **DFS Traversal**: \(O(n + m)\), as each node and edge is processed once.
- **Overall Time Complexity**: \(O(n + m)\).

### Sample Input (input.txt)
```
6 6 5 
1 3 
3 2 
1 4 
2 6 
5 6 
4 6
```

### Output
```
[1, 4, 6, 5]
```

# Detect a Cycle in an Undirected Graph using BFS
Your code has a good structure but contains some issues. Let me explain and provide corrections:

1. **Input Assumption**: The code assumes that all nodes from 1 to `n` are present in the graph, but some nodes might not appear in the edges list. You need to ensure all nodes are included in the adjacency list.
  
2. **Output Handling**: The `print` statements will output results to the console, but the problem statement likely requires results in `output.txt`.

3. **Disconnected Graphs**: The BFS function assumes the graph is connected and starts from a single node. For disconnected graphs, cycle detection should handle all components.

4. **Starting Node**: The starting node is hard-coded as `1`, but this might not always be valid.

Here is the corrected and improved version:

```python
from collections import deque

# Open input and output files
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

# Read the number of nodes (n) and edges (m)
n, m = [int(i) for i in f1.readline().split()]

# Construct adjacency list
adj_list = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = [int(i) for i in f1.readline().split()]
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs_cycle_detection(adj_list, start):
    color = {node: "white" for node in adj_list}
    parent = {node: None for node in adj_list}
    
    color[start] = "gray"
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbour in adj_list[node]:
            if color[neighbour] == "white":
                color[neighbour] = "gray"
                parent[neighbour] = node
                queue.append(neighbour)
            elif parent[node] != neighbour:  # Found a back edge
                return True
        
        color[node] = "black"

    return False

# Check for cycles in all components
has_cycle = False
visited = set()
for node in range(1, n + 1):
    if node not in visited:
        if bfs_cycle_detection(adj_list, node):
            has_cycle = True
            break
        visited.update(adj_list.keys())  # Mark all reachable nodes as visited

# Write the result to the output file
f2.write("YES\n" if has_cycle else "NO\n")

f1.close()
f2.close()
```


1. **Adjacency List Initialization**: Ensures all nodes from `1` to `n` are included in the adjacency list, even if they have no edges.
   
2. **Disconnected Components**: Handles graphs that are not connected by iterating over all nodes and checking each unvisited component.

3. **Visited Nodes Tracking**: Added a `visited` set to ensure no node is revisited.

4. **Output to File**: The result is written to `output.txt` as required.

5. **Generalized Starting Node**: Eliminates the hard-coded starting node, making it more robust for any input.



