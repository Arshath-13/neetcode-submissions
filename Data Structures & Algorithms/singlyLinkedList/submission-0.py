from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head

        while curr and index > 0:
            curr = curr.next
            index -= 1

        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = newNode

    def remove(self, index: int) -> bool:

        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        curr = self.head

        while curr and index > 1:
            curr = curr.next
            index -= 1

        if curr is None or curr.next is None:
            return False

        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        result = []
        curr = self.head

        while curr:
            result.append(curr.val)
            curr = curr.next

        return result