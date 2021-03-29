# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 2021.03.29
        # Attempt to do it with time O(n) and space O(1)
        
        """
        # 1st solution: see
        # https://medium.com/@ChYuan/leetcode-no-234-palindrome-linked-list-%E5%BF%83%E5%BE%97-easy-58518af31fb
        if head.next is None: return True
        if head.next.next is None:
            return True if head.val == head.next.val else False
        bw_sh = self.getStartNode(head) # start head; make a copy 
        bw = self.revList(bw_sh) # reverse the last half part listnode
        while bw:
            try:
                assert bw.val == head.val
                bw, head = bw.next, head.next
            except:
                return False
        return True
        
    def getStartNode(self, head):
        slow = head
        fast = head
        while True:
            slow = slow.next
            fast = fast.next.next
            if not fast.next: return slow # odd nodes
            if not fast.next.next: return slow.next # even nodes
        
    def revList(self, head):
        #
        #        Head
        #  N1 --> N2 --> N3 --> N4 --> N5 --> None
        #         b      a            t = None 
        #         b <--- a       t
        #                b       a       
        #                b <---  a      t
        # ...
        #
        before = None
        after = head
        tmp = None
        while after:
            tmp = after.next
            after.next = before
            before = after
            after = tmp
        return before
        """
        
        # 2nd solution: see
        # https://leetcode.com/problems/palindrome-linked-list/discuss/1115409/Python-Iteration
        if not head or not head.next: return True
        pre, fast, slow = None, head, head
        while fast and fast.next:
            fast = fast.next.next # forward fast pointer
            slow.next, pre, slow = pre, slow, slow.next # reversed slow pointer
        if fast: slow = slow.next # slow and pre are crossed
        while slow and slow.val == pre.val:
            slow = slow.next # forward
            pre = pre.next # backward
        return not pre # pre is None if whole listnodes is visited
        
        # 1st solution: 772 ms (36%) and 39.5 MB (35%)
        # 2nd solution: 672 ms (45%) and 31.4 MB (49%)
        
