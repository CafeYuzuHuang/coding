# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 2021.03.16
        # 1st solution
        if head is None:
            return head
        res = head
        while not head.next is None:
            if head.val < head.next.val:
                head = head.next
            else:
                head.next = head.next.next
        return res
    
        # 1st solution: 28 ms (81%) and 13.6 MB (14%)
    
