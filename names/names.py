import time
from binary_search_tree import BinarySearchTree as bst



start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

"""
# Orginal Solution
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""

"""
My Solution
Time Complexity: 
"""
# Loop through first set of names 
for name in names_1:
    # add it to the binary search tree
    bst.insert(name)

# Loop through second set of names
for name in names_2:
    # if the bst contains the name
    if bst.contains(name):
        # add the name to duplicates list
        duplicates.append(name)
    # otherwise
    else:
        # add them to the binary search tree
        bst.insert(name)


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