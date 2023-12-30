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

    def levelorder_traversal(self, node: Node):
        """travel binary tree with BFS approach"""
        if not node:
            return

        queue = []
        queue.append(node)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.value, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    def reversed_levelorder_traversal(self, node: Node):
        """travel binary tree with BFS approach in reverse order"""
        if not node:
            return []
        result = []
        queue = [node]
        while queue:
            current = queue.pop(0)
            result.insert(0, current.value)
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        return result            


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

print("levelorder:")
t.levelorder_traversal(t.root)
print("")


print("reversed levelorder:")
result = t.reversed_levelorder_traversal(t.root)
print(*result)
print("")