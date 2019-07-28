class FixedSizeMaxPriorityQueue(object):

    def __init__(self, capacity=10):
        self.n = 0
        self.capacity = capacity
        self.keys = [None] * self.capacity

    def __len__(self):
        return self.n

    @property
    def max(self):
        """
        >>> q = FixedSizeMaxPriorityQueue()
        >>> q.max
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> q.insert(3)
        >>> q.max
        3
        >>> q.insert(4)
        >>> q.max
        4
        >>> q.insert(5)
        >>> q.max
        5
        """
        if self.n == 0:
            raise IndexError('underflow')
        return self.keys[1]

    def pop(self):
        """
        >>> q = FixedSizeMaxPriorityQueue()
        >>> q.pop()
        Traceback (most recent call last):
            ...
        IndexError: underflow
        """
        if len(self) == 0:
            raise IndexError('underflow')
        res = self.keys[1]
        self.keys[1], self.keys[self.n] = self.keys[self.n], self.keys[1]
        self.keys[self.n] = None
        self.n -= 1
        return res

    def insert(self, k):
        """
        >>> q = FixedSizeMaxPriorityQueue(capacity=5)
        >>> q.insert(1)
        >>> q.insert(2)
        >>> q.keys
        [None, 2, 1, None, None]
        >>> q.insert(3)
        >>> q.keys
        [None, 3, 1, 2, None]
        >>> q.insert(4)
        >>> q.keys
        [None, 4, 3, 2, 1]
        """
        self.n += 1
        self.keys[self.n] = k
        self._swim(self.n)

    def _swim(self, n):
        """
        >>> q = FixedSizeMaxPriorityQueue()
        >>> q.keys = [None, 2, 1, 3]
        >>> q.n = 3 
        >>> q._swim(3)
        >>> q.keys
        [None, 3, 1, 2]
        """
        keys = self.keys
        while n > 1 and keys[n//2] < keys[n]:
            keys[n//2], keys[n] = keys[n], keys[n//2]
            n = n//2
            
    def _sink(self, n):
        """
        >>> q = FixedSizeMaxPriorityQueue()
        >>> q.keys = [None, 3, 4, 5]
        >>> q.n = 3
        >>> q._sink(1)
        >>> q.keys
        [None, 5, 4, 3]
        """
        keys = self.keys
        while n * 2 <= self.n:
            i = n * 2
            if i < self.n and keys[i+1] > keys[i]:
                i += 1
            if keys[n] >= keys[i]:
                break
            keys[n], keys[i] = keys[i], keys[n]
            n = i


if __name__ == '__main__':
    import doctest
    doctest.testmod()
