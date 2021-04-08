class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 2021.04.08 revisited
        
        # 3rd: iterative solution, vertical scan
        # time complexity: O(m*n)
        # space complexity: O(1)
        """
        n = len(strs)
        if n == 0: return ''
        elif n == 1: return strs[0]
        
        pf_len_max = 1000 # max prefix length
        prefix = ''
        for s in strs:
            n = len(s)
            if n < pf_len_max: pf_len_max = n
        for i, c in enumerate(strs[0][:pf_len_max]):
            try:
                assert all( [ s[i] == c for s in strs[1:] ] )
                prefix += c
            except:
                break
        return prefix
        """
        
        # 7th solution: horizontal scanning
        """
        n = len(strs)
        if n == 0 or any( [s == '' for s in strs] ): return ''
        elif n == 1: return strs[0]
        ref = strs[0]
        pflen = len(ref)
        for s in strs[1:]:
            ifend = True # check if the following loop finishes normally
            for i, c in enumerate(s):
                if i > pflen-1 or c != ref[i]:
                    if i == 0: return ''
                    ifend = False
                    break
            pflen = i+1 if ifend else i # can be simplified: pflen = i + ifend (since True = 1, False = 0)
            ref = s
        return strs[0][:pflen]
        """
        
        # 9th solution: divide-and-conquer (recursive)
        # best case time complexity: O(m*n)
        # space complexity: O(m*logn), logn represents no. of stacks during recursion
        
        n = len(strs)
        if n == 0: return ''
        elif n == 1: return strs[0]
        lcp_len_max = 1000 # initialized by large value
        for s in strs:
            if len(s) < lcp_len_max: lcp_len_max = len(s)
        if lcp_len_max == 0: return ''
        
        # apply lcp_len_max and strs into the following functions
        def divide(l, r):
            if l == r: return strs[l][:lcp_len_max]
            m = (l + r)//2
            LCP_l, LCP_r = divide(l, m), divide(m+1, r)
            return conquer(LCP_l, LCP_r)
        
        def conquer(str1, str2):
            if len(str1) < len(str2):
                for i, c in enumerate(str1):
                    if str2[i] != c: return str2[:i] if i > 0 else ''
                return str1 # loop finished normally
            else:
                for i, c in enumerate(str2):
                    if str1[i] != c: return str1[:i] if i > 0 else ''
                return str2 # loop finished normally
        
        return divide(0, n-1)
        
        
        # 3rd solution: 32 ms (78%) and 14.3 MB (58%)
        # 7th solution: 36 ms (51%) and 14.4 MB (58%)
        # 9th solution: 36 ms (51%) and 14.2 MB (82%)
        
