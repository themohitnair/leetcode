from typing import Optional, List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum_vals = val1 + val2
        dig = sum_vals % 10
        carry = sum_vals // 10

        result = ListNode(dig)

        l1_next = l1.next if l1 else None
        l2_next = l2.next if l2 else None
        
        result_next = self.addTwoNumbers(l1_next, l2_next)

        if carry:
            if result_next:
                result_next = self.addTwoNumbers(result_next, ListNode(carry))
            else:
                result_next = ListNode(carry)

        result.next = result_next         
            
        return result