Problem: https://leetcode.com/problems/find-the-difference/
v0:
Strategy: transform string to list, Compare and substring

Time Complexity: O(S+T), where T is the length of longer string
Space Complexity: O(S), where S is the length of shorter string

result: (varies)
Runtime: 40 ms, faster than 20.38% of Python online submissions for Find the Difference.
Memory Usage: 12.6 MB, less than 93.58% of Python online submissions for Find the Difference.

v1:
Strategy: Use property of XOR. The number of same characters would be odd, which results their XOR to be 0.

Time Complexity: O(S+T)
Space Complexity: O(1)

result:
Runtime: 20 ms, faster than 89.98% of Python online submissions for Find the Difference.
Memory Usage: 12.8 MB, less than 33.69% of Python online submissions for Find the Difference.
