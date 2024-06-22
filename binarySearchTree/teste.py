from Node import Node
from BinarySearchTree import BST  # Assuming your BST class is defined in a module named BST

# Create an instance of the BST
bst = BST()

# Insert some elements
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# Test search functionality
print("Searching for 20:", bst.search(20))  # Expected output: True
print("Searching for 90:", bst.search(90))  # Expected output: False

# Test remove functionality
print("\nRemoving 20:")
bst.remove(20)
bst.in_order_traversal()  # Expected output after removal: 30, 40, 50, 60, 70, 80

print("\nRemoving 30:")
bst.remove(30)
bst.in_order_traversal()  # Expected output after removal: 40, 50, 60, 70, 80

# Test traversal methods
print("\nIn-order traversal:")
bst.in_order_traversal()  # Expected output: 40, 50, 60, 70, 80

print("\nPre-order traversal:")
bst.pre_order_traversal()  # Expected output: 50, 40, 70, 60, 80

print("\nPost-order traversal:")
bst.post_order_traversal()  # Expected output: 40, 60, 80, 70, 50

# Test finding minimum and maximum values
print("\nMinimum value in the tree:", bst.find_min().data)  # Expected output: 40
print("Maximum value in the tree:", bst.find_max().data)  # Expected output: 80

# Test finding height of the tree
print("\nHeight of the tree:", bst.find_height())  # Expected output: 2

