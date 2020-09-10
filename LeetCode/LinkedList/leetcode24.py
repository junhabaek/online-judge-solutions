# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp_header = ListNode(next=head)
        prior_node = temp_header
        left_node = head
        right_node = left_node.next if left_node else None

        while left_node and right_node:
            left_node.next, right_node.next = right_node.next, left_node
            prior_node.next = right_node

            prior_node = prior_node.next.next
            left_node = prior_node.next
            right_node = left_node.next if left_node else None

        return temp_header.next
