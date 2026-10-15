class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.nodes = {}

    def add(self, key):
        new_node = Node(key)
        self.nodes[key] = new_node
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    return
                current = current.right

    def left_rotate(self, x):
        a = self.nodes[x]
        b = a.right
        parent = a.parent
        a.right = b.left
        if b.left is not None:
            b.left.parent = a
        b.parent = parent
        if parent is None:
            self.root = b
        elif parent.left is a:
            parent.left = b
        else:
            parent.right = b
        b.left = a
        a.parent = b

    def right_rotate(self, x):
        a = self.nodes[x]
        b = a.left
        parent = a.parent
        a.left = b.right
        if b.right is not None:
            b.right.parent = a
        b.parent = parent
        if parent is None:
            self.root = b
        elif parent.left is a:
            parent.left = b
        else:
            parent.right = b
        b.right = a
        a.parent = b

    def preorder(self):
        result = []
        stack = []
        if self.root is not None:
            stack.append(self.root)
        while stack:
            node = stack.pop()
            result.append(str(node.key))
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return " ".join(result)

n = int(input())
keys = list(map(int, input().split()))
m = int(input())
tree = BinarySearchTree()
for key in keys:
    tree.add(key)
for _ in range(m):
    command, x = input().split()
    x = int(x)
    if command == "left":
        tree.left_rotate(x)
    else:
        tree.right_rotate(x)
    print(tree.preorder())