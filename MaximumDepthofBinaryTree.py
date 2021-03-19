# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 2021.03.19 
        # Max depth ~10^4, extreme unbalanced binary tree!
        # For fully balanced tree: ~14
        
        # 1st solution: Use iterative method and scanning
        # Time complexity: O(N) = O(2^n); where N is # of nodes, n is the max depth
        # Space complexity: min O(1), max O(2^n-1) = O(N/2)
        # Balanced: 1 -> 2 -> 4 -> 8 ...
        # Unbalanced: e.g. 1 -> 2 -> 3 -> 6 ...
        """
        if root is None:
            return 0
        queue = list([root, ])
        max_depth = 1
        max_count = 2
        count_val = 0
        count_none = 0
        while len(queue) > 0:
            p = queue.pop(0)
            
            if p.left:
                queue.append(p.left)
                count_val += 1
            else:
                count_none += 1
            if p.right:
                queue.append(p.right)
                count_val += 1
            else:
                count_none += 1
            
            if (count_val + count_none) == max_count and count_val > 0:
                max_depth += 1
                max_count = 2 * count_val
                count_val = 0
                count_none = 0
        return max_depth
        """
        
        # 3rd solution: breadth-first search (BFS)
        # more elegant and simple than 1st solution
        """
        if not root:
            return 0
        max_depth, queue = 0, [(root, 1)]
        while queue:
            p, depth = queue.pop(0)
            max_depth = max(depth, max_depth)
            if p.left: queue.append((p.left, depth + 1))
            if p.right: queue.append((p.right, depth + 1))
        return max_depth
        """
        
        # 4th solution: recursive, depth-first search (DFS)
        # The most elegant approach
        # Pre-order, in-order, or post-order DFS does not matter here
        if not root:
            return 0
        return self.dfs(root)
        
    def dfs(self, p, depth = 0):
        if not p:
            return depth
        return max(depth, 
                   self.dfs(p.left, depth + 1), 
                   self.dfs(p.right, depth + 1))
        
        # 1st solution: 40 ms (77%) and 15.3 MB (97%)
        # 3rd solution: 40 ms (77%) and 15.3 MB (92%)
        # 4th solution: 36 ms (92%) and 16.7 MB (5%)
        
        
