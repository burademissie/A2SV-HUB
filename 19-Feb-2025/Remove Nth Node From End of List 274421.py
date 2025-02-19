# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        answer = ListNode(0,head)
        nod = head
        newnod = answer
        while nod and n>0:
            nod = nod.next
            n -= 1
        
        while nod:
            nod = nod.next
            newnod = newnod.next
        
        newnod.next = newnod.next.next
        return answer.next


        