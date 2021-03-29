class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 2021.03.29
        # 1st solution: solve it without iteration / recursion
        # 1: 1
        # 2: 10
        # 4: 100
        # 8: 1000
        # ...
        """
        if n <= 0: return False
        return True if int(str(bin(n)).replace(str(bin(n))[:3], \
                                               '0b0')[2:], 2) == 0 else False
        """
        
        # 2nd solution: optimized
        if n <= 0: return False
        elif n <= 2: return True
        return True if int(str(bin(n))[3:], 2) == 0 else False
        
        # 1st solution: 28 ms (87%) and 14.3 MB (41%)
        # 2nd solution: 32 ms (66%) and 14.1 MB (89%)
        
