# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answerdummy = ListNode(0)
        answer = answerdummy
        carry = 0
        while l1 or l2:
            value = carry
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            
            carry = value // 10
            value %= 10
            
            answer.next = ListNode(value)
            answer = answer.next

        if carry:
            answer.next = ListNode(1)

        return answerdummy.next
