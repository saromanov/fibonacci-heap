class Node:
    ''' implementation of node for fibonacci heap
    '''
    def __init__(self, value):
        self.left = None
        self.right = None
        self.child = None
        self.parent = None
        self.degree = 0
        self.mark = False
        self.value = value