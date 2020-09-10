# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i1, i2 = l1, l2

        result_header = ListNode()
        ri = result_header

        # 올림 수
        prior_rounds = 0

        while i1 and i2:
            prior_rounds, cur_value = divmod(i1.val + i2.val + prior_rounds, 10)
            ri.next = ListNode(val=cur_value)
            ri = ri.next
            i1 = i1.next
            i2 = i2.next

        while i1 or i2:
            remnant_node = None
            if i1:
                remnant_node = i1
                i1 = i1.next
            elif i2:
                remnant_node = i2
                i2 = i2.next

            if remnant_node:
                prior_rounds, cur_value = divmod(remnant_node.val + prior_rounds, 10)
                ri.next = ListNode(val=cur_value)
                ri = ri.next

        if prior_rounds:
            ri.next = ListNode(val=1)

        return result_header.next
