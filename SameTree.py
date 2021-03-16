# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 2021.03.16
        # 1st solution: naive, recursive
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.right, q.right) and \
                    self.isSameTree(p.left, q.left)
        """
        
        # 2nd solution: iteration
        # https://leetcode.com/problems/same-tree/solution/
        # About collections.deque: https://desolve.medium.com/%E5%BE%9E%E9%9B%B6%E9%96%8B%E5%A7%8B%E5%AD%B8python-23-588d3d7475d6
        data = deque([(p,q), ])
        while data:
            p, q = data.popleft()
            if not self.checkBTree(p, q):
                return False
            if p:
                data.append((p.left, q.left))
                data.append((p.right, q.right))
        return True
        
        # 3rd solution: iteration
        # Use list instead of deque
        """
        data = list([(p,q), ])
        while data:
            p, q = data.pop(0) # pop the 1st element; i.e. (p, q)
            if not self.checkBTree(p, q):
                return False
            if p:
                data.append((p.left, q.left))
                data.append((p.right, q.right))
        return True
        """
    
    def checkBTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val != q.val:
            return False
        else:
            return True
        
        # 1st solution: 28 ms (85%) and 14.2 MB (88%)
        # 2nd solution: 32 ms (62%) and 14.1 MB (88%)
        # 3rd solution: 28 ms (85%) and 14.4 MB (35%)
        
        # Note:
        # Time complexity: O(N) in worst case.
        # Space complexity: O(logN) for "balanced tree" and O(N) in worst case.
        # Structure to ensure balance: AVL tree, red-black tree, ...
        
