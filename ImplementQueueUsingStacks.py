class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 2021.03.29
        self.stack = []
        self.stack_bk = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # stack: [xn, xn-1, ..., x1, x0]
        for i in range(len(self.stack)):
            self.stack_bk.append(self.stack.pop())
        self.stack_bk.append(x) # [x0, x1, ... xn+1]
        for j in range(len(self.stack_bk)):
            self.stack.append(self.stack_bk.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if len(self.stack) == 0 else False

    # Runtime: 32 ms (51%), memory: 14.4 MB (44%)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
