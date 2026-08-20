# [Sequences where Adjacent Divide](https://www.geeksforgeeks.org/problems/count-in-array2138/1)
## Medium
Given two positive integer&nbsp;n and m. Find the number of arrays of size n that can be formed such that:

Each element is in the range [1, m].
All adjacent are such that one of them divide the another i.e element Ai&nbsp;divides Ai + 1&nbsp;or Ai+1&nbsp;divides Ai.

Examples:
Input: n = 3, m = 3
Output : 17
Explanation: The possible arrays are [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 3, 1], [1, 3, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 1], [2, 2, 2], [3, 1, 1], [3, 1, 2], [3, 1, 3], [3, 3, 1] and [3, 3, 3].

Input: n = 1, m = 10 
Output: 10
Explanation: The possible arrays are [1], [2], [3], [4], [5], [6], [7], [8], [9] and [10].
