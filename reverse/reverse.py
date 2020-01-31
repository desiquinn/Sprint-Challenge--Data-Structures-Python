class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    # Create a previous variable and set it equal to None
    prev = None
    # Create a current pointer and set it equal to the head
    curr_node = self.head
    # Traverse through the list while curr is not equal to None
    while curr_node is not None:
      # create a temp variable to store what next is currently
      next_node = curr_node.get_next()
      # set what next points to in the current node to previous (this switches the pointer)
      # on the first node prev is None
      curr_node.set_next(prev)
      # update prev to now be what's stored in curr
      # on the first node curr is the Head
      prev = curr_node
      # set the head to the current node
      self.head = curr_node
      #update curr to what used to be the next node
      curr_node = next_node


"""
PLAN: 
prev = null  

while curr is not None
next = curr.next
curr.next = prev
prev = curr
curr = next
"""