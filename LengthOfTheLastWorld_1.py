class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2021.03.13
        # 9th: reversed iterator
        try:
            assert len(s) > 1
        except:
            return 0 if s == " " else 1
        rev_iter = RevIter(s, len(s))
        counts = 0
        for c in rev_iter:
            if c != " ":
                counts += 1
            elif counts > 0:
                return counts
        return counts
        
class RevIter:
    def __init__(self, val, start):
        """ Set start value for the reverse iterator """
        self.val = val
        self.start = start
        self.count = start
    def __iter__(self):
        """ Make the class instance iterable """
        return self
    def next(self): # Python 2
    # def __next__(self): # Python 3
        """ Generate the next item if 0 is not reached yet """
        if self.count > 0:
            self.count -= 1
            return self.val[self.count]
        else:
            raise StopIteration
        
# Runtime: 20 ms (48%) and memory 13.6 MB (57%)
