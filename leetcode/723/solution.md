Overview

The game process may be somewhat complex. Let's start by understanding the game steps and finding the corresponding actions for each step. We can divide this game into several (potentially repeating) steps:

    find
    crush
    drop

Find stands for finding all crushable candies, crush represents the elimination of adjacent candies, while drop involves rearranging the candies and making the ones above fall down. We mention that these steps are potentially repeated because after a drop, the rearranged candies may form new groups of candies to be crushed, requiring us to repeat the steps until we can no longer find a group of crushable candies.

img
Approach 1: Separate Steps: Find, Crush, Drop
Intuition

Starting from the first step: find and mark cells in the current board to be crushed. One simple approach is to check if three candies in the same row or column centered around a particular cell (r, c), are the same. That is, either board[r][c] = board[r - 1][c] = board[r + 1][c], or board[r][c] = board[r][c - 1] = board[r][c + 1]. If certain candies meet these conditions and qualify as crushable candies, we can store their positions.

img

After iterating through all the cells, if no new candies to be crushed are found, it indicates that the game is over. Otherwise, we continue with crushing candies. We modify the values of the stored candy positions to 0, indicating that they have been eliminated. At this point, we have completed the second step of the game.

img

In the third step, we need to make the candies above fall down until they hit the bottom or another candy.

During this process, the candies can only fall downwards, meaning that each column of the board is independent. It would be helpful to discuss them separately for easier computation.

img

For each column, we traverse from bottom to top. Throughout this process, we keep track of the position of the lowest 0 value. If the current cell is not 0, it will eventually fall to this lowest 0 position. Therefore, we swap its position with the position of the lowest 0, and raise the position of the lowest 0 by 1.

img

In summary, through the aforementioned three steps, we obtain a new board.

img

Next, we need to continue checking if there are any crushable candies in the new grid. If we discover new crushable candies, we repeat these steps again.

img

Finally, when no group of crushable candies can be found, it indicates that the game is over.

img

Algorithm

    Define find() to find all crushable candies:
        Initialize an empty set crushed_set.
        Iterate over each candy (r, c):
            If board[r][c] = 0, continue.
            If board[r][c] = board[r + 1][c] = board[r - 1][c], add (r, c), (r + 1, c) and (r - 1, c) to the set. If board[r][c] = board[r][c + 1] = board[r][c - 1], add (r, c), (r, c + 1) and (r, c - 1) to the set.
        Return crushed_set.

    Define crush(crushed_set) to mark all crushable candies:
        Iterate over every candy (r, c) in crushed_set and set board[r][c] = 0.

    Define drop() to rearrange the candies' new positions based on the rules:
        Iterate over each column c.
        For each column, set lowest_zero as -1 since there is no lowest zero yet.
        Iterate candies (r, c) from bottom to top, for each candy board[r][c]. If board[r][c] is zero, update lowest_zero as lowest_zero = max(lowest_zero, r). If board[r][c] is non-zero and lowest_zero is not -1, then we swap board[r][c] with board[lowest_zero][c] and decrement lowest_zero by 1.

    While find() returns an non-empty set crushed_set:
        Perform crush(crushed_set).
        Perform drop().

    Return board when the while loop is complete.

Implementation
Complexity Analysis

Let m×n be the size of the grid board.

    Time complexity: O(m2⋅n2)
        Each find process takes O(m⋅n) time as we need to iterate over every cell of board.
        There could be at most O(m⋅n) independent drop steps to eliminate all valid candy groups, as shown in the picture below:

    img

    We can construct the following board where around half of the candies (2m⋅n​) are crushed, and each crush operation eliminates at most two groups (8) of candies. Therefore, we need at least 16m⋅n​ drops to obtain the final board.
        In summary, the time complexity in the worst-case scenario is O(m2⋅n2).


    Space complexity: O(m⋅n)

        In each find step, we store the crushable candies in crushed_set, there can be at most O(m⋅n) candies in the set (imagine all candies are of the same value).

        The drop and crush steps involve in-place modification and do not require additional space.


Approach 2: In-place Modification
Intuition

In the previous solution, we require O(m⋅n) auxiliary space to store the candies that needed to be crushed at each step. Now, we can improve the way we mark the candies, allowing us to directly record the candies that need to be crushed by updating board in-place.

We can change the value of the crushed candies to their negative values. For example, if board[r][c] = 1, we change it to board[r][c] = -1. This way, during the crush operation, we only need to change all negative values to 0.

However, this approach introduces a new problem. How do we determine other connected crushable candies? For example, as shown in the picture below, consider the column with [1,1,1,1]. If we mark the first three candies as -1, it becomes [-1,-1,-1,1]. According to the original comparing conditions, the last 1 will not be marked as crushable.

img

To address this, we can modify the original conditions to compare absolute values. With this modification, the last 1 will be changed to -1, since all of them have an absolute value of 1.

img

Algorithm

    Define find_and_crush() to find and eliminate all crushable candies:
        Set complete as True.
        Iterate over each candy (r, c):
            If board[r][c] = 0, continue.
            If abs(board[r][c]) = abs(board[r + 1][c]) = abs(board[r - 1][c]), update board[r][c], board[r + 1][c] and board[r - 1][c] as their negative absolute values. If abs(board[r][c]) = abs(board[r][c + 1]) = abs(board[r][c - 1]), update board[r][c], board[r][c - 1] and board[r][c + 1] as their negative absolute values. Update complete as False.
        Iterate over board and set each negative value as 0.
        Return complete.

    Define drop() to rearrange the candies' new positions based on the rules:
        Iterate over each column c.
        For each column, set lowest_zero as -1 since there is no lowest zero yet.
        Iterate candies (r, c) from bottom to top, for each candy board[r][c]. If board[r][c] is zero, update lowest_zero as lowest_zero = max(lowest_zero, r). If board[r][c] is non-zero and lowest_zero is not -1, then we swap board[r][c] with board[lowest_zero][c] and decrement lowest_zero by 1.

    While find_and_crush() returns False:
        Perform drop().

    Return board when the while loop is complete.

Implementation
Complexity Analysis

Let m×n be the size of the grid board.

    Time complexity: O(m2⋅n2)
        Each find_and_crush process takes O(m⋅n) time as we need to iterate over every cell of board.
        There could be at most O(m⋅n) independent drop steps to eliminate all valid candy groups.
        In summary, the time complexity in the worst-case scenario is O(m2⋅n2).

    Space complexity: O(1)
        Both the function drop and find_and_crush involve in-place modification and do not require additional space.

