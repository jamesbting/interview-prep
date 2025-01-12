Approach 1: Simulation
Intuition

The problem statement implies that the length of original must equal m×n, the total number of elements required to fill the matrix. So, we'll start by checking if it's possible to construct the array and return an empty array if not.

Next, we'll simulate filling the 2D matrix row by row using nested loops.

    Row (i): The row index i is directly controlled by the outer loop, which ranges from 0 to m-1. Each time the outer loop increments i, it moves to the next row.
    Column (j): The column index j is controlled by the inner loop, which ranges from 0 to n-1. As the inner loop increments j, it moves across the columns of the current row.

Algorithm

    Check if the length of the original array is equal to m * n:
        If not, return an empty 2D array.
    Initialize a 2D array resultArray of dimensions m×n.
    Create a variable index to keep track of the current position in the original array.
    Iterate through each row i of resultArray:
        For each row, iterate through each column j:
            Assign the element at the current index of the original array to resultArray[i][j].
            Increment index to move to the next element in original.
    After filling all elements, return the resultArray.

Implementation
Complexity Analysis

Let m and n be the number of rows and columns in resultArray, respectively.

    Time complexity: O(m×n)

    The algorithm initializes a 2D array and fills it using nested loops. The outer loop runs m times and the inner loop runs n times. Thus, the total number of iterations is m×n, which equals a time complexity of O(m×n).

    Space complexity: O(1)

    The output array has a space complexity of O(m×n). However, we do not consider input and output space as part of our space complexity calculations. Thus, the space complexity of the algorithm is constant.
