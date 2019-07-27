def sort(lst):
    """
    >>> lst = [1, 4, 3, 2, 5]
    >>> sort(lst)
    >>> lst
    [1, 2, 3, 4, 5]
    """
    n = len(lst)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[i]:
                lst[j], lst[i] = lst[i], lst[j]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
