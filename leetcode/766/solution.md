Approach 1: Group by Category
Intuition and Algorithm

We ask what feature makes two coordinates (r1, c1) and (r2, c2) belong to the same diagonal?

It turns out two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.

This leads to the following idea: remember the value of that diagonal as groups[r-c]. If we see a mismatch, the matrix is not Toeplitz; otherwise it is.
Implementation
Complexity Analysis

    Time Complexity: O(M∗N). (Recall in the problem statement that M,N are the number of rows and columns in matrix.)

    Space Complexity: O(M+N).

Approach 2: Compare With Top-Left Neighbor
Intuition and Algorithm

For each diagonal with elements in order a1​,a2​,a3​,…,ak​, we can check a1​=a2​,a2​=a3​,…,ak−1​=ak​. The matrix is Toeplitz if and only if all of these conditions are true for all (top-left to bottom-right) diagonals.

Every element belongs to some diagonal, and it's previous element (if it exists) is it's top-left neighbor. Thus, for the square (r, c), we only need to check r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c].
Implementation
Complexity Analysis

    Time Complexity: O(M∗N), as defined in the problem statement.

    Space Complexity: O(1).
