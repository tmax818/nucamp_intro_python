class Node:
    def __init__(self, value):
        self.value = value
        self.next = self.prev = self


class SL_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            return
