# [Subarrays with Sum in Range](https://www.geeksforgeeks.org/problems/count-the-number-of-subarrays/1)
## Hard
Given an integer array arr[] and two integers l and r, find the number of subarrays whose sum lies in the range [l, r] (inclusive).
A subarray is a contiguous sequence of elements within the array.
Examples:
Input: l = 3, r = 8, arr[] = [1, 4, 6]
Output: 3
Explanation: The subarrays are [1,4], [4] and [6]. Therefore answer for this test case is 3.

Input: l = 4, r = 13, arr[] = [2, 3, 5, 8]
Output: 6
Explanation: The subarrays are [2, 3], [2, 3, 5], [3, 5], [5], [5, 8] and [8]. Therefore answer for this test case is 6.

Constraints:1 ≤ arr.size() ≤ 1051 ≤ arr[i] ≤ 1041 ≤ l ≤ r ≤ 109