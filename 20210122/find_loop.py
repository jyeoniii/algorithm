# https://www.algoexpert.io/questions/Find%20Loop

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    s = set()
    while True:
        if head in s: return head
        s.add(head)
        head = head.next

