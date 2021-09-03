class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


node1 = DoubleNode("first")
node2 = DoubleNode("second")
node3 = DoubleNode("third")

# # first link
# node1.next = node2
# node2.prev = node1

# # second link
# node2.next = node3
# node3.prev = node2

# print('node1', id(node1), id(node1.prev), id(node1.next))
# print('node2', id(node2), id(node2.prev), id(node2.next))
# print('node3', id(node3), id(node3.prev), id(node3.next))


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # def append(self, value):
    #     new_node = DoubleNode(value)

    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node
    #         return

    #     new_node.prev = self.tail
    #     self.tail.next = new_node
    #     self.tail = new_node

    def append(self, value):
        new_node = DoubleNode(value)
        self.tail = new_node

        if self.head is None:
            self.head = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node


dllist = DoublyLinkedList()
dllist.append("First Node")
