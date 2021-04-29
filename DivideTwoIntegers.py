class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 2021.04.29
        # Note the constraints:
        # 32-bits
        # divisor != 0 (may be negative)
        
        # 2nd solution: bit operation
        # see https://knightzone.studio/2018/10/24/3944/leetcode%EF%BC%9A29-divide-two-integers/
        # e.g. 8 / 3 = 2
        # 1000 / 11 -> 1000 > 110 -> 1000 - 110 = 0010 = 10 -> 10 < 11 -> quotient = 10
        """
        negsign = True if (dividend < 0) != (divisor < 0) else False
        a, b = abs(dividend), abs(divisor)
        if a < b: return 0
        
        maxshiftdigits = 0 # max allowed: 32
        while a >= (b << maxshiftdigits): maxshiftdigits += 1
        
        res = 0
        for i in range(maxshiftdigits-1, -1, -1):
            shiftval = b << i
            if shiftval <= a:
                res += 1 << i
                a -= shiftval
        if not negsign and res > 2147483647: res = 2147483647 # overflow
        return -res if negsign else res
        """
        
        # 3rd solution: optimized?
        
        negsign = True if (dividend < 0) != (divisor < 0) else False
        a, b, res = abs(dividend), abs(divisor), 0
        if a < b: return res
        for i in range(32, -1, -1):
            shiftval = b << i
            if shiftval <= a:
                res += 1 << i
                a -= shiftval
        if not negsign and res > 2147483647: res = 2147483647 # overflow
        return -res if negsign else res
        
        # 2nd solution: 36 ms (46%) and 13.9 MB (99%)
        # 3rd solution: 28 ms (90%) and 14.2 MB (54%)
