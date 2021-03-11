class Solution(object):
    def recurStrComp(self, s1, s2):
        try:
            assert s1 == s2
            return min(len(s1), len(s2))
        except:
            x = min(len(s1), len(s2)) - 1
            if x > 0:
                return self.recurStrComp(s1[0:x], s2[0:x])
            else:
                return x
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 2021.03.11
        # 1st: naive solution
        """
        n = len(strs)
        pf_len_max = 1000 # max prefix length
        prefix = ''
        for s in strs:
            pf_len_max = min(pf_len_max, len(s))
        for j in range(pf_len_max):
            try:
                c0 = strs[0][j]
                assert all( [strs[i][j] == c0 for i in range(n)] )
                prefix += c0
            except:
                break
        return prefix
        """
        
        # 5th solution: intend to save memory allocation (improvement of 1st)
        # Expected: time complexity O(n*m) -> O(n), space complexity O(m) -> O(1)
        n = len(strs)
        pf_len_max = 1000 # max prefix length
        prefix = ''
        for s in strs:
            ii = len(s)
            try:
                assert pf_len_max <= ii
            except:
                prefix = s
                pf_len_max = ii
                try:
                    assert pf_len_max > 0
                except:
                    return ''
        ii = pf_len_max # ii as tmp variable of pf_len_max
        for i, s in enumerate(strs):
            pf = prefix[0: ii]
            ss = s[0: ii]
            ii = self.recurStrComp(pf, ss)
            try:
                assert ii > 0
            except:
                return ''
        return prefix[0: ii]
        
        # The 1st approach runtime ~ 16ms (95%!!), memory 13.8 MB (40%);
        # whereas the 5th approach runtime ~ 24ms (59%), memory 13.7 MB (68%).
