# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 2021.04.13
        # Note: do this in one pass
        # Note: n <= L is guaranteed.
        
        # 1st solution: two-pass, time O(n), space O(1)
        # see https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/
        # goal: remove the (L - n + 1)th node.
        """
        dummy = ListNode()
        dummy.next = head
        first = head
        L = 0
        while first: # to get length of list
            L += 1
            first = first.next
        L -= n
        first = dummy
        while L > 0:
            L -= 1
            first = first.next
        # Now, we have
        #    ...   head   ...   L-n   L-n+1   ...
        #   ^dummy ^dummy.next
        #   ^first ----------> ^first (after while loop)
        #                             ^first.next
        first.next = first.next.next
        return dummy.next
        """
        
        # 2nd-3rd solution: one-pass, time O(n), space O(1)
        # see https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/
        # Hint: use two pointers to maintain the gap n
        # while the first reach the end, second.next points the ListNode need to be removed
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n+1): # move n+1 steps
            first = first.next
        while first: # move L-n steps
            first, second = first.next, second.next
        second.next = second.next.next
        return dummy.next
        
        # 1st solution: 28 ms (92%), 14.2 MB (49%)
        # 2nd solution: 36 ms (45%), 14.1 MB (92%)
        # 3rd solution: 36 ms (45%), 14.3 MB (16%)
        
