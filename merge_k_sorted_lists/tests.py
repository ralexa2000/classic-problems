from merge_k_sorted_lists.divide_and_conquer import ListNode, merge_k_lists


def list_to_ListNode(l):
    next = None
    for li in reversed(l):
        next = ListNode(li, next=next)
    return next


def ListNode_to_list(ln):
    l = []
    while ln:
        l.append(ln.val)
        ln = ln.next
    return l


def test_common():
    l = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged = merge_k_lists(list(map(list_to_ListNode, l)))
    assert ListNode_to_list(merged) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_empty_lists():
    assert merge_k_lists([]) == None
    assert merge_k_lists([[]]) == []
    assert ListNode_to_list(
        merge_k_lists([list_to_ListNode([1, 2]), None, None])) == [1, 2]
