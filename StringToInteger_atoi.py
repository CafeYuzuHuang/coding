class Solution:
    def myAtoi(self, s: str) -> int:
        # 2021.04.01
        # ignore leading whitespace and rest characters other than digits
        
        # 3rd solution: naive
        # Time complexity: O(n) if digits << words, O(nlogn) otherwise
        # Space complexity: O(1) if digits << words, O(n) otherwise
        """
        if len(s) == 0: return 0
        readin = ''
        num = 0
        sign = 0 # -1 if negative, +1 if positive, 0 means unspecified
        lower = -2**31
        upper = -lower-1
        
        # chr(x) = c -> ord(c) = x; x is the ASCII code of character c
        for c in s:
            # Step 1
            if ord(c) == 32 and sign == 0 and readin == '': # leading whitespace
                continue
            # Step 2
            elif ord(c) == 43 and sign == 0: # plus sign
                sign = 1 # enter here 0 or 1 time
                continue
            elif ord(c) == 45 and sign == 0: # hyphen (minus sign)
                sign = -1 # enter here 0 or 1 time
                continue
            # step 3
            elif ord(c) >= 48 and ord(c) <= 57: # digits
                readin += c
                if sign == 0: sign = 1 # auto assign to be positive
                continue
            elif readin != '' or sign != 0: # rest characters
                break
            else: # leading non alphabets or other symbols
                break
        
        # str to int
        n = len(readin)
        if n == 0: return 0
        for r in readin:
            num += (ord(r)-48)*10**(n-1)
            n -= 1
        if sign == -1: num = -num
        
        # clamp by limits
        if num > upper: num = upper
        elif num < lower: num = lower
        return num
        """
        
        # 5th solution: optimized
        # space complexity: O(1)
        # time complexity: O(n)
        n = len(s)
        if n == 0: return 0
        num = 0
        sign = 0
        upper = 2147483647 # 2^31-1
        lower = -2147483648 # -2^31
        i = 0
        
        # step 1
        while i < n and s[i] == ' ': i += 1 # leading whitespace
        
        # step 2
        if i < n and s[i] in ['+', '-']:
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # step 3
        while i < n and ord(s[i]) >= 48 and ord(s[i]) <= 57:
            num = num*10 + (ord(s[i])-48)
            # if overflow, clamp the result and terminate the iteration
            if num > upper and sign != -1: return upper
            elif -num < lower and sign == -1: return lower
            i += 1
        
        # ignore the rest and return digits
        return -num if sign == -1 else num
        
        # 3rd solution: 40 ms (22%) and 14.1 MB (82%)
        # 5th solution: 40 ms (22%) and 14.3 MB (25%)
        
        
