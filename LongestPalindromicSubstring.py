class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 2021.04.01
        # 1st solution: dynamic programming, 
        # O(n^2) time complexity, O(n) space complexity
        n = len(s)
        if n <= 1: return s
        
        start = 0
        end = 0
        for i in range(n):
            len1 = self.expandAroundCenter(s, i, i) # len1: odd
            len2 = self.expandAroundCenter(s, i, i+1) # len2: even
            lenmax = max(len1, len2)
            if (lenmax > end - start): # longer palindrome found
                start = i - (lenmax-1)//2
                end = i + lenmax//2
        return s[start:end+1]
        
    def expandAroundCenter(self, ssub, left, right):
        m = len(ssub)
        l, r = left, right
        while l >= 0 and r < m and ssub[l] == ssub[r]:
            l -= 1
            r += 1
        return r - l - 1
        
        
        # 1st solution: 812 ms (89%), 14.5 MB (39%)
        
