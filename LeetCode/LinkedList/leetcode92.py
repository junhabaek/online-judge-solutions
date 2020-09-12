# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        header_node = None
        cur_idx = 1
        before, cur = None, head

        while cur_idx <= m:
            cur_idx = cur_idx + 1
            header_node = before
            before = cur
            cur = cur.next

        while cur_idx <= n:
            cur_idx = cur_idx + 1
            cur.next, before, cur = before, cur, cur.next

        if not header_node:
            head.next = cur
            result_head = before
        else:
            header_node.next.next, header_node.next = cur, before
            result_head = head

        return result_head
