class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2021.03.13
        # 11th: use generator, attempting to reduce memory
        # (but runtime is expected to be longer)
        try:
            assert len(s) > 1
        except:
            return 0 if s == " " else 1
        counts_bk = 0
        counts = 0
        for c in self.gen(s):
            if c != " ":
                counts += 1
            elif counts > 0:
                counts_bk = counts
                counts = 0
        if counts > 0:
            return counts
        else:
            return counts_bk
    
    def gen(self, str):
        for c in str:
            yield c
        
        
    # 11th runtime 12 ms (95%) and memory 13.7 MB (30%)
