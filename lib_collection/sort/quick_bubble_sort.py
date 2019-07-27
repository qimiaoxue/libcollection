def sort(lst):
    """
    >>> lst = [5, 4, 3, 2, 1]
    >>> sort(lst)
    >>> lst
    [1, 2, 3, 4, 5]
    """
    n = len(lst)
    done = False
    round = n - 1
    while not done and round:
        done = True
        for i in range(round):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                done = False
        round -= 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
