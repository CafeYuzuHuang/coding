class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 2021.03.12
        # 4th solution: 
        nl = len(needle)
        dif = len(haystack) - nl
        try:
            assert haystack != "" or needle == ""
            assert dif >= 0
        except:
            return -1 # not found
        try:
            assert needle != ""
            assert needle != haystack
        except:
            return 0 # found at first
        
        for i in range(dif+1):
            try:
                assert needle == haystack[i:i+nl]
                return i
            except:
                pass
        return -1
        
        # 20 ms (65%), 13.7 MB (84%)
