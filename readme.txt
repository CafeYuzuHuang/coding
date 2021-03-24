索引：請使用 Ctrl+F 搜尋關鍵字

1. Two Sum: https://leetcode.com/problems/two-sum/
  - brute force: time O(N^2), space O(1) (unsorted) or O(N) (sorted)
  - double dictionary comprehension
  - single dictionary comprehension: time O(N) (rarely O(N^2)) and space O(N)
  
7. Reverse Integer: https://leetcode.com/problems/reverse-integer/
  - naive: time O(N)
  - pop-and-push: time O(logN) see: https://leetcode.com/problems/reverse-integer/solution/
  
9. Palindrome Number: https://leetcode.com/problems/palindrome-number/
  - naive: time O(N), with try-except to boost up
  - time O(logN) and space O(1) see: https://leetcode.com/problems/palindrome-number/solution/
  
13. Roman to Integer: https://leetcode.com/problems/roman-to-integer/
  - naive: time O(N), space O(1)
  
14. Longest Common Prefix: https://leetcode.com/problems/longest-common-prefix/
  - naive (horizontal scanning): time O(N^2) in the worst case
  - recursive (vertical scanning): time O(N^2) in the worst case
  - divide-and-conquer, binary search, etc.: https://leetcode.com/problems/longest-common-prefix/solution/
  
20. Valid Parentheses: https://leetcode.com/problems/valid-parentheses/
  - stacking method with edge case screening: time O(N), space O(N)

21. Merge Two Sorted Lists: https://leetcode.com/problems/merge-two-sorted-lists/
  - iterative: time O(N) and space O(N)
  - recursive: not implemented yet

26. Remove Duplicates From Sorted Array: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
  - naive: time O(N)
  - cheated via datatype conversion: faster than naive
  
27. Remove Element: https://leetcode.com/problems/remove-element/
  - naive (Use remove method): time O(N)
  - other O(N) solutions: https://leetcode.com/problems/remove-element/solution/
  
28. Implement str Str(): https://leetcode.com/problems/implement-strstr/
  - naive, time O(N)
  
35. Search Insert Position: https://leetcode.com/problems/search-insert-position/
  - binary search (standard & variation), time O(logN), space O(1)
  
53. Maximum Subarray: https://leetcode.com/problems/maximum-subarray/
  - scanning: time O(N), space O(1)
  - divide-and-conquer: time O(N*logN), space O(N)
  
58. Length of Last Word: https://leetcode.com/problems/length-of-last-word/
  - naive: use split method
  - reverse iteration
  - forward generator

66. Plus one: https://leetcode.com/problems/plus-one/
  - naive: use dtype conversion and mathematical operation, O(N) time complexity
  - simulate the ADD algorithm, O(N) time complexity
  
67. Add Binary: https://leetcode.com/problems/add-binary/
  - induction method, character operation
  - use binary - integer decimal interconversion (if overflow issue does not matter)
  - short-cut method, one line statement (for python only)
  
69. Sqrt(x): https://leetcode.com/problems/sqrtx/
  - brute force
  - short cut
  - Newton-Raphson (implicit)
  - Newton-Raphson (explicit)
  - binary search
  
70. Climbing Stairs: https://leetcode.com/problems/climbing-stairs/
  - induction method: brute force, Fibonacci, or dynamic programming, time complexity O(N)
  - model solution with time complexity O(logN): see https://leetcode.com/problems/climbing-stairs/solution/
  
83. Remove Duplicates from Sorted List: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
  - naive, time complexity O(N)
  
88. Merge Sorted Array: https://leetcode.com/problems/merge-sorted-array/
  - naive, time complexity O(N), N = m+n
  
100. Same Tree: https://leetcode.com/problems/same-tree/
  - recursive, time complexity O(N), space complexity O(logN) to O(N)
  - iterative, time complexity O(N), space complexity O(logN) to O(N)
    (r.f.: https://leetcode.com/problems/same-tree/solution/ )

101. Symmetric Tree: https://leetcode.com/problemset/all/?status=Todo&difficulty=Easy
  - iterative
  - recursive

104. Maximum Depth of Binary Tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/
  - iterative / breath-first search (BFS): time complexity = O(N), space complexity <= O(N/2), where N is # of nodes
  - recursive / depth-first search (DFS): time complexity = O(N), space complexity = O(max_depth), limited by max stacks allowed during recursion.
  Source: 
  https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/959021/Python-BFS-and-DFS/780755/
  https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/

108. Convert Sorted Array to Binary Search Tree: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
  - recursion / divide-and-conquer / binary search: time complexity O(n), space complexity O(logn), both get PR = 100%
  Refer to: https://zxi.mytechroad.com/blog/tree/leetcode-108-convert-sorted-array-to-binary-search-tree/
  
110. Balanced Binary Tree: https://leetcode.com/problems/balanced-binary-tree/
  - recursive, post-order DFS: https://leetcode.com/problems/balanced-binary-tree/discuss/1116838/Python-PostOrder
  time complexity O(N), space complexity O(h_max), where N is # of nodes and h_max is the max depth

111. Minimum Depth of Binary Tree: https://leetcode.com/problems/minimum-depth-of-binary-tree/
  - iterative
  - recursive: https://ithelp.ithome.com.tw/articles/10213282
  
112. Path Sum: https://leetcode.com/problems/path-sum/
  - iterative

118. Pascal's Triangle: https://leetcode.com/problems/pascals-triangle/
  - iterative: dynamic programming, time complexity O(n^2), space complexity O(n), n is # of rows
    with mapping and lambda expression: https://blog.csdn.net/coder_orz/article/details/51589254
  - recursive + iterative model solution (recursive for computing factorial)

119. Pascal's Triangle II: https://leetcode.com/problems/pascals-triangle-ii/
  - recursive + iterative model solution (recursive for computing factorial)
  - recursive / dynamic programming
  
121. Best Time to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
  - brute force, time complexity O(n^2)
  - divide-and-conquer, time complexity O(N*logN)
  - one-pass, time complexity O(N) https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

122. Best Time to Buy and Sell Stock II: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
  - dynamic programming: time complexity O(N), space complexity O(N)
  
125. Valid Palindrome: https://leetcode.com/problems/valid-palindrome/
  - naive, time complexity O(N), space complexity O(1) or O(N)
  
136. Single Number: https://leetcode.com/problems/single-number/
  - brute force, time complexity O(N^2), space complexity O(1)
  - hash table: time complexity O(N), space complexity O(N)
  - model solution: time complexity O(N), space complexity O(1) !!  https://leetcode.com/problems/single-number/solution/
  
141. Linked List Cycle: https://leetcode.com/problems/linked-list-cycle/
  See https://blog.csdn.net/coder_orz/article/details/51516558

155. Min Stack: https://leetcode.com/problems/min-stack/
  - One-pass solution, time complexity O(1), space O(N)
  See https://www.coderbridge.com/@ninja-ja/889274a4faa84b639d8e239eed6acb16
  
160. Intersection of Two Linked Lists: https://leetcode.com/problems/intersection-of-two-linked-lists/
  - Naive, time complexity O(N), space complexity O(1)
  See https://medium.com/@ChYuan/leetcode-no-160-intersection-of-two-linked-lists-%E5%BF%83%E5%BE%97-10a32c1ac8a8

167. Two Sum II - Input array is sorted: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
  - single dictionary comprehension: r.f. problem 1
  - two-pointer approach: time complexity O(N), space complexity O(1)
  - binary search combined with for-loop scanning: time complexity O(NlogN), not implemented
  - brute force: O(N^2), not implemented
  
168. Excel Sheet Column Title: https://leetcode.com/problems/excel-sheet-column-title/
  - iterative and recursive solutions, both with time and space complexity O(logN)

169. Majority Element: https://leetcode.com/problems/majority-element/
  - math trick with one-pass, time complexity O(N), space complexity O(1)
  
171. Excel Sheet Column Number: https://leetcode.com/problems/excel-sheet-column-number/
  - naive

172. Factorial Trailing Zeroes: https://leetcode.com/problems/factorial-trailing-zeroes/
  - model solution, time complexity O(logn), space complexity O(1)
  







