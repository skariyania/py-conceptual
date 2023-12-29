"""tree implementation"""

class Node:
    """tree node"""
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    """tree data structure implementation"""
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        """insert values to tree node"""
        new_node = Node(value)
        # insert at root if tree root is None
        if self.root is not None:
            self.insert_recursive(current_node=self.root, new_node=new_node)
        else:
            self.root = new_node

    def insert_recursive(self, current_node: Node, new_node: Node):
        """recursive insert value to sub tree"""
        if current_node.left is None:
            current_node.left = new_node
        elif current_node.right is None:
            current_node.right = new_node
        else:
            self.insert_recursive(current_node.left, new_node)

    def inorder_traversal(self, node: Node):
        """travel tree node and print inorder"""
        if node:
            self.inorder_traversal(node.left)
            print(f"{node.value}", end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node: Node):
        """travel tree node and print pre order"""
        if node:
            print(f"{node.value}", end=" ")
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node: Node):
        """travel tree node and print post order"""
        if node:
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)
            print(f"{node.value}", end=" ")


t = BinaryTree()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
print("inorder:")
t.inorder_traversal(t.root)
print("")

print("preorder:")
t.preorder_traversal(t.root)
print("")

print("postorder:")
t.postorder_traversal(t.root)
print("")
