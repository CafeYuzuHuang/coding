class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 2021.03.21:
        # 1st solution: iterative / dynamic programming
        # time complexity: O(N^2), space complexity: O(N), N is # of rows
        """
        res = [[1]] # guaranteed that numRows >= 1
        if numRows == 1:
            return res
        for i in range(1, numRows):
            tmp = [0]*(len(res[-1])+1)
            tmp[:-1] = [i for i in res[-1]]
            tmp[1:] = [tmp[i+1] + res[-1][i] for i in range(len(res[-1]))]
            res.append(tmp)
        return res
        """
        
        # 2nd solution: model solution, recursive
        # B[i, j] = C(i-1, i-1-j) = (i-1)!/(i-1-j)!/j!
        """
        res = [[1]] # guaranteed that numRows >= 1
        if numRows == 1: return res
        for i in range(1, numRows):
            res.append([self.fac(i)/self.fac(i-j)/self.fac(j) for j in range(i+1)])
        return res
        
    def fac(self, n): # factorial of n
        return n*self.fac(n-1) if n > 1 else 1
        """
        
        # 3rd solution: mapping (Python's trick)
        # identical to 1st solution but more simple and pretty
        
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res
        
        # 1st solution: 16 ms (76%) and 13.4 MB (38%)
        # 2nd solution: 20 ms (49%) and 13.5 MB (38%)
        # 3rd solution: 12 ms (96%) and 13.4 MB (38%)
        
        
        
        
