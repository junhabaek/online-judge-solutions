# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        reverse_list = []
        cur_node = head

        while cur_node:
            reverse_list.append(cur_node.val)
            cur_node = cur_node.next

        cur_node = head
        result = True

        while cur_node:
            expected_val = reverse_list.pop()
            if cur_node.val != expected_val:
                result = False
                break
            cur_node = cur_node.next

        return result
