def sort(lst):
    """
    >>> lst = [5, 4, 3, 2, 1]
    >>> sort(lst)
    >>> lst
    [1, 2, 3, 4, 5]
    """
    sublist_count = len(lst) // 2
    print('sublist_count: {}'.format(sublist_count))
    while sublist_count > 0:
        for i in range(sublist_count):
            print('sublist_count: {}, i: {}'.format(sublist_count, i))
            gap_insertion_sort(lst, i, sublist_count)
        sublist_count //= 2
        print('sublist_count_1: {}'.format(sublist_count))


def gap_insertion_sort(lst, start, gap):
    for i in range(start+gap, len(lst), gap):
        print('start+gap: {}, i: {}, gap: {}'.format(start+gap, i, gap))
        v = lst[i]
        print('v: {}'.format(v))
        j = i
        print('j: {}'.format(j))
        while j >= gap and lst[j-gap] > v:
            lst[j] = lst[j-gap]
            j -= gap
        lst[j] = v


if __name__ == '__main__':
    import doctest
    doctest.testmod()
