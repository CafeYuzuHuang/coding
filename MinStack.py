class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 2021.03.23
        self.stack = []
        self.min_rec = []
    
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # Record min. value after pushing, say,
        # stack:   [] -> [2] -> [2,3] -> [2,3,1] -> [2,3]
        # min_rec: [] -> [2] -> [2,2] -> [2,2,1] -> [2,2]
        self.min_rec.append( min(self.min_rec[-1], val) if self.min_rec else val )
        return None
    
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_rec.pop()
        return None
    
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
    
    def getMin(self):
        """
        :rtype: int
        """
        # Retriving the min element with O(1) time complexity
        # However, the space complexity is O(N)
        return self.min_rec[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Note: all operations are O(1) time complexity, including list.appned() and list.pop(-1).
# Run time 44 ms (97%), memory 17.1 MB (100%) !!!
