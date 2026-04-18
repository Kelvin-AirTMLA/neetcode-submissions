# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        l1 = list1
        l2 = list2
        dummy = ListNode()
        current = dummy

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
                current = current.next
            
            elif l1.val > l2.val:
                current.next = l2
                l2 = l2.next
                current = current.next

        # check for leftovers in case of unbalanced lists by length
        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next