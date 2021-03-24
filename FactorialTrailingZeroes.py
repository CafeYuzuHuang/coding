class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 2021.03.24
        # n -> n! = n x n-1 x ... x 2 x 1 x 0
        # If solve it: O(n!) ~ O(n^n)
        # Therefore, DO NOT solve this problem straightforward!
        # Trailing zero: 
        # If one 0: 5 x 2
        # If k 0s: (5 x 2) x k
        # -> Find # of 5 can be separated from n!:
        # k = n//5 + n//5^2 + ...
        
        # 1st solution: model solution
        # target time complexity O(logn)
        if n == 0: return 0
        a = 999
        f = 0
        res = 0
        while a > 0:
            f += 1
            a = n//(5**f)
            res += a
        return res
        
        # Time 32 ms (78%), memory 14.3 MB (23%)
