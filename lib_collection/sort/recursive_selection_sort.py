def sort(lst):
    """
    >>> lst = [5, 4, 3, 2, 1]
    >>> sort(lst)
    >>> lst
    [1, 2, 3, 4, 5]
    """
    _sort(lst, len(lst)-1)


def _sort(lst, slot):
    if slot == 0:
        return
    most = slot
    for i in range(slot):
        if lst[i] > lst[most]:
            most = i
    lst[most], lst[slot] = lst[slot], lst[most]
    _sort(lst, slot-1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
