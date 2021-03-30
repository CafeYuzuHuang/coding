class Solution:
    def addDigits(self, num: int) -> int:
        # 2021.03.30
        # try to solve w/o loop/recursion
        # loop/recursion: O(logn); target: O(1)
        
        # 1st solution: Use mathematical approach
        # see: https://leetcode.com/problems/add-digits/solution/
        # n = d0 + d1*10 + d2*100 + ...
        # = d0 + d1*(1+9) + d2*(1+99) + ...
        # = d0 + d1*(1+9*1) + d2*(1+9*11) + d3*(1+9*111) + ...
        # -> n%9 = sum(d0...dn)%9
        
        # Via mathematical induction: 
        # e.g. if n = 35972 --> return k; we know 0 <= k <= 9
        # n%9 = 8, 3+5+9+7+2 = 26, 26%9 = 8 -> 2+6 = 8 = k
        
        if num == 0: return 0
        if num%9 == 0: return 9
        return num%9
        
        # 1st solution: 24 ms (97%) and 14.2 MB (73%)
        
