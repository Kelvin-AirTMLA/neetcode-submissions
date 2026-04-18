# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        array = list()
        
        # Handle edge case: if both lists are empty
        if list1 == None and list2 == None:
            return None
        
        # Handle list1 (check if it's not empty first)
        if list1 != None:
            node_for_list1 = ListNode(val = 0, next=None)
            node_for_list1.val = list1.val
            array.append(node_for_list1.val)
            node_for_list1.next = list1.next
            
            if node_for_list1.next != None:
                var_next = node_for_list1.next
                array.append(var_next.val)
                
                while var_next.next != None:
                    var_next = var_next.next
                    array.append(var_next.val)
        
        # Handle list2 (check if it's not empty first)
        if list2 != None:
            node_for_list2 = ListNode(val = 0, next=None)
            node_for_list2.val = list2.val
            array.append(node_for_list2.val)
            node_for_list2.next = list2.next
            
            if node_for_list2.next != None:
                var_next2 = node_for_list2.next
                array.append(var_next2.val)
                
                while var_next2.next != None:
                    var_next2 = var_next2.next
                    array.append(var_next2.val)

        sorted_array = sorted(array)
        
        # Build the merged linked list from sorted array
        if not sorted_array:
            return None
        
        # Create head node
        head = ListNode(sorted_array[0])
        current = head
        
        # Build the rest of the list
        for val in sorted_array[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return head

        