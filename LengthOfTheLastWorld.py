class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2021.03.13
        # 3rd solution ...
        """
        try: # note: s != ""; i.e. len(s) != 0
            assert len(s.split()) > 0 # split by any whitespace in sequence
        except:
            return 0
        return len(s.split()[-1])
        """
        # split method goes through whole string and generate a list
        # to store the result, which takes longer runtime and larger memory
        
        # 5th/6th solution:
        try:
            assert len(s) > 1
        except:
            return 0 if s == " " else 1
        counts = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                counts += 1
            elif counts > 0:
                return counts
        return counts
        
        # 7th/8th: refine 5th/6th ??
        """
        try:
            assert len(s) > 1
        except:
            return 0 if s == " " else 1
        counts = 0
        i = len(s)-1
        while i > -1: # to replace for loop with range method
            if s[i] != " ":
                counts += 1
            elif counts > 0:
                return counts
            i -= 1
        return counts
        """
        
        # 3rd runtime 16 ms (76%) and memory 13.6 MB (57%)
        # 5th runtime 12 ms (95%) and memory 13.8 MB (30%)
        # 6th (resubmit of 5th): 8 ms (100%!) and 13.7 MB (30%)
        # 7th runtime 20 ms and memory 13.7 MB
        # 8th runtime 12 ms and memory 13.9 MB
        
        
