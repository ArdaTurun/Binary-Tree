class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._add_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._add_recursive(current.right, value)

    def find_level(self, value):
        return self._find_level_recursive(self.root, value, 0)

    def _find_level_recursive(self, node, value, level):
        if node is None:
            return -1
        if node.value == value:
            return level
        elif value < node.value:
            return self._find_level_recursive(node.left, value, level + 1)
        else:
            return self._find_level_recursive(node.right, value, level + 1)

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print_tree(node.right, level + 1, "R--- ")
        print("     " * level + prefix + str(node.value))
        print_tree(node.left, level + 1, "L--- ")

userNumbers = input("Please enter numbers with spaces between them: ")
numberList = list(map(int, userNumbers.split()))

tree = BST()
for sayi in numberList:
    tree.add(sayi)

print("\nGenerated Binary Tree:\n")
print_tree(tree.root)

whichLevel = int(input("\nWhich number's level do you want to know? "))
level = tree.find_level(whichLevel)

if level == -1:
    print(f"Number {whichLevel} was not found in the tree.")
else:
    print(f"The number {whichLevel} is located at the {level}. level of the tree.")
