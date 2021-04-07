class Solution:
    def reverse(self, x: int) -> int:
        # 2021.04.07 revisited
        # x is in the range of [lower, upper], where
        # upper = 2^31-1 = 2147483647
        # lower = -2^31 = -2147483648
        # expected return should be within [lower, upper]; otherwise, return 0
        
        # 2nd solution: pop-and-push, numerical
        # time complexity: O(n*logn) (n: digits of int = log10(x))
        # space complexity: O(n) (returned y)
        """
        # if abs(x) < 10: return x
        sign = -1 if x < 0 else 1
        x, y = sign*x, 0
        lim = 2147483648 - max(0, sign)
        while x > 0:
            y *= 10
            y += x%10 # push
            x = x//10 # pop
            if y > lim: return 0 # overflow
        return sign*y
        """
        
        # 5th & 9th solution: push-and-pop, string ver.
        # time complexity: O(n) (n: digits of int = log10(x))
        # space complexity: O(n) (returned res)
        """
        if abs(x) < 10: return x
        res = ''
        isleading = True
        sign = 1
        if x < 0:
            res += '-'
            sign = -1
        lim = 2147483648 - max(0, sign)
        for i, c in enumerate(str(sign*x)[::-1]):
            if c != '0' and isleading: isleading = False
            if not isleading: res += c
            if len(res) >= 10 and int(res)*sign > lim: return 0
        return int(res)
        """
        
        # 6th solution: simplified code, but less efficient
        
        if abs(x) < 10: return x
        res, sign = '', 1
        if x < 0: res, sign = '-', -1
        lim = 2147483648 - max(0, sign)
        for i, c in enumerate(str(sign*x)[::-1]):
            res += c
        return int(res) if int(res)*sign <= lim else 0
        
        
        # 8th solution: 
        """
        if abs(x) < 10: return x
        res, sign, isleading = '', 1, True
        if x < 0:
            res, sign = '-', -1
        lim = 2147483648 - max(0, sign)
        x_str = str(sign*x)[::-1]
        i, n = -1, len(x_str)
        while isleading:
            i += 1
            if x_str[i] != '0' and isleading: isleading = False
        for j, c in enumerate(x_str[i:]):
            res += c
            if j > 9: return 0
            elif j == 9 and int(res)*sign > lim: return 0
        return int(res)
        """
        
        # 2nd solution: runtime 36 ms (34%) and memory 14.2 MB (46%)
        # 5th solution: runtime 28 ms (87%) and memory 14.2 MB (73%)
        # 6th solution: runtime 32 ms (66%) and memory 14.3 MB (12%)
        # 8th solution: runtime 32 ms (66%) and memory 14.3 MB (46%)
        # 9th solution: runtime 36 ms (34%) and memory 14.4 MB (12%)
        
