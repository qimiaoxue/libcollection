def sort(lst):
    """
    >>> lst = [1, 4, 3, 2, 5]
    >>> sort(lst)
    >>> lst
    [1, 2, 3, 4, 5]
    """
    n = len(lst)
    for i in range(n-1, 0, -1):
        most = i
        for j in range(i):
            if lst[j] > lst[most]:
                most = j
        lst[i], lst[most] = lst[most], lst[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
