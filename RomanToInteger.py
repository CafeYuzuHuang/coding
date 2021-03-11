class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2021.03.11:
        # 4th: naive solution
        sym_dict = {'M': 1000, 
                    'D': 500, 
                    'C': 100, 
                    'L': 50, 
                    'X': 10, 
                    'V': 5, 
                    'I': 1} # in descenting order
        val = 0
        n = len(s)-1
        while n >= 0:
            a = sym_dict[s[n]]
            val += a
            try:
                assert n > 0
                b = sym_dict[s[n-1]]
                if s[n] == s[n-1]: # II, VV, LL; III -> II + I
                    val += b
                    n -= 1
                elif a > b: # IX, XC, CM
                    val -= b
                    n -= 1
            except:
                pass
            n -= 1
        return val
        
