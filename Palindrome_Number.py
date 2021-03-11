class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # 2021.03.11:
        # 1st: naive solution
        x_s = str(x)
        for i, c in enumerate(x_s[:len(x_s)//2]):
            try:
                assert (c == x_s[-(i+1)])
            except:
                return False
        return True
        
        
        
