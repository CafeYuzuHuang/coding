# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 2021.03.29
        # 1st solution:
        if not head: return head
        before = None
        after = None
        while head:
            after = head.next
            head.next = before
            before = head
            head = after
        return before
        
        # 1st solution: 32 ms (87%) and 15.6 MB (76%)
        
        
