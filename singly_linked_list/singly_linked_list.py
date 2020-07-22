class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
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
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
         # 1. create the Node from the value
        new_node = Node(value)
        # So, what do we do if tail is None?
        # What's the rule we want to set to indicate that the linked list is empty?
        # Would it be better to check the head?
        # Lets check them both: an empty linked list has an empty head and an empty tail
        if self.head is None and self.tail is None:
            # in a one-element linked list, what should head and tail be referring to?
            # have both head and tail referring to the single node
            self.head = new_node
            # set the new node to be the tail
            self.tail = new_node
        else:
            # These steps assume that the tail is already referring to a Node
            # 2. set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node
            self.tail = new_node
    
    def remove_head(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return
        # what if we only have a single element in the linked list?
        # both head ans tail are pointing at the same Node
        if not self.head.get_next():
            head = self.head
            # delete the linked lists head reference
            self.head = None
            # also delete the linked list tail reference
            self.tail = None
            return head.get_value()
        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val


    def remove_tail(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return
        # if we have a non-empty linked list

        # we have to start at the head and move down the linked list until we get to the node right before the tail

        # iterate over our linked list
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()
        # at this point, `current` is the node right before the tail
        # set the tail to be None
        val = self.tail.get_value()
        self.tail = None
        # move self.tail to the Node right before
        self.tail = current
        return 
        
    def contains(self, value):
        pass

    def get_max(self):
        # iterate through all elements
        cur_node = self.head
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()
