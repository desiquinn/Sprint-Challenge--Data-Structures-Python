import time
import sys
sys.path.append("../ring_buffer")
from doubly_linked_list import DoublyLinkedList

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    # Adds item to the back of the queue
    def enqueue(self, value):
        # increase size of queue by 1
        self.storage.add_to_tail(value)
        self.size += 1

    # Removes and returns item from the front of the queue
    def dequeue(self):
        if not self.storage.head:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    # Returns the length of the queue
    def len(self):
        return self.size

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

"""
The runtime for this solution before optimization is O(n^2)
where n is the number of names in name_1.  

We need to make the run time O(n log n), O(n), or O(log n)
"""