# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None 
        middle = head


        # loop 
        while middle != None:
            right = middle.next
            middle.next = left
            left = middle 
            middle = right 
        
        head = left
        return head

