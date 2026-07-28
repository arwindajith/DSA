# in this file we implement the linked_list

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class linkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def append(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
        elif self.head.next == None:
            self.head.next = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def delete(self, value):
        if self.is_empty():
            return "list is empty"
        elif self.head.next == None:
            if self.head.value == value:
                self.head.value == None
            else:
                return "value does not exist"
        else:
            temp = self.head
            prev = temp

            while temp.next is not None and temp.value != value:
                prev = temp
                temp = temp.next

            if temp.value == value and temp == self.head:
                self.head = self.head.next

            elif temp.value == value:
                prev.next = temp.next
            else:
                return "not exist"

    def display(self):
        if self.is_empty():
            print(None)
        elif self.head.next is None:
            print(f"{self.head.value} -> {None}")
        else:
            temp = self.head
            while temp.next is not None:
                print(temp.value, end=" ")
                temp = temp.next
            print(temp.value)


ll = linkedList()
ll.append(1)
ll.append(5)
ll.append(3)
ll.append(7)
ll.append(9)
print(ll.delete(3))
print(ll.display())
