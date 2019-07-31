class QuickFindUnionFind(object):

    def __init__(self, cnt):
        self.n = cnt
        self.parents = [i for i in range(cnt)]

    def __len__(self):
        """
        >>> uf = QuickFindUnionFind(10)
        >>> len(uf)
        10
        """
        return self.n

    def find(self, p):
        """
        >>> uf = QuickFindUnionFind(3)
        >>> uf.find(3)
        Traceback (most recent call last):
            ...
        IndexError: 3
        >>> uf.find(1)
        1
        >>> uf.find(2)
        2
        >>> uf.find(0)
        0
        """
        self._validate(p)
        return self.parents[p]

    def union(self, p, q):
        """
        >>> uf = QuickFindUnionFind(3)
        >>> uf.union(1, 2)
        >>> uf.parents
        [0, 1, 1]
        """
        self._validate(p)
        self._validate(q)
        p_parent = self.find(p)
        q_parent = self.find(q)
        if p_parent == q_parent:
            return
        for i in range(self.n):
            if self.parents[i] == q_parent:
                self.parents[i] = p_parent
        self.n -= 1
    
    def is_connected(self, p, q):
        """
        >>> uf = QuickFindUnionFind(3)
        >>> uf.is_connected(0, 1)
        False
        >>> uf.union(0, 1)
        >>> uf.is_connected(0, 1)
        True
        """
        self._validate(p)
        self._validate(q)
        return self.find(p) == self.find(q)

    def _validate(self, p):
        if not 0 <= p < self.n:
            raise IndexError(p)
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()
