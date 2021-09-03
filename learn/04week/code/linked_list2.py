class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")

# print(head.value)
# print(head.next.value)
# print(head.next.next.value)


def iter_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next


iter_linked_list(head)

head.next.next.next = Node("$th Node")

iter_linked_list(head)
