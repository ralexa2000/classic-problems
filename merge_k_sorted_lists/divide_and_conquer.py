from __future__ import annotations

import typing


class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next


def merge2lists(l1: ListNode, l2: ListNode) -> ListNode:
    cur = None
    first = None
    while l1 or l2:
        if (l1 and l2 and l1.val <= l2.val) or (l1 and not l2):
            if cur:
                cur.next = l1
            else:
                first = l1
            cur = l1
            l1 = l1.next
        else:
            if cur:
                cur.next = l2
            else:
                first = l2
            cur = l2
            l2 = l2.next

    return first


def merge_k_lists(lists: typing.List[ListNode]) -> ListNode:
    last = len(lists) - 1
    while last > 0:
        first = 0
        while first < last:
            lists[first] = merge2lists(lists[first], lists[last])
            first += 1
            last -= 1

    return lists[0] if len(lists) > 0 else None
