class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 2021.04.07 revisited
        
        # 2nd & 3rd solution: linear scan (iterative)
        
        if x < 0: return False
        if x < 10: return True
        x_str = str(x)
        for i, c in enumerate(x_str[:len(x_str)//2]):
            if c != x_str[-i-1]: return False
        return True
        
        
        # 4th solution: one-line
        # -> less memory used
        """
        return x >= 0 and str(x) == str(x)[::-1]
        """
        
        
        # 2nd solution: 60 ms (63%), 14.4 MB (16%)
        # 3rd solution: 60 ms (63%), 14.2 MB (49%)
        # 4th solution: 56 ms (77%), 14 MB (99%)
        
