from doubly_linked_list import DoublyLinkedList

"""
Understand Notes:
- Useful for asyncronous processes
- FIFO (which means Queue)
- Two points to items (can we use head and tail of DLL?)
- when queue length is 0, it's empty
- when queue length is the number of elements, it's full
- add data to head
- read(or get) from tail
- since we're adding to the head, the newest data is at the head
- since we are removing from the tail, the oldest data is at the tail
- when the head and tail are the same then what?
- current will always point to the lastest (newest data = head)
- if full the head pointer points to the newest and the tail pointer
points to the oldest.
- to overwrite we need to come head pointer to the tail, tail pointer 
to next, overwrite the value of head, set current to next
newest - end - head - current
oldest - start - tail
switching logic...
"""

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            # print(f"empty append current: {self.current.value}")
            # print(f"head: {self.storage.head.value}")
        elif self.storage.length == self.capacity:
            # self.storage.tail.next = self.storage.head - can't do this because it cause and infinate loop
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
            self.current.value = item
            # print(f"at capacity current: {self.current.value}")
            # print(f"head: {self.storage.head.value}")
        #else add new item to tail
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            # print(f"space was avail current: {self.current.value}")
            # print(f"head: {self.storage.head.value}")

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head
        while current_node != None:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
            # print(list_buffer_contents)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
