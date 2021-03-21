class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 2021.03.21
        # 1st solution: model solution
        """
        r = rowIndex
        res = [1]*(r+1)
        if r <= 1: return res
        
        for i in range(1, r//2+1):
            res[i] = self.fac(r)/self.fac(r-i)/self.fac(i)
            res[r-i] = res[i]
        return res
        
    def fac(self, n): # factorial of n
        return n*self.fac(n-1) if n > 1 else 1
        """
        
        # 2nd solution:
        """
        r = rowIndex
        res = [1]*(r+1)
        if r <= 1: return res
        for i in range(1, r//2+1):
            res[i] = self.fac2(r, r-i)/self.fac2(i)
            res[r-i] = res[i]
        return res
    
    def fac2(self, n, m = 1):
        return n*self.fac2(n-1, m) if n > m else 1
        """
        
        # 3rd solution: recursive, dynamic programming
        r = rowIndex
        res = [1]*(r+1)
        if r <= 1: return res
        prev = self.getRow(r-1)
        for i in range(1, r):
            res[i] = prev[i-1] + prev[i]
        return res
        
        # 1st solution: 20 ms (27%) and 13.5 MB (14%)
        # 2nd solution: 20 ms (56%) and 13.5 MB (14%)
        # 3rd solution: 16 ms (83%) and 13.7 MB (6%)
    
