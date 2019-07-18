#from libcollection.lib_collection.node import Node
from lib_collection.node import Node


class LinkedStack(object):
    
    def __init__(self):
        self.n = 0
        self.head = Node(None)

    def __len__(self):
        return self.n

    def __str__(self):
        pass

    def __contains__(self):
        pass

    def __iter__(self):
        pass

    def push(self, i):
        """
        >>> stack = LikedStack()
        >>> stack.push('a')
        >>> len(stack)
        1
        >>> stack.push('b')
        >>> len(stack)
        2
        """
        n = Node(i)
        n.next = self.head.next
        self.head.next = n 
        self.n += 1

    def pop(self):
        pass

    def top(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
