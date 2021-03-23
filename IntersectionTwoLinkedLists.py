# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 2021.03.23 
        # Restrict to time complexity O(N) and space O(1).
        # In addition, headA and headB are not allowed to be modified.
        # 2nd solution: Note the return type is ListNode instead of int.
        
        # Edge case:
        if headA is None or headB is None: return None
                
        # Find offset value = abs(countA - countB)
        tmpA, tmpB = headA, headB
        countA = countB = 1
        while tmpA.next:
            countA += 1
            tmpA = tmpA.next
        while tmpB.next:
            countB += 1
            tmpB = tmpB.next
        
        # Offset
        tmpA, tmpB = headA, headB
        if countA > countB:
            for i in range(countA-countB):
                tmpA = tmpA.next
        elif countA < countB:
            for i in range(countB-countA):
                tmpB = tmpB.next
        
        # Check if exists intersection
        while tmpA:
            if tmpA == tmpB:
                return tmpA
            tmpA = tmpA.next
            tmpB = tmpB.next
        return None
        
        # Runtime: 200 ms (53%); memory: 43.4 MB (34%)
        
