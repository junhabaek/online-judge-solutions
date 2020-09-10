# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp_list = []
        cur_node = head

        result_head = ListNode()

        while cur_node:
            temp_list.append(cur_node.val)
            cur_node = cur_node.next

        cur_result_node = result_head

        while temp_list:
            temp_node = ListNode(temp_list.pop())
            cur_result_node.next = temp_node
            cur_result_node = temp_node

        return result_head.next
