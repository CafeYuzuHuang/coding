class Solution:
    def intToRoman(self, num: int) -> str:
        # 2021.04.02
        # 1st solution: naive
        """
        res = ''
        n = num
        a, b = n % 1000, n // 1000
        if b > 0: # b < 4
            res = res + 'M'*b
        n = a
        
        a, b = n % 100, n // 100
        if b == 9: res += 'CM'
        elif b >= 5: res += 'D' + 'C'*(b-5)
        elif b == 4: res += 'CD'
        else: res += 'C'*b
        n = a
        
        a, b = n % 10, n // 10
        if b == 9: res += 'XC'
        elif b >= 5: res += 'L' + 'X'*(b-5)
        elif b == 4: res += 'XL'
        else: res += 'X'*b
        
        if a == 9: res += 'IX'
        elif a >= 5: res += 'V' + 'I'*(a-5)
        elif a == 4: res += 'IV'
        else: res += 'I'*a
        
        return res
        """
        
        # 2nd solution: more elegant
        res = ''
        roman_sym = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        for i, d in enumerate(str(num)[::-1]):
            k1 = roman_sym[2*i]
            try:
                k2 = roman_sym[2*i+1]
            except: # out-of-range (might happen in this problem)
                k2 = ''
            try:
                k3 = roman_sym[2*i+2]
            except: # out-of-range (might happen in this problem)
                k3 = ''
            res = self.returnRomanSym(int(d), k1, k2, k3) + res
        return res
        
    @staticmethod
    def returnRomanSym(digit, rs1, rs5, rs10):
        if digit == 9:
            return '' if rs10 == '' else rs1 + rs10
        elif digit >= 5:
            return '' if rs5 == '' else rs5 + rs1*(digit-5)
        elif digit == 4:
            return '' if rs5 == '' else rs1 + rs5
        else:
            return rs1*digit
        
        
        # 1st solution: 44 ms (85%) and 14 MB (95%)
        # 2nd solution: 52 ms (49%) and 14.2 MB (57%)
        
