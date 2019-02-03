from node import Node

class FibonacciHeap:
    def __init__(self):
        '''initialization of the fibonacci heap
        '''
        self.head = None
        self._nodes = 0
    
    def insert(self, x):
        ''' inserting data to the heap
        creating of new node and attach it to exist heap
        '''
        self._nodes+=1
        if not self.head:
            self.head = Node(x)
            return
        new_node = Node(x)
        new_node.left = self.head
        new_node.right = self.head.right
        self.head.right = new_node
        if new_node.right:
            new_node.right.left = new_node
        else:
            new_node.right = self.head
            self.head.left = new_node
        
        if new_node.value < self.head.value:
            self.head = new_node
    
    def min(self):
        ''' return head of the heap with minimal value
        '''
        return self.head.value
