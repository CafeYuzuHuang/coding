class Solution:
    def romanToInt(self, s: str) -> int:
        # 2021.04.08 revisited
        # return value range: 1~3999
        # arg. string length range: 1~15
        
        # 1st: naive solution
        # lookup hash table O(1) + linear scan O(n)
        """
        sym_dict = {'M': 1000, 
                    'D': 500, 
                    'C': 100, 
                    'L': 50, 
                    'X': 10, 
                    'V': 5, 
                    'I': 1} # in descenting order
        res = 0
        n = len(s)-1
        while n >= 0:
            a = sym_dict[s[n]]
            res += a
            if n > 0:
                b = sym_dict[s[n-1]]
                if s[n] == s[n-1]: # II, VV, LL; III -> II + I
                    res += b
                    n -= 1
                elif a > b: # IX, XC, CM
                    res -= b
                    n -= 1
            n -= 1
        return res
        """
        
        # 2nd solution: another approach, simplified
        sym_dict = {'M': 1000, 
                    'D': 500, 
                    'C': 100, 
                    'L': 50, 
                    'X': 10, 
                    'V': 5, 
                    'I': 1} # in descenting order
        res = 0
        ref = sym_dict[s[0]]
        for i, c in enumerate(s):
            v = sym_dict[c]
            if v <= ref: # II, VI, DC, ...
                res += v
            else: # IX, XC, CM ...
                res += v
                res -= 2*ref
            ref = sym_dict[s[i]]
        return res
        
        # 1st solution: 40 ms (92%) and 14.3 MB (28%)
        # 2nd solution: 44 ms (80%) and 14.3 MB (28%)
        
        
