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
        return node.height if node else 0

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
        node = self.root
        while node:
            if key == node.key:
                return True
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self.find_min(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return self.balance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def next_key(self, key):
        node = self.root
        result = None
        while node:
            if node.key >= key:
                result = node.key
                node = node.left
            else:
                node = node.right
        return result

    def prev_key(self, key):
        node = self.root
        result = None
        while node:
            if node.key <= key:
                result = node.key
                node = node.right
            else:
                node = node.left
        return result

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
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return " ".join(result)

tree = AVLTree()
q = int(input())
for _ in range(q):
    parts = input().split()
    command = parts[0]
    if command == "add":
        tree.add(int(parts[1]))
    elif command == "del":
        tree.delete(int(parts[1]))
    elif command == "exists":
        print("YES" if tree.exists(int(parts[1])) else "NO")
    elif command == "next":
        result = tree.next_key(int(parts[1]))
        print(result if result is not None else "None")
    elif command == "prev":
        result = tree.prev_key(int(parts[1]))
        print(result if result is not None else "None")
    elif command == "root":
        if tree.root is None:
            print("Empty")
        else:
            print(tree.root.key)
    elif command == "height":
        print(tree.height())
    elif command == "print":
        print(tree.preorder())