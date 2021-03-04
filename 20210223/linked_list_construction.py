# https://www.algoexpert.io/questions/Linked%20List%20Construction

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.s = set()

    def setHead(self, node):
        if node in self.s: self.remove(node)
        if not self.head:
            self.head = self.tail = node
        else:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if node in self.s: self.remove(node)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert in self.s: self.remove(nodeToInsert)

        if node == self.head:
            self.head = nodeToInsert

        node_start = node_end = nodeToInsert
        while node_end.next: node_end = node_end.next

        prev_node = nodeToInsert.prev
        if prev_node:
            prev_node.after = node_start
        node.prev = node_end
        node_start.prev = prev_node
        node_end.after = node

        self.s.add(nodeToInsert)


    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert in self.s: self.remove(nodeToInsert)

        if node == self.tail:
            self.tail = nodeToInsert

        node_start = node_end = nodeToInsert
        while node_end.next: node_end = node_end.next

        after_node = node.after
        if after_node:
            after_node.prev = node_end
        node.after = node_start
        node_end.after = after_node
        node_start.prev = node

        self.s.add(nodeToInsert)

    def insertAtPosition(self, position, nodeToInsert):
        if nodeToInsert in self.s: self.remove(nodeToInsert)
        node, cnt = self.head, 1
        while cnt != position:
            node = node.next
            cnt += 1
        self.insertBefore(node, nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node:
            if node.value == value:
                next = node.next
                self.remove(node)
                node = next

    def remove(self, node):
        node_start = node_end = node
        while node_end.next: node_end = node_end.next

        if node_start == self.head: self.head = node_end.next
        if node_end == self.tail: self.tail = node_start.prev

        if node_start.prev:
            node_start.prev.next = node_end.next
        if node_end.next:
            node_end.next.prev = node_start.prev
        node_start.prev, node_end.next = None, None

    def containsNodeWithValue(self, value):
        node = self.head
        while node:
            if node.value == value: return True
            node = node.next
        return False