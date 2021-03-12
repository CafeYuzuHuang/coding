class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 2021.03.12
        # 1st: naive solution
        """
        p_dict = {'{': '}', 
                  '[': ']', 
                  '(': ')'} # define pairs
        s_len = len(s)
        if s_len % 2 > 0: # odd characters
            return False
        c_stack = [] # for stacking
        for i, c in enumerate(s):
            try:
                assert p_dict[c_stack[-1]] == c # paired
                c_stack.pop()
            except:
                c_stack.append(c)
        try:
            assert c_stack == []
            return True
        except:
            return False
        """
        
        # 2nd/5th solution: attempt to boosting up
        
        n = len(s)
        try:
            # assert n > 0 # n is guaranteed not to be empty
            assert n % 2 == 0 # even characters
        except:
            return False
         
        p_dict = {'{': '}', 
                  '[': ']', 
                  '(': ')'} # define pairs
        c_stack = [] # __for stacking
        for i, c in enumerate(s):
            try:
                assert p_dict[c_stack[-1]] == c # paired
                c_stack.pop()
            except:
                try:
                    assert p_dict[c] != ''
                except: # ')', ']', and '}' should not be in stack!
                    return False
                c_stack.append(c)
        try:
            assert c_stack == []
            return True
        except:
            return False
        
        
        # 3rd/4th solution: attempt to boosting up
        """
        n = len(s)
        try:
            # assert n > 0 # n is guaranteed not to be empty
            assert n % 2 == 0 # even characters
        except:
            return False
        p_dict = {'{': '}', 
                  '[': ']', 
                  '(': ')'} # define pairs
        c_stack = [] # __for stacking
        nn = 0
        while nn < n:
            c = s[nn]
            try:
                assert p_dict[c_stack[-1]] == c # paired
                c_stack.pop()
            except:
                try:
                    assert p_dict[c] != ''
                except: # ')', ']', and '}' should not be in stack!
                    return False
                c_stack.append(c)
            nn += 1
        try:
            assert c_stack == []
            return True
        except:
            return False
        """
        # 1st: 24 ms (39%), 13.6 MB (65%)
        # 2nd: 16 ms (88%), 13.7 MB (37%)
        # 3rd & 4th: 24 ms (39%), 13.6 MB (65%)
        # 5th: 16 ms (88%), 13.6 MB (65%) !!
        # While is far slower than enumerate for loop!
