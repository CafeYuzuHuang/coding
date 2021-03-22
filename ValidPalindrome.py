class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 2021.03.22
        # 1st solution: naive
        
        i = 0
        j = len(s)
        while i < j:
            try:
                assert s[i].isalnum()
            except:
                i += 1
                continue
            try:
                assert s[j].isalnum()
            except:
                j -= 1
                continue
            try:
                assert s[i].lower() == s[j].lower()
                i += 1
                j -= 1
            except:
                return False
        return True
        
        
        # 2nd solution: naive, for comparison
        # Separate the preprocessing step from comparison step
        """
        snew = ''
        for i, c in enumerate(s):
            if c.isalnum(): # 0-9a-zA-Z
                snew += c.lower()
        n = len(snew)
        if n <= 1: return True
        for i in range(n//2):
            try:
                assert snew[i] == snew[n-1-i]
            except:
                return False
        return True
        """
        
        # 1st solution: 48 ms (49%) and 14.1 MB (75%)
        # 2nd solution: 364 ms (13%) and 15.2 MB (37%)
        
