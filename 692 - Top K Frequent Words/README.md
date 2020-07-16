Problem: https://leetcode.com/problems/top-k-frequent-words/
v0:
Strategy: Build hash table by Counter and sort

Time Complexity: O(N) + O(NlogN), where N is the number of element
Space Complexity: O(N)

result: (varies)
Runtime: 52 ms, faster than 40.21% of Python online submissions for Top K Frequent Words.
Memory Usage: 12.7 MB, less than 83.25% of Python online submissions for Top K Frequent Words.

v1:
Strategy: Build hash table by Counter and use heap

Time Complexity: O(N) + O(NlogK), where N is the number of element
Space Complexity: O(N)

result: (varies)
Runtime: 72 ms, faster than 14.27% of Python online submissions for Top K Frequent Words.
Memory Usage: 13 MB, less than 20.36% of Python online submissions for Top K Frequent Words.
