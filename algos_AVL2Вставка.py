class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.right) - self.get_height(node.left)

    def update_height(self, node):
        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

    def rotate_left(self, a):
        b = a.right
        a.right = b.left
        b.left = a
        self.update_height(a)
        self.update_height(b)
        return b

    def rotate_right(self, a):
        b = a.left
        a.left = b.right
        b.right = a
        self.update_height(a)
        self.update_height(b)
        return b

    def balance(self, node):
        if node is None:
            return None
        self.update_height(node)
        bf = self.balance_factor(node)
        if bf == 2:
            if self.balance_factor(node.right) < 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        if bf == -2:
            if self.balance_factor(node.left) > 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        return node

    def add(self, key):
        self.root = self._add(self.root, key)

    def _add(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._add(node.left, key)
        elif key > node.key:
            node.right = self._add(node.right, key)
        else:
            return node
        return self.balance(node)

    def exists(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def height(self):
        return self.get_height(self.root)

    def preorder(self):
        if self.root is None:
            return "Empty"
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            result.append(str(node.key))
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return " ".join(result)

tree = AVLTree()
q = int(input())
for _ in range(q):
    command = input().split()
    operation = command[0]
    if operation == "add":
        tree.add(int(command[1]))
    elif operation == "exists":
        print("YES" if tree.exists(int(command[1])) else "NO")
    elif operation == "root":
        if tree.root is None:
            print("Empty")
        else:
            print(tree.root.key)
    elif operation == "height":
        print(tree.height())
    elif operation == "print":
        print(tree.preorder())