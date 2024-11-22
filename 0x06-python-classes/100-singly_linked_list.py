#!/usr/bin/python3
"""
linked list
"""


class Node:
    """
    Represents a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a Node with data and optional next_node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data, ensuring it is an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next_node, ensuring it is None or a Node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.
    """

    def __init__(self):
        """
        Initialize the list with a head node set to None.
        """
        self.__head = None

    def __str__(self):
        """
        Print the entire list, one node's data per line.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Insert a new Node with value in the correct sorted position.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
