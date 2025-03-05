# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ihalf = ListNode()
        half = ihalf
        right = left = head
        while right and right.next:
            right = right.next.next
            half.next = ListNode(left.val)
            half = half.next
            left = left.next
        next = cur = left
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        ans = 0
        while prev:
            ans = max(prev.val + ihalf.next.val , ans)
            prev = prev.next
            ihalf.next = ihalf.next.next
        return ans

        