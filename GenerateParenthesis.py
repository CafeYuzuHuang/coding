class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 2021.04.27
        # Since upper limit of n is not high, brute force may be acceptable
        # Well-formed:  # of "(" is larger or equal than ")" during the process
        
        # 1st solution: brute force
        # See: https://leetcode.com/problems/generate-parentheses/solution/
        # time complexity O(2^2n *n)
        # space complexity: O(2^2n *n)
        """
        def gen(A = []):
            if len(A) == 2*n:
                if valid(A): res.append("".join(A))
            else:
                A.append('(')
                gen(A)
                A.pop()
                A.append(')')
                gen(A)
                A.pop()
            
        def valid(A):
            chk = 0
            for c in A:
                if c == '(': chk += 1
                else: chk -= 1
                if chk < 0: return False
            return chk == 0
        
        res = []
        gen()
        return res
        """
        
        # 2nd solution: modified (backtrack method in solution #2
        # time complexity: O(4^n/n^0.5)
        # space complexity: O(4^n/n^0.5)
        
        def gen(l = 0, lmr = 0, A = []):
            if len(A) == 2*n: 
                res.append("".join(A)) # all generated seq. are valid
            else:
                if l < n:
                    A.append('(')
                    gen(l+1, lmr+1, A)
                    A.pop()
                if lmr > 0:
                    A.append(')')
                    gen(l, lmr-1, A)
                    A.pop()
        
        res = []
        gen()
        return res
        
        """
        # 3rd solution: iterative, enumerate
        # time complexity: O(4^n/n^0.5)
        # space complexity: O(4^n/n^0.5)
        # See: https://leetcode.com/problems/generate-parentheses/solution/
        if n == 0: return ['']
        res = []
        for c in range(n):
            for l in self.generateParenthesis(c):
                for r in self.generateParenthesis(n-1-c):
                    res.append('({}){}'.format(l, r))
        
        return res
        """
        
        # 1st solution: 112 ms (5%), 14.7 MB (39%)
        # 2nd solution: 28 ms (95%), 14.5 MB (87%)
        # 3rd solution: 36 ms (60%), 14.7 MB (39%)
        
