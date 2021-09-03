class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self


node1 = DoubleNode(1)

print(node1.value, node1.next, node1.prev)
