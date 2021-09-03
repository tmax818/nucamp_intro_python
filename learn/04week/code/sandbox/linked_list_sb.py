class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = self.head.next

        current_node.next = Node(value)

    def traverse(self):
        current_node = self.head
        while current_node.next is not None:
            print(current_node.value)
            current_node = current_node.next
        print(current_node.value)


llist = LinkedList()
llist.append("first")
llist.append("second")
