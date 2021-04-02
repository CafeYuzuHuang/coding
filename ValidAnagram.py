class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2021.03.30
        # anagram means strings with same characters and number of each character
        
        # 1st solution: hash table
        # Time: O(n), space: ~ O(1) if alphabet set is far smaller than len(s)
        """
        if len(s) != len(t): return False
        rec_s = {}
        for i, c in enumerate(s):
            try:
                rec_s[c] += 1
            except:
                rec_s[c] = 1
        for j, d in enumerate(t):
            try:
                rec_s[d] -= 1
                assert rec_s[d] >= 0
            except:
                return False # character not in s, or negative value found
        return True
        """
        
        # 2nd solution: datatype conversion and sorting
        # Time: O(nlogn), space: O(n)
        """
        return False if sorted(list(s)) != sorted(list(t)) else True
        """
        
        # 3rd solution: optimized
        """
        if len(s) != len(t): return False
        if set(s) != set(t): return False
        return False if sorted(list(s)) != sorted(list(t)) else True
        """
        
        # 5th solution: recursive
        # time O(nlogn)~O(n^2), space O(logn)~O(n)
        """
        if len(s) != len(t): return False
        if len(s) == 0 and len(t) == 0: return True
        elif len(s) == 0 or len(t) == 0: return False
        return self.isAnagram(s.replace(s[0], ''), t.replace(s[0], ''))
        """
        
        # 6th solution: recursive
        ns, nt = len(s), len(t)
        if ns != nt: return False
        if ns == 0 and nt == 0: return True
        # elif ns == 0 or nt == 0: return False # unecessary statement since ns != nt is gueranteed, 2021.04.02 commented by baranee18
        return self.isAnagram(s.replace(s[0], ''), t.replace(s[0], ''))
        
        # 1st solution: 60 ms (20%) and 14.3 MB (99%)
        # 2nd solution: 52 ms (44%) and 15.5 MB (6%)
        # 3rd solution: 48 ms (61%) and 15.3 MB (6%)
        # 5th solution: 32 ms (98%) and 15.2 MB (6%)
        # 6th solution: 20 ms (100%) and 15.1 MB (6%)
        
