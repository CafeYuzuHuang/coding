class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 2021.04.02
        # 0 <= digits.length <= 4, digits[i] in ['2', ... '9']
        
        # 1st solution: naive / iterative / brute force
        # time complexity O(n*4^n), space O(n)
        """
        if not digits: return []
        mapping = {'2': ['a', 'b', 'c'], 
                  '3': ['d', 'e', 'f'], 
                  '4': ['g', 'h', 'i'], 
                  '5': ['j', 'k', 'l'], 
                  '6': ['m', 'n', 'o'], 
                  '7': ['p', 'q', 'r', 's'], 
                  '8': ['t', 'u', 'v'], 
                  '9': ['w', 'x', 'y', 'z']}
        nd = len(digits)
        ind = [0]*nd
        indmax = [len(mapping[d])-1 for d in digits]
        res = []
        i = 0
        imax = 1
        for x in indmax:
            imax *= (x+1)
        while i < imax:
            tmp = ''
            for j, d in enumerate(digits):
                tmp += mapping[d][ind[j]]
            res.append(tmp)
            
            i += 1
            ind[0] += 1
            for ii in range(len(ind)):
                if ind[ii] > indmax[ii]:
                    ind[ii] = 0
                    try:
                        ind[ii+1] += 1
                    except:
                        pass
        return res
        """
        
        # 2nd solution: back-tracking:
        # see https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/
        nd = len(digits)
        if nd == 0: return []
        mapping = {'2': 'abc', 
                  '3': 'def', 
                  '4': 'ghi', 
                  '5': 'jkl', 
                  '6': 'mno', 
                  '7': 'pqrs', 
                  '8': 'tuv', 
                  '9': 'wxyz'}
        
        def backTrack(index, path):
            # index as int, path as list
            # index: current digit checking
            # path: current combination of letters we have
            
            # Case 1: finish examining all digits
            if len(path) == nd: # finished combination
                res.append(''.join(path)) # path = ['a', 'b', 'c'] -> res.append('abc')
                return None
            
            # Case 2: examining digit-by-digit
            tmp = mapping[digits[index]]
            for t in tmp: # loop through all possible letters
                path.append(t)
                backTrack(index+1, path) # go to next digit with holding current letter(s)
                path.pop() # remove current (last) letter before go next 
        
        res = []
        backTrack(0, [])
        return res
        
        # 1st solution: 36 ms (11%) and 14.4 MB (34%)
        # 2nd solution: 32 ms (58%) and 14.2 MB (86%)
        
