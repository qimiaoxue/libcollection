class MinPriorityQueue(object):

    def __init__(self, capacity=4):
        self.n = 0
        self.capacity = capacity
        self.keys = [None] * self.capacity

    def __len__(self):
        return self.n

    @property
    def min(self):
        """
        >>> q = MinPriorityQueue()
        >>> q.min
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> q.insert(5)
        >>> q.insert(4)
        >>> q.min
        4
        >>> q.insert(3)
        >>> q.min
        3
        """
        if len(self) == 0:
            raise IndexError('underflow')
        return self.keys[1]
    
    def pop(self):
        """
        >>> q = MinPriorityQueue()
        >>> q.pop()
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> q.insert(4)
        >>> q.insert(3)
        >>> q.insert(2)
        >>> q.insert(1)
        >>> q.pop()
        1
        >>> q.pop()
        2
        >>> q.capacity
        4
        """
        if len(self) == 0:
            raise IndexError('underflow')
        keys = self.keys
        res = keys[1]
        keys[1], keys[self.n] = keys[self.n], keys[1]
        keys[self.n] = None
        self.n -= 1
        self._sink(1)

        if self.n and self.n * 4 == self.capacity:
            self._resize(self.capacity//2)
        return res
        

    def insert(self, k):
        """
        >>> q = MinPriorityQueue()
        >>> q.insert(5)
        >>> q.min
        5
        >>> q.insert(4)
        >>> q.min
        4
        >>> q.insert(3)
        >>> q.insert(2)
        >>> q.min
        2
        """
        if self.n + 1 == self.capacity:
            self._resize(self.capacity*2)
        self.n += 1
        self.keys[self.n] = k
        self._swim(self.n)

    def _swim(self, n):
        """
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 2, 3, None, 1]
        >>> q._swim(4)
        >>> q.keys
        [None, 1, 2, None, 3]
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 3, 2, None, 1]
        >>> q._swim(4)
        >>> q.keys
        [None, 1, 3, None, 2]
        """
        keys = self.keys
        while n > 1 and keys[n//2] > keys[n]:
            keys[n], keys[n//2] = keys[n//2], keys[n]
            n = n//2

    def _sink(self, n):
        """
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 3, 2, 1]
        >>> q.n = 3
        >>> q._sink(1)
        >>> q.keys
        [None, 1, 2, 3]
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 3, 1, 2]
        >>> q.n = 3
        >>> q._sink(1)
        >>> q.keys
        [None, 1, 3, 2]
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

    def _resize(self, n):
        """
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 1, 2, 3]
        >>> q.n = 3
        >>> q._resize(6)
        >>> q.keys
        [None, 1, 2, 3, None, None]
        """
        q = MinPriorityQueue(capacity=n)
        for i in range(self.n+1):
            q.keys[i] = self.keys[i] 
        self.keys = q.keys
        self.capacity = n


if __name__ == '__main__':
    import doctest
    doctest.testmod()
