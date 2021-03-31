# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 2021.03.31
        # NOTE: non-emtpy listnodes; non-leading zero (except for 0 itself)
        # l2 and l1 are in reversed order, so does the returned listnode
        # all values are non-negative
        
        # 4th solution: iterative, naive
        head = ListNode(0)
        l1_val, l2_val, res = l1.val, l2.val, head
        
        while l1 or l2:
            tmp = l1_val + l2_val + head.val
            if tmp < 10:
                head.val = tmp
                if l1 and l1.next:
                    head.next = ListNode(0)
                    head = head.next
                elif l2 and l2.next:
                    head.next = ListNode(0)
                    head = head.next
            else: 
                head.val = tmp - 10
                head.next = ListNode(1)
                head = head.next
            l1_val = l1.next.val if l1 and l1.next else 0
            l2_val = l2.next.val if l2 and l2.next else 0
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return res
        
        
        
        # 4th solution: 72 ms (51%) and 14.3 MB (73%)
        
