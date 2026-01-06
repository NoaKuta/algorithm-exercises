import random
from typing import Optional 

class Node:
    def __init__(self, value):
        self.value = value
        self.left : Optional[Node] = None
        self.right : Optional[Node] = None
        self.parent : Optional[Node] = None

    def print(self):
        if self.left:
            self.left.print()
        print(self.value, ", ", sep="", end="")
        if self.right:
            self.right.print()

    def print_indented(self, indent="", side=""):
        if self.right:
            if side == "left" or side=="":
                next_indent = indent+"   ┃"
            else:
                next_indent = indent[:-1]+"    ┃"
            self.right.print_indented(next_indent, side="right")

        current_indent=""
        if side=="left":
            current_indent=indent[:-1]+"┗"
        elif side=="right":
            current_indent=indent[:-1]+"┏"
        print(F"{current_indent}{self.value}")

        if self.left:
            if side == "right" or side=="":
                next_indent = indent+"   ┃"
            else:
                next_indent = indent[:-1]+"    ┃"
            self.left.print_indented(next_indent, side="left")

    def depth(self) -> int:
        depth = 0
        if self.left:
            depth = max(depth, self.left.depth())
        if self.right:
            depth = max(depth, self.right.depth())
        return depth + 1

    def min(self) -> 'Node':
        if self.left:
            return self.left.min()
        return self

    def max(self) -> 'Node':
        if self.right:
            return self.right.max()
        return self

    def successor(self) -> Optional['Node']:
        if self.right:
            return self.right.min()
        x = self
        y = self.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y
        
    def predecessor(self) -> Optional['Node']:
        if self.left:
            return self.left.max()
        x = self
        y = self.parent
        while y and x == y.left:
            x = y
            y = y.parent
        return y

    def get_number_of_nodes(self) -> int:
        number_of_nodes : int = 1
        if self.left:
            number_of_nodes += self.left.get_number_of_nodes()
        if self.right:
            number_of_nodes += self.right.get_number_of_nodes()
        return number_of_nodes
    
    def get_k_node(self, k : int) -> 'Node':
        left_count = 0
        if self.left:
            left_count = self.left.get_number_of_nodes()

        if left_count == k-1:
            return self
        if left_count < k-1:
            assert(self.right)
            return self.right.get_k_node(k - left_count - 1)
        else:
            assert(self.left)
            return self.left.get_k_node(k)

class Tree:
    def __init__(self, key=lambda x: x):
        self.root = None
        self.key = key 

    def insert(self, value):
        """הכנסת איבר חדש תוך שימוש בפונקציית המפתח (key)"""
        val_key = self.key(value)
        x = self.root
        y : Optional[Node] = None
        
        while x is not None:
            node_key = self.key(x.value)
            if val_key == node_key:
                return # הערך (או המפתח) כבר קיים בעץ
            
            y = x
            if val_key > node_key:
                x = x.right
            else:
                x = x.left
        
        new_node = Node(value)
        if y is None:
            self.root = new_node
        else:
            if val_key > self.key(y.value):
                y.right = new_node
            else:
                y.left = new_node
            new_node.parent = y

    def search_or_insert(self, value) -> Node:
        """חיפוש איבר לפי מפתח, ואם אינו קיים - הכנסתו"""
        val_key = self.key(value)
        x = self.root
        y : Optional[Node] = None
        
        while x is not None:
            node_key = self.key(x.value)
            if val_key == node_key:
                return x
            y = x
            if val_key > node_key:
                x = x.right
            else:
                x = x.left
        
        new_node = Node(value)
        if y is None:
            self.root = new_node
        elif val_key > self.key(y.value):
            y.right = new_node
        else:
            y.left = new_node
        new_node.parent = y
        return new_node

    def get_number_of_nodes(self):
        return self.root.get_number_of_nodes() if self.root else 0

    def print_indented(self):
        if self.root:
            self.root.print_indented()

    def median(self) -> Optional[Node]:
        if self.root:
            number_of_nodes = self.get_number_of_nodes()
            return self.root.get_k_node(int(number_of_nodes / 2) + 1)
        return None

# דוגמה להרצה: מיון מילים לפי אורכן
def main():
    # יוצרים עץ שהמפתח שלו הוא אורך המחרוזת
    tree = Tree(key=len)
    
    words = ["banana", "apple", "hi", "a", "watermelon"]
    for word in words:
        tree.insert(word)

    print("Tree structure (sorted by length):")
    tree.print_indented()
    
    median_node = tree.median()
    if median_node:
        print(f"\nMedian word (by length): {median_node.value}")

if __name__ == '__main__':
    main()