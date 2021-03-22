# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 2021.03.22
        # Both solutions found on the Internet ...
        
        # 1st solution: reversed list node method, 
        # O(N) time complexity, O(1) space complexity
        """
        if head and head.next and head == self.revListNode(head):
            return True
        return False
        
    def revListNode(self, head):
        before = None
        after = None
        while head:
            after = head.next
            head.next = before
            before = head
            head = after
        return before
        """
        
        # 2nd solution: O(N) time complexity and O(1) space complexity
        # Expect longer runtime, but easier to understand
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False
        
        # 1st solution: 44 ms (56%) and 20.4 MB (30%)
        # 2nd solution: 44 ms (56%) and 20.5 MB (15%)
        
        
