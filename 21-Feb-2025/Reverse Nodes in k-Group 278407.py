# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        group = dummy
        
        while True:
            kth = group
            for _ in range(k):
                kth = kth.next
                # print(kth)  
                if not kth:
                    return dummy.next
                    
                
            group_next = kth.next
            group_start = group.next
            prev , curr = None , group_start
            

            for _ in range(k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                # print(next)

            group.next = prev
            group_start.next = curr

            group = group_start

        
        