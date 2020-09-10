# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_head = ListNode()
        cur_result_node = result_head

        cur_l1, cur_l2 = l1, l2

        while cur_l1 is not None and cur_l2 is not None:
            temp_node = ListNode()

            if cur_l1.val <= cur_l2.val:
                temp_node.val = cur_l1.val
                cur_l1 = cur_l1.next
            else:
                temp_node.val = cur_l2.val
                cur_l2 = cur_l2.next

            cur_result_node.next = temp_node
            cur_result_node = cur_result_node.next

        if cur_l1 is not None:
            cur_result_node.next = cur_l1
        else:
            cur_result_node.next = cur_l2

        return result_head.next
