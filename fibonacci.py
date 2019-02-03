from node import Node


class HeadIsNotExistException(Exception):
    pass

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
        
        if new_node.value > self.head.value:
            self.head = new_node
    
    def max(self):
        ''' return head of the heap with maximum value
        '''
        return self.head.value
    
    def degreewiseMerge(self):
        pass
    
    def removeMax(self):
        ''' remove max value from the head of heap
        and after this, rebuild of the heap
        '''
        tmp = self.head
        if not tmp:
            raise HeadIsNotExistException('head of the heap is not exist')
        degree = tmp.degree
        child = tmp.child
        right = None
        while degree > 0:
            right = child.right
            child.left.right = child.right
            child.right.left = child.left
            child.left = tmp
            child.right = tmp.right
            self.head = child
            child.left.right = child
            child.parent = None
            child = right
            degree-=1
    
        tmp.left.right = tmp.right
        tmp.right.left = tmp.left
        if tmp == tmp.right:
            self.head = None
        else:
            self.head = tmp.right
            self.degreewiseMerge()
        self._nodes-=1
        return tmp