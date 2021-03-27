class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 2021.03.27
        # 2nd solution: naive
        # Such approach will be beaten by some terrible strings ...
        """
        n = len(s)
        if n == 1: return True
        i = 1
        n_s = 1
        n_t = 1
        while i < n:
            if s[i] != s[i-1]: # new character
                n_s += 1
            if s[i] in s[:i]: # appeared before
                n_s *= 10
            if t[i] != t[i-1]:
                n_t += 1
            if t[i] in t[:i]:
                n_t *= 10
            try:
                assert n_s == n_t
            except:
                return False
            i += 1
        return True
        """
        
        # 3rd solution: Python's trick for index matching
        # see: https://leetcode.com/problems/isomorphic-strings/discuss/1126975/Python3-one-liner-with-index
        """
        return [s.index(ch) for ch in s] == [t.index(ch) for ch in t]
        """
        
        # 4th solution: naive with dictionary
        """
        n = len(s)
        if n == 1: return True
        rec_s = {}
        rec_t = {}
        i = 0
        while i < n:
            try:
                rec_s[s[i]].append(i)
            except:
                rec_s[s[i]] = [i]
            try:
                rec_t[t[i]].append(i)
            except:
                rec_t[t[i]] = [i]
            try:
                assert rec_t[t[i]] == rec_s[s[i]]
            except:
                return False
            i += 1
        return True
        """
        
        # 5th solution: one-dictionary
        # r.f. Problme 1 (Two Sum)
        # Here only interested in the last matching of characters from s and t, 
        # not the whole indexing record. Use single dict to record the last
        # matching result so that it is more efficient than prev. solutions.
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                if t[i] in d.values(): # new c appears in s, but not in t
                    return False
                d[c] = t[i] # key: s; value: t
            else:
                if t[i] != d[c]: # old c in s, but new c in t
                    return False
        return True 
        
        # 2nd solution: wrong answer
        # 3rd solution: 44 ms (51%) and 15 MB (11%)
        # 4th solution: 64 ms (11%) and 15.6 MB (9%)
        # 5th solution: 36 ms (88%) and 14.4 MB (74%)
        
        
