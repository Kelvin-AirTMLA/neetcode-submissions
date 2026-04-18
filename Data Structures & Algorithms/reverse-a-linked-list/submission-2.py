# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3
        if head is None:
            return head

        prev = None # what is already reversed (nothing has been reversed)
        current = head # what I am trying to reversed

        while current:
            tmp = current.next # rest of the list that I need to reverse (so i dont lose it)
            current.next = prev # current.next = 1, prev = None

            prev = current # reversal has happened Hooray!!!!🔥
            current = tmp # current = 0
        
        return prev
