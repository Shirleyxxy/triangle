### Run Program
```
cd triangle
python solve-triangle.py triangle.txt
```
The answer to this problem is 732506.


### Solution
If the triangle is small, we could explore every possible route and find the maximum sum from top to bottom of the triangle. However, the input triangle has 100 rows. From each number, we could either move down and to the left or move down and to the right. Therefore, we have 2^99 different routes and it is computationally intensive to explore all of them.

In order to find the maximum sum, at first we start from the top cell of the triangle and go down to one of the two cells in the second row. Suppose we have already obtained the maximum sums by starting from either one of the two cells in the second row, then the solution will be the value of the top cell plus the greater sum starting from the second row. Similarly, if we start from a specific cell of the triangle, the maximum sum for that cell would be the value of that specific cell plus either the maximum sum obtained by starting from the cell down and to the left or the maximum sum obtained by starting from the cell down and to the right, whichever is greater.

Thus, we can approach this problem using **bottom-up dynamic programming**. The maximum sum for each cell in the bottom row is the value of the cell itself, so we could calculate the maximum sums for the cells above row by row in a bottom-up way. We also directly modify the value of each cell in the triangle to store the maximum sum obtained by starting from that specific cell to the bottom of the triangle. Essentially, we break the problem into smaller subproblems and start to find solutions to the subproblems from the bottom row. In the end, we only need to return the value of the top cell since it is the maximum sum obtained by starting from the top to bottom of the triangle, which is exactly what we want.


### Complexity Analysis
- **Time Complexity:**   
O(N) where N is the number of cells in the triangle. We loop through each cell from bottom to top and for each cell, we only consider two possible routes and use the pre-computed values from the cells in the row right below it.

- **Space Complexity:**   
O(1) since we modify the input triangle in-place. We do not use any extra space to obtain the final answer.
