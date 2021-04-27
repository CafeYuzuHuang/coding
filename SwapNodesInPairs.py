# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 2021.04.27
        # note: do not modify the value of each node
        # see: https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/24md.html
        
        if head == []: return head
        res = ListNode()
        res.next = head
        prev, cur = res, head
        
        while cur and cur.next:
            # Swap nodes:
            # cur.next.next -> cur.next
            # cur.next -> prev
            tmp = cur.next.next
            cur.next.next = cur
            prev.next = cur.next
            cur.next = tmp
            
            # Move to the next
            prev = cur
            cur = cur.next
        return res.next
        
        # 1st solution: 32 ms (58%), 14.2 MB (49%)
