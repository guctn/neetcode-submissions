# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or head.next == None:
            return
        # 01. we need to find the middle of the linked list
        slow, fast = head, head.next
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        # 02. reverse the second half - so we can know the last node, then return to the previous one, but actually just moving next
        prev, curr = None, slow.next
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr 
            curr = next_node

        # 03. now we need to link the first node from half one to the first node of half two (which is the last node from the original list) and then move both next and add them at the same order

        first, second = head, prev
        temp1, temp2 = first.next, second.next
        while temp1 != None or temp2 != None:
            first.next = second
            first = temp1
            temp1 = first.next
            if temp1 == None and temp2 == None:
                break
            second.next = first
            second = temp2
            temp2 = second.next




        