# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 2021.03.16
        # 1st solution: iterative and deque
        """
        p = root.left
        q = root.right
        m1 = list([p, ])
        m2 = list([q, ])
        
        while m1 and m2:
            p = m1.pop(0)
            q = m2.pop(0)
            if not self.checkBTreeSym(p, q):
                return False
            if p:
                m1.append(p.left)
                m1.append(p.right)
            if q:
                m2.append(q.right)
                m2.append(q.left)
        if not m1 and not m2:
            return True
        return False
        """
        
        # 2nd solution: recursive
        return self.isMirrored(root.left, root.right)
    
    
    def checkBTreeSym(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val != q.val:
            return False
        else:
            return True
    
    def isMirrored(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        return (p.val == q.val) and self.isMirrored(p.left, q.right) and \
                self.isMirrored(p.right, q.left)
    
    
    # 1st solution: 36 ms (60%) and 14.5 MB (47%)
    # 2nd solution: 36 ms (60%) and 14.1 MB (99%)
        
