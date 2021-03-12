class Solution(object):
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 2021.03.12:
        # 1st solution: iterative solution look up via forums
        # Note the definition of ListNode data structure
        # l1 and l2 ARE listnode dtype, NOT linked list
        try:
            assert not l1 is None
        except:
            return l2
        try:
            assert not l2 is None
        except:
            return l1
        
        # dumped records merged listnodes
        # cur is the current listnode
        dumped = ListNode(None)
        cur = dumped
        while l1 != None and l2 != None:
            try:
                assert l1.val >= l2.val
                cur.next = l2
                l2 = l2.next
            except:
                cur.next = l1
                l1 = l1.next
            cur = cur.next # cur is overwritten, but dumped is not
        # find the tail:
        try:
            assert l1 != None
            cur.next = l1
        except:
            cur.next = l2
        return dumped.next
        # other choice: apply recursive solution
        
        # Note:
        # return dumped -> [None, a, b, c, ...]
        # return dumped.next -> [a, b, c, ...] (expected answer)
        # return dumped.next.next -> [b, c, ...]
        # return cur -> two values
        # return cur.next -> one value
