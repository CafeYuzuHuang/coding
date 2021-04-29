索引：請使用 Ctrl+F 搜尋關鍵字

<Easy>

1. Two Sum: https://leetcode.com/problems/two-sum/
  - brute force: time O(N^2), space O(1) (unsorted) or O(N) (sorted)
  - double dictionary comprehension
  - single dictionary comprehension: time O(N) (rarely O(N^2)) and space O(N)
  ** revisited:
  - binary search with linear scan: time O(NlogN) (sorting) and space O(N)
  - two-pointer approach: time O(NlogN) (sorting) and space O(N)
  Posted as: https://leetcode.com/problems/two-sum/discuss/1146543/python-3-solutions-comparison-with-discussion-fastest-beats-95
  
7. Reverse Integer: https://leetcode.com/problems/reverse-integer/
  - naive: time O(N)
  - pop-and-push: time O(logN) see: https://leetcode.com/problems/reverse-integer/solution/
  ** revisited:
  - pop-and-push: time O(nlogn) where n = log10x is # of digits, space O(n)
  - reversed string and linear search: time O(n), space O(n)
  
9. Palindrome Number: https://leetcode.com/problems/palindrome-number/
  - naive: time O(N), with try-except to boost up
  - time O(logN) and space O(1) see: https://leetcode.com/problems/palindrome-number/solution/
  ** revisited:
  - reversed string and linear search: time O(n), space O(n) where n = log10x is # of digits
  - one-line string match: time O(n) and space O(n) but more efficient
  
13. Roman to Integer: https://leetcode.com/problems/roman-to-integer/
  - naive: time O(N), space O(1)
  ** revisited: simplified solution available
  
14. Longest Common Prefix: https://leetcode.com/problems/longest-common-prefix/
  - naive (horizontal scanning): time O(N^2) in the worst case
  - recursive (vertical scanning): time O(N^2) in the worst case
  - divide-and-conquer, binary search, etc.: https://leetcode.com/problems/longest-common-prefix/solution/
  ** revisited: modified above solutions
  
20. Valid Parentheses: https://leetcode.com/problems/valid-parentheses/
  - stacking method with edge case screening: time O(N), space O(N)

21. Merge Two Sorted Lists: https://leetcode.com/problems/merge-two-sorted-lists/
  - iterative: time O(N) and space O(N)
  - recursive: not implemented yet

26. Remove Duplicates From Sorted Array: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
  - naive: time O(N)
  - cheated via datatype conversion: faster than naive
  ** revisited: 
  - two-pointer method, r.f. solution: https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/
  
27. Remove Element: https://leetcode.com/problems/remove-element/
  - naive (Use remove method): time O(N)
  - other O(N) solutions: https://leetcode.com/problems/remove-element/solution/
  
28. Implement str Str(): https://leetcode.com/problems/implement-strstr/
  - naive, time O(N)
  ** revisited: prettify the code
  
35. Search Insert Position: https://leetcode.com/problems/search-insert-position/
  - binary search (standard & variation), time O(logN), space O(1)
  
53. Maximum Subarray: https://leetcode.com/problems/maximum-subarray/
  - scanning: time O(N), space O(1)
  - divide-and-conquer: time O(N*logN), space O(N)
  
58. Length of Last Word: https://leetcode.com/problems/length-of-last-word/
  - naive: use split method
  - reverse iteration
  - forward generator
  ** revisited:
  - reverse iteration
  - forward iteration

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
  
175 - 183 are SQL query problems:
175. Combine Two Tables: https://leetcode.com/problems/combine-two-tables/
176. Second Highest Salary: https://leetcode.com/problems/second-highest-salary/
181. Employees Earning More Than Their Managers: https://leetcode.com/problems/employees-earning-more-than-their-managers/
182. Duplicate Emails: https://leetcode.com/problems/duplicate-emails/
183. Customers Who Never Order: https://leetcode.com/problems/customers-who-never-order/

190. Reverse Bits: https://leetcode.com/problems/reverse-bits/
  - naive / iterative (math operation)
  - mask-and-shift: https://leetcode.com/problems/reverse-bits/solution/
  -> Far faster than iterative solution!

191. Number of 1 Bits: https://leetcode.com/problems/number-of-1-bits/
  - naive / data type conversion and counting
  - naive / iterative with bit operation

193 and 195 are BASH problems:
193. Valid Phone Numbers: https://leetcode.com/problems/valid-phone-numbers/
195. Tenth Line: https://leetcode.com/problems/tenth-line/

196 and 197 are MySQL query problems:
196. Delete Duplicate Emails: https://leetcode.com/problems/delete-duplicate-emails/
  Posted as: https://leetcode.com/problems/delete-duplicate-emails/discuss/1128063/Delete-Duplicate-Emails-faster-than-97
197. Rising Temperature: https://leetcode.com/problems/rising-temperature/

202. Happy Number: https://leetcode.com/problems/happy-number/
  - math induction to reduct computing time

203. Remove Linked List Elements: https://leetcode.com/problems/remove-linked-list-elements/
  - Naive, use dummy head; r.f. problem #83

204. Count Primes: https://leetcode.com/problems/count-primes/
  - Math: found all prime numbers or found all non-prime numbers
  - Math (Eratosthenes sieve) is the most efficient: see https://www.geeksforgeeks.org/sieve-of-eratosthenes/

205. Isomorphic Strings: https://leetcode.com/problems/isomorphic-strings/
  - index matching: See https://leetcode.com/problems/isomorphic-strings/discuss/1126975/Python3-one-liner-with-index
  - naive pattern matching with two dictionaries
  - pattern matching with one dictionary: See https://leetcode.com/problems/isomorphic-strings/discuss/1119546/Python-faster-than-99.19
  r.f. Problem 1 (Two Sum)

206. Reverse Linked List: https://leetcode.com/problems/reverse-linked-list/
  - Iterative: R.f. problem 141, 1st solution
  - Recursive: see https://leetcode.com/problems/reverse-linked-list/solution/

217. Contains Duplicate: https://leetcode.com/problems/contains-duplicate/
  - sorting, followed by iterative search
  - datatype conversion
  - hash table
  
225. Implement Stack using Queues: https://leetcode.com/problems/implement-stack-using-queues/
  - single queue solution, use pop(-1) and insert(0,) to behave like push from 0-index
  - two queues solution, use pop(-1) and append() (or insert(-1,)) to behave like push from 0-index

226. Invert Binary Tree: https://leetcode.com/problems/invert-binary-tree/
  - recursive / DFS: time complexity O(n), space complexity O(h) ~ O(n)
  - iterative: See https://leetcode.com/problems/invert-binary-tree/solution/

228. Summary Ranges: https://leetcode.com/problems/summary-ranges/
  - iterative, one-pass and naive

231. Power of Two: https://leetcode.com/problems/power-of-two/
  - iterarive or recursive method may be used, but not necessary
  - datatype conversion or bit operation

232. Implement Queue using Stacks: https://leetcode.com/problems/implement-queue-using-stacks/
  - naive / two-stack solution: O(n) in push operation, O(1) in pop operation
  Amortized O(1) time complexity for both pop and push: see approach #2 https://leetcode.com/problems/implement-queue-using-stacks/solution/

234. Palindrome Linked List: https://leetcode.com/problems/palindrome-linked-list/
  - fast-and-slow pointers / list reversion: time O(n), space (1)
  See: https://medium.com/@ChYuan/leetcode-no-234-palindrome-linked-list-%E5%BF%83%E5%BE%97-easy-58518af31fb
  More beautiful way: https://leetcode.com/problems/palindrome-linked-list/discuss/1115409/Python-Iteration

219. Contains Duplicate II: https://leetcode.com/problems/contains-duplicate-ii/
  - hash table, O(n) time and space complexity

235	Lowest Common Ancestor of a Binary Search Tree: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
  - recursion: See https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/
  - iterative: see above
  
237. Delete Node in a Linked List: https://leetcode.com/problems/delete-node-in-a-linked-list/
  - see: https://leetcode.com/problems/delete-node-in-a-linked-list/solution/

242. Valid Anagram: https://leetcode.com/problems/valid-anagram/
  - hash table --> time O(n), space O(1)
  - sorting --> time O(nlogn), space O(1)
  - recursion with replace (100% faster!) --> time O(n), space O(n)
  Posted as: https://leetcode.com/problems/valid-anagram/discuss/1134022/Python-3-recursion-with-replace-100-faster
  The discussion of time complexity is below the solution code.

257. Binary Tree Paths: https://leetcode.com/problems/binary-tree-paths/
  - recursion

258. Add Digits: https://leetcode.com/problems/add-digits/
  - math operation for O(1) time complexity, see https://leetcode.com/problems/add-digits/solution/
  (via mathematical induction or model solution known as mathenatical digit root)
  
263. Ugly Number: https://leetcode.com/problems/ugly-number/
  - naive, iterative or recursive

268. Missing Number: https://leetcode.com/problems/missing-number/
  - model solution: time O(n), space O(1)
  - bit manipulation: time O(n), space O(1), see https://leetcode.com/problems/missing-number/solution/

278. First Bad Version: https://leetcode.com/problems/first-bad-version/
  - binary search: time O(logn), space O(1)


<Medium>

2. Add Two Numbers: https://leetcode.com/problems/add-two-numbers/
  - iterative, naive, time complexity and space complexity: O(max(m, n))

3. Longest Substring Without Repeating Characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/
  - iterative, hash table + slide window, both time and space complexity are O(n)

5. Longest Palindromic Substring: https://leetcode.com/problems/longest-palindromic-substring/
  - dynamic programming, O(n^2) time complexity, O(n) space complexity
  - brute force, O(n^3) time complexity (skipped)
  - Manacher's algorithm: O(n) time complexity (skipped). 
    See https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm

6. ZigZag Conversion: https://leetcode.com/problems/zigzag-conversion/
  - See: https://leetcode.com/problems/zigzag-conversion/solution/

8. String to Integer (atoi): https://leetcode.com/problems/string-to-integer-atoi/
  - naive (scanning, iterative)

11. Container With Most Water: https://leetcode.com/problems/container-with-most-water/
  - brute force, time O(n^2), space O(1)
  - two-pointer, time O(n), space O(1)

12. Integer to Roman: https://leetcode.com/problems/integer-to-roman/
  - naive

15. 3Sum: https://leetcode.com/problems/3sum/
  - brute force, O(n^3) time complexity -> time limit exceeded
  - sorting, followed by using hash table: O(nlogn) ~ O(n^2) time complexity, O(n) space complexity
  - [Accepted] two-pointer with binary search: https://leetcode.com/problems/3sum/discuss/7653/Python-solution-.

16. 3Sum Closest: https://leetcode.com/problems/3sum-closest/
  - two-pointer, time complexity O(n^2)
  - binary search, time complexity O(n^2logn)
  - hash table approach cannot be applied to this problem since the target sum is not specific.
  r.f. https://leetcode.com/problems/3sum-closest/solution/

17. Letter Combinations of a Phone Number: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
  - naive, iterative, brute force; time complexity O(n*4^n), space complexity O(n)
  - back-tracking, recursive, brute force; same time and space complexity as above.
  See https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/

18. 4Sum: https://leetcode.com/problems/4sum/
  - hash set, recursive, time complexity O(n^3), space O(n). See https://leetcode.com/problems/4sum/solution/
  - two pointer, see https://leetcode.com/problems/4sum/solution/
  - iterative, combine two-pointer and bisection
  -> O(n^2logn) fails, O(n^3logn) required (rewinding one of the two pointers)

19. Remove Nth Node From End of List: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
  - two pass: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/
  - one pass: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/

22. Generate Parentheses: https://leetcode.com/problems/generate-parentheses/
  - brute force
  - back-track
  - iterative
  For the approaches above, see: https://leetcode.com/problems/generate-parentheses/solution/

24. Swap Nodes in Pairs: https://leetcode.com/problems/swap-nodes-in-pairs/
  - iterative, forward; see: https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/24md.html

29. Divide Two Integers: https://leetcode.com/problems/divide-two-integers/
  - bitwise operation: see https://knightzone.studio/2018/10/24/3944/leetcode%EF%BC%9A29-divide-two-integers/
  and https://leetcode.com/problems/divide-two-integers/discuss/1084803/Python-bitwise

31. Next Permutation: https://leetcode.com/problems/next-permutation/
  - single pass, see https://leetcode.com/problems/next-permutation/solution/



