class FixedSizeMinPriorityQueue(object):

    def __init__(self, capacity=10):
        self.n = 0
        self.capacity = capacity
        self.keys = [None] * self.capacity

    def __len__(self):
        return self.n

    def _sink(self, n):
        """
        >>> q = FixedSizeMinPriorityQueue()
        >>> q.keys = [None, 3, 1, 2, None]
        >>> q.n = 3
        >>> q._sink(1)
        >>> q.keys
        [None, 1, 3, 2, None]
        >>> q = FixedSizeMinPriorityQueue()
        >>> q.keys = [None, 3, 2, 1, None]
        >>> q.n = 3
        >>> q._sink(1)
        >>> q.keys
        [None, 1, 2, 3, None]
        """
        keys = self.keys
        while n * 2 <= self.n:
            i = n * 2
            if i < self.n and keys[i+1] < keys[i]:
                i += 1
            if keys[n] <= keys[i]:
                break
            keys[n], keys[i] = keys[i], keys[n]
            n = i

    def pop(self):
        """
        >>> q = FixedSizeMinPriorityQueue()
        >>> q.insert(5)
        >>> q.insert(4)
        >>> q.insert(3)
        >>> q.insert(2)
        >>> q.insert(1)
        >>> q.pop()
        1
        >>> q.pop()
        2
        >>> q.pop()
        3
        >>> q.pop()
        4
        >>> q.pop()
        5
        """
        res = self.keys[1]
        self.keys[1], self.keys[self.n] = self.keys[self.n], self.keys[1]
        self.keys[self.n] = None
        self.n -= 1
        self._sink(1)
        return res

    @property
    def min(self):
        """
        >>> q = FixedSizeMinPriorityQueue()
        >>> q.min
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> q.insert(3)
        >>> q.min
        3
        >>> q.insert(2)
        >>> q.min
        2
        >>> q.insert(1)
        >>> q.min
        1
        >>> q.insert(4)
        >>> q.min
        1
        """
        if self.n == 0:
            raise IndexError('underflow')
        return self.keys[1]

    def insert(self, i):
        """
        >>> q = FixedSizeMinPriorityQueue(capacity=4)
        >>> q.insert(3)
        >>> q.insert(2)
        >>> q.insert(1)
        >>> q.keys
        [None, 1, 3, 2]
        """
        self.n += 1
        self.keys[self.n] = i
        self._swim(self.n)

    def _swim(self, n):
        """
        >>> q = FixedSizeMinPriorityQueue()
        >>> q.keys = [None, 2, 3, None, 1]
        >>> q.n = 4
        >>> q._swim(4)
        >>> q.keys
        [None, 1, 2, None, 3]
        """
        keys = self.keys
        while n > 1 and keys[n//2] > keys[n]:
            keys[n//2], keys[n] = keys[n], keys[n//2]
            n //= 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
