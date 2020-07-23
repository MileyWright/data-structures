"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from singly_linked_list import LinkedList

# Array: 
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)


#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size = len(self.storage)
#             return self.storage.pop()

# Linked List:
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_head(value)
        self.size = self.size + 1 #once you "append", you have to update the count

    def pop(self):
        if len(self) == 0:
            return None
        else:
            self.size = self.size - 1 
            return self.storage.remove_head()