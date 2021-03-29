class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 2021.03.29
        self.que = [] # 1st solution use single queue
        self.que_bk = [] # 2nd solution use two queues

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # 1st:
        """
        self.que.insert(0, x) # [xn, x0, x1, ...] <- top
        for i in range(len(self.que)-1):
            self.que.insert(0, self.que.pop()) # [x0, x1, ... xn]
        # Time complexity O(n^2): O(n) for each insert and loop n-1 ~ n times
        # pop() = pop(-1) has time complexity O(1)
        """
        
        # 2nd:
        # For queue structure, push from left side should be O(1) not O(n)
        # que: [x0, x1, x2,... xn]
        self.que_bk = [x]
        for i in range(len(self.que)):
            self.que_bk.append(self.que.pop()) # [xn+1, xn, ... x1, x0]
        for j in range(len(self.que_bk)):
            self.que.append(self.que_bk.pop()) # [x0, x1, ... xn+1]
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.que.pop() # O(1)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.que[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if len(self.que) > 0 else True

    # 1st runtime 32 ms (51%), memory 14.2 MB (75%)
    # 2nd runtime 28 ms (80%), memory 14.1 MB (98%)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
