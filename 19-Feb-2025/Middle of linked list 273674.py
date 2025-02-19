# Problem: Middle of linked list - https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow , fast = head , head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
