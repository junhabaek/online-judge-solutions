# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        length = 1
        last_idx = head

        while last_idx.next:
            last_idx = last_idx.next
            length = length + 1

        odd_idx, even_idx = head, head.next

        for i in range(length // 2):
            last_idx.next = odd_idx.next
            odd_idx.next = even_idx.next

            last_idx = last_idx.next
            odd_idx = odd_idx.next
            even_idx = odd_idx.next

        last_idx.next = None

        return head
