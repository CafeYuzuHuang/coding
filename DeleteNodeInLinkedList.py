# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 2021.03.30
        # "node" will not be the tail, but may be head
        # node values are UNIQUE
        
        # 1st solution: merge node
        node.val = node.next.val
        node.next = node.next.next
        
        
        
        # 1st solution: 40 ms (60%) and 15 MB (33%)
        
