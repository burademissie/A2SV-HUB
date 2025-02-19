# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small , large = ListNode() , ListNode()
        sm , la = small , large

        while head:
            if head.val < x:
                sm.next = head
                sm = sm.next
            else:
                la.next = head
                la = la.next
            head = head.next

        la.next = None
        sm.next = large.next
        return small.next


        