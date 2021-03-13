索引：

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


  

