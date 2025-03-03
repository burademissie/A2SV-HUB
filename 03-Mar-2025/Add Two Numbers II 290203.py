# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = dummy2 = ListNode(0)
        dummy1.next = l1
        dummy2.next = l2
        prev = None
        cur = next = l1
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        prev1 = prev
        prev = None
        cur = next = l2
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        prev2 = prev

        carry = 0
        answer = ListNode(0)
        realanswer = answer
        
        while prev1 or prev2 or carry:
            add = carry
            if prev1:
                add += prev1.val
                prev1 = prev1.next
            if prev2:
                add += prev2.val
                prev2 = prev2.next
            carry = add // 10
            answer.next = ListNode(add % 10)
            answer = answer.next
            
        prev = None
        cur = next = realanswer.next
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev