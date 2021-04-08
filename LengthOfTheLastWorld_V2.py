class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 2021.04.08 revisited
        # Constraints:
        # (1) 1 <= s.length <= 10^4
        # (2) s consists of only English letters and spaces ' '.
        
        # 1st solution: use split method to generate list of substrings
        """
        try: # note: s != ""; i.e. len(s) != 0
            assert len(s.split()) > 0 # split by any whitespace in sequence
        except:
            return 0
        return len(s.split()[-1])
        """
        # split method goes through whole string and generate a list
        # to store the result, which takes longer runtime and larger memory
        
        # 2nd solution: iterative
        """
        if len(s) == 1: return 0 if s == " " else 1
        counts = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ": counts += 1
            elif counts > 0: break
        return counts
        """
        
        # 3rd solution: iterative, 2nd
        """
        if len(s) == 1: return 0 if s == " " else 1
        for i, c in enumerate(s[::-1]):
            if c != " ": break
        isend = True
        for j, c in enumerate(s[-i-1::-1]):
            if c == " ":
                isend = False
                break
        return j + isend
        """
        
        # 6th solution: forward iteration
        n = len(s)
        if n == 1: return 0 if s == " " else 1
        i, count = 0, 0
        while i < n:
            if s[-i-1] != " ": count += 1
            elif count > 0: break
            i += 1
        return count
        
        # 1st solution: 32 ms (48%) and 14.3 MB (37%)
        # 2nd solution: 28 ms (77%) and 14 MB (97%)
        # 3rd solution: 28 ms (77%) and 14.2 MB (65%)
        # 6th solution: 20 ms (99%) and 14.3 MB (37%)
        
