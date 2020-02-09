import sys
sys.path.append('../ring_buffer')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if not self.storage.head:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size

"""
Queue is FIFO like a line

"""