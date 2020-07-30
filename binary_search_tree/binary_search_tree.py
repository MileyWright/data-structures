"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        cur_node = self.value
        # start at root and loop until 'cur_node' is None
        if value < cur_node: # if 'value' <= 'cur_node'
            if self.left is None: # if 'cur_node.left' is None
                self.left = BSTNode(value) # insert our value!
            else: # else
                self.left.insert(value) # go left (update 'cur_node' to be 'cur_node.left')
        elif value >= cur_node: # elif 'value' > 'cur_node'
            if self.right is None: # if 'cur_node.right' is None
                self.right = BSTNode(value) # insert our value!
            else: # else
                self.right.insert(value)# go right (update 'cur_node' to be 'cur_node.right')


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare target_value to cur_value
            # 1. == we return True
            # 2. < we go left
            # 3. > we go right
            # 4. if cant go left/right (not found, return False)
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None: # if the right side is None
            return self.value # then that is the highest value
        else: # otherwise keep going
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value) # call the function
        if self.left is not None: # if it's not none on the left side
            self.left.for_each(fn) # then CALL the function, and pass in fn
        if self.right is not None: # if it's not none on the right side
            self.right.for_each(fn) # then CALL the function, and pass in fn
    
    # Stretch Goals -------------------------
    def delete(self):
        pass
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
