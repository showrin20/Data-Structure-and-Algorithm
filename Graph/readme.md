## [Codes of Graphs](https://docs.google.com/document/d/1aSFCw0m3sRzeHuRBBFoL8GCcObWVmqjEwuaE84P96lw/edit?usp=sharing)
# Graph Representation

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

