class Node:
    """Represents an individual node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Manages the linked list structure and recursive operations."""
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        """Inserts a new node at the front of the list in O(1) time."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Inserts a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # --- Recursive Sum ---
    def recursive_sum(self):
        """Public method to sum all node values using recursion."""
        return self._sum_recursive(self.head)

    def _sum_recursive(self, node):
        if node is None:
            return 0
        return node.data + self._sum_recursive(node.next)

    # --- Recursive Search ---
    def recursive_search(self, target):
        """Public method to search for a given ID using recursion."""
        return self._search_recursive(self.head, target)

    def _search_recursive(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self._search_recursive(node.next, target)

    # --- Recursive Reverse ---
    def recursive_reverse(self):
        """Public method to reverse the list in-place using recursion."""
        self.head = self._reverse_recursive(self.head, None)

    def _reverse_recursive(self, current, prev):
        if current is None:
            return prev
        next_node = current.next
        current.next = prev
        return self._reverse_recursive(next_node, current)

    # --- Utility Display Method ---
    def display(self):
        """Prints the list in a user-friendly format."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "List is empty")