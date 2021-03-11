class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # 2021.03.11
        # 1st: naive solution:
        lim = 2**31
        x_sign = 1 if x < 0 else 0 # deal with the negative sign
        r_str = '-' if x < 0 else ''
        for c in reversed(str(x)[x_sign:]):
            r_str += c
        if int(r_str) >= lim or int(r_str) < -lim: # overflow!
            return 0
        else:
            return int(r_str)
            
