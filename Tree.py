"""
Unit 4 Discussion: Binary Search Trees

This program demonstrates how a Binary Search Tree (BST) works
using 2026 Las Vegas Raiders receiving-yard statistics.

The tree stores each player's receiving yards as a numerical value.
Smaller values are placed on the left, and larger values are
placed on the right.
"""


# Node class represents each individual node in the BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Binary Search Tree class
class BST:
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Recursively insert values into the correct position
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)

        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

        # Duplicate values are ignored

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Recursively search for a value
    def _search_recursive(self, node, value):
        if node is None:
            return False

        if value == node.value:
            return True

        elif value < node.value:
            return self._search_recursive(node.left, value)

        else:
            return self._search_recursive(node.right, value)

    # Return values using in-order traversal
    def inorder(self):
        values = []
        self._inorder_recursive(self.root, values)
        return values

    # Recursively perform in-order traversal
    def _inorder_recursive(self, node, values):
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


# Main program
def main():

    # 2026 Las Vegas Raiders receiving-yard statistics
    raiders_players = {
        658: "Brock Bowers",
        529: "Tre Tucker",
        388: "Michael Mayer",
        371: "Ashton Jeanty",
        122: "Jalen Nailor",
        112: "Cody White",
        57: "Jack Bech"
    }

    # Create a Binary Search Tree
    raiders_tree = BST()

    # Receiving-yard values inserted into the tree
    receiving_yards = [
        371,
        122,
        529,
        57,
        388,
        112,
        658
    ]

    # Insert each player's receiving yards
    for yards in receiving_yards:
        raiders_tree.insert(yards)

    # Display program title
    print("==========================================")
    print("          LAS VEGAS RAIDERS")
    print("          2026 RECEIVING STATS")
    print("==========================================")

    # Display player statistics in ascending order
    print("\nPlayer Receiving Yards:")
    print("------------------------------------------")

    for yards in raiders_tree.inorder():
        player = raiders_players[yards]
        print(f"{player}: {yards} yards")

    # Display in-order traversal
    print("\nIn-Order Traversal:")
    print(raiders_tree.inorder())

    # Test searches for existing values
    print("\nSearch Tests:")
    print("------------------------------------------")

    print(
        "Search for Brock Bowers (658):",
        raiders_tree.search(658)
    )

    print(
        "Search for Tre Tucker (529):",
        raiders_tree.search(529)
    )

    # Test searches for values that do not exist
    print(
        "Search for 500 yards:",
        raiders_tree.search(500)
    )

    print(
        "Search for 1000 yards:",
        raiders_tree.search(1000)
    )

    # Edge case: searching an empty tree
    print("\nEdge Case Tests:")
    print("------------------------------------------")

    empty_tree = BST()

    print(
        "Search in an empty tree:",
        empty_tree.search(100)
    )

    print(
        "In-order traversal of an empty tree:",
        empty_tree.inorder()
    )

    # Edge case: inserting a duplicate value
    raiders_tree.insert(658)

    print(
        "Tree after inserting duplicate 658:",
        raiders_tree.inorder()
    )

    # Edge case: creating a tree with only one node
    single_tree = BST()
    single_tree.insert(658)

    print(
        "Single-node tree:",
        single_tree.inorder()
    )

    # Final message
    print("\n==========================================")
    print("              GO RAIDERS!")
    print("==========================================")


# Run the main program
if __name__ == "__main__":
    main()
