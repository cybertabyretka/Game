from Utils.Settings.DataStructures.LinkedList import LinkedList


class Stack:
    def __init__(self, *elements: any) -> None:
        self.linked_list: LinkedList = LinkedList(*reversed(elements))

    def __str__(self) -> str:
        return self.linked_list.__str__()

    def push(self, element: any) -> None:
        self.linked_list.append_to_start(element)

    def pop(self) -> any:
        return self.linked_list.remove_first()

    def peek(self) -> any:
        return self.linked_list.at(0)

    def size(self) -> int:
        return self.linked_list.size()

    def clear(self):
        self.linked_list.clear()

    def is_empty(self):
        return self.linked_list.is_empty()