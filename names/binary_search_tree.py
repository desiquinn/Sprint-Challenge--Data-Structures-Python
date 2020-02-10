from queue import Queue
from stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(node.value)
        if self.right:
            self.right.in_order_print(self.right)

    def bft_print(self, node):
        q = Queue()
        q.enqueue(self)
        while q.len() > 0:
            temp = q.dequeue()
            if temp.left:
                q.enqueue(temp.left)
            if temp.right:
                q.enqueue(temp.right)
            print(temp.value)

    def dft_print(self, node):
        s = Stack()
        s.push(self)
        while s.len() > 0:
            temp = s.pop()
            print(temp.value)
            if temp.left:
                s.push(temp.left)
            if temp.right:
                s.push(temp.right)

    def pre_order_dft(self, node):
        print(node.value)
        if self.left:
            self.left.pre_order_dft(self.left)
        if self.right:
            self.right.pre_order_dft(self.right)

    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self.left)
        if self.right:
            self.right.post_order_dft(self.right)
        print(node.value)