# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 2021.03.27
        # 3rd solution:
        # time complexity: O(N), space complexity: O(N)
        if not head: return None
        res = None
        while head:
            if head.val != val and not res:
                res = head # start recording list
            while head.next and head.next.val == val:
                # Ensure next is not None, then check val
                head.next = head.next.next # avoid recording to res
            head = head.next
        return res
        
        # 3rd solution: 68 ms (72%) and 17 MB (99%)
        
