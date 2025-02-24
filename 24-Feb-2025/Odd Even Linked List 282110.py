# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: 
            return head
        odd = head
        even = head.next
        ehead = even
        while even != None and even.next != None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd=odd.next
            even= even.next
        odd.next = ehead
        return head