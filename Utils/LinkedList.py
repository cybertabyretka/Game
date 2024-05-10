class Node:
    def __init__(self, val: any = None) -> None:
        self.val: any = val
        self.next: Node | None = None


class LinkedList:
    def __init__(self, *elements: any) -> None:
        self.head: Node = Node()
        self.len: int = 0
        self.tail: Node = Node()
        for element in elements:
            self.append_to_end(element)

    def __str__(self) -> str:
        current_node = self.head
        out = ''
        while current_node:
            out += f'{current_node.val}->'
            current_node = current_node.next
        return out[:-2]

    def __convert_index_to_positive(self, pos: int) -> int:
        return pos + self.len

    def __append_in_empty_list(self, new_node: Node) -> None:
        self.head = new_node
        self.len += 1

    def size(self) -> int:
        return self.len

    def remove(self, pos: int = -1) -> any:
        if pos < 0:
            pos = self.__convert_index_to_positive(pos)
        if pos == 0:
            return self.remove_first()
        if pos == (self.len - 1):
            return self.remove_last()
        if pos >= self.len or pos < 0:
            raise Exception('Index is not correct')
        current_index = 0
        current_node = self.head
        while current_index != (pos - 1):
            current_node = current_node.next
            current_index += 1
        value_to_remove = current_node.next.val
        current_node.next = current_node.next.next
        self.len -= 1
        return value_to_remove

    def append_to_end(self, element: any) -> None:
        new_node = Node(element)
        if self.head.val is None:
            self.__append_in_empty_list(new_node)
            return
        if self.tail.val is None:
            self.head.next = new_node
            self.tail = new_node
            self.len += 1
            return
        self.tail.next = new_node
        self.tail = self.tail.next
        self.len += 1

    def append_to_start(self, element: any) -> None:
        new_node = Node(element)
        if self.head.val is None:
            self.__append_in_empty_list(new_node)
            return
        new_node.next = self.head
        self.head = new_node
        if self.len == 1:
            self.tail = new_node.next
        self.len += 1

    def append(self, element: any, pos: int | None = None) -> None:
        new_node = Node(element)
        if pos is None:
            self.append_to_end(element)
            return
        if pos < 0:
            pos = self.__convert_index_to_positive(pos)
        if pos == 0:
            self.append_to_start(element)
            return
        if pos >= self.len or pos < 0:
            raise Exception('Index is not correct')
        current_index = 0
        current_node = self.head
        while current_index != pos - 1:
            current_node = current_node.next
            current_index += 1
        next_node = current_node.next
        current_node.next = new_node
        new_node.next = next_node
        self.len += 1

    def remove_last(self) -> any:
        if self.head.val is None:
            return None
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        value_to_remove = current_node.next.val
        current_node.next = None
        self.tail = current_node
        self.len -= 1
        return value_to_remove

    def remove_first(self) -> any:
        if self.head.val is None:
            return None
        value_to_remove = self.head.val
        if self.head.next is None:
            self.head = Node()
            self.len -= 1
            return value_to_remove
        self.head = self.head.next
        if self.len == 2:
            self.tail = Node()
        self.len -= 1
        return value_to_remove

    def at(self, pos: int) -> any:
        if pos == 0:
            return self.head.val
        current_index = 0
        current_node = self.head
        if pos < 0:
            pos = self.__convert_index_to_positive(pos)
        if pos >= self.len or pos < 0:
            raise Exception('Index is not correct')
        while current_index != pos:
            current_node = current_node.next
            current_index += 1
        return current_node.val

    def remove_from_end_at(self, pos: int) -> any:
        if pos < 0:
            pos = abs(pos) - 1
        else:
            pos = self.len - pos - 1
            if pos < 0:
                raise Exception('Index is not correct')
        self.remove(pos)

    def reverse(self, __current_node: Node | None = None, __current_index: int = 0) -> None:
        if self.len <= 1:
            return
        if __current_index == 0:
            __current_node = self.head
            self.tail, self.head = self.head, self.tail
        else:
            __current_node = __current_node.next
        if __current_index != (self.len - 2):
            __current_index += 1
            self.reverse(__current_node, __current_index)
        __current_node.next.next = __current_node
        __current_node.next = None

    def clear(self):
        self.tail.next = self.tail.val = self.head.next = self.head.val = None
        self.len = 0

    def is_empty(self):
        return self.len == 0