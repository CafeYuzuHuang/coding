class Solution:
    def isHappy(self, n: int) -> bool:
        # 2021.03.26 
        # oth solution: naive
        # Time limit exceed during testing...
        """
        res = n
        val = n
        while res > 1:
            res = 0
            for i, c in enumerate(str(val)):
                res += int(c)**2
            val = res
        return True if res == 1 else False
        """
        
        # 1st solution: naive with tricks
        # 1 -> happy
        # 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 2
        # 3 -> 9 -> 81 -> 65 -> 61 -> 37 -> ... -> 2
        # 4 ... -> 2
        # 5 -> 25 -> 29 -> 85 -> 89 -> ... 2
        # 6 -> 36 -> 45 -> 41 -> 17 -> 50 -> 5 -> ... 2
        # 7 -> 49 -> 97 -> 130 -> 10 -> 1 -> happy
        # 8 -> 64 -> 52 -> 29 ... 2
        # 9 -> 81 -> 65 -> ... 2
        # Thus, only 1 and 7 are happy for 0 <= n <= 9
        # The above induction is equivalent to create a map or dict that
        # dict = {1: T, 2: F, 3: F, ... 7: T, 8: F, 9: F}
        """
        res = n
        val = n
        while res > 9:
            res = 0
            for i, c in enumerate(str(val)):
                res += int(c)**2
            val = res
        return True if res in [1, 7] else False
        """
        
        # 2nd solution: one more contraints
        # If a number visits twice, return False
        res = n
        val = n
        rec = {}
        while res > 9:
            try:
                assert res in rec
                return False # duplicated
            except:
                rec[res] = 1
            res = 0
            for i, c in enumerate(str(val)):
                res += int(c)**2
            val = res
        return True if res in [1, 7] else False
        # Less while looping times, but more memory usage and dict indexing time
        
        # 1st solution: 32 ms (84%) and 14.1 MB (78%)
        # 2nd solution: 36 ms (61%) and 14.2 MB (51%)
        
