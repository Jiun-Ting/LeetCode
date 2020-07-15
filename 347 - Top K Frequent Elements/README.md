Problem: https://leetcode.com/problems/top-k-frequent-elements/
v0:
Strategy: use hash table and Counter, most_common(heapq.nlargest)in Python

Time Complexity: O(N)+O(NlogK), where N is the number elements
Space Complexity: O(N)

result:
Runtime: 96 ms, faster than 61.99% of Python online submissions for Top K Frequent Elements.
Memory Usage: 16.3 MB, less than 34.51% of Python online submissions for Top K Frequent Elements.


v0:
Strategy: use hash table(Counter) and heapq.nlargest

Time Complexity: O(N)+O(NlogK), where N is the number elements
Space Complexity: O(N)

result:(varies)
Runtime: 92 ms, faster than 76.15% of Python online submissions for Top K Frequent Elements.
Memory Usage: 16.5 MB, less than 9.14% of Python online submissions for Top K Frequent Elements.
