from Node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if (self.root == None):
            self.root = Node(data)
        else:
            self.__insert_recursive(self.root, data)

    def __insert_recursive(self, node: Node, data):
        if(data <= node.data):
            if(node.left == None):
                node.left = Node(data)
            else:
                #continuar a busca
                self.__insert_recursive(node.left, data)
        if(data > node.data):
            if(node.right == None):
                node.right = Node(data)
            else:
                self.__insert_recursive(node.right, data)
    
    def search(self, data):
        if(self.root == None):
            return False
        else:
           return self.__search_recursive(self.root, data)
    
    def __search_recursive(self, node: Node, data):
        if(data == node.data):
            return True
        elif(data < node.data):
            if(node.left == None):
                return False
            else:
               return self.__search_recursive(node.left, data)
        else:
            if(node.right == None):
                return False
            else:
                return self.__search_recursive(node.right, data)

    def remove(self, data):
        if self.root is None:
            return None
        else:
            self.root = self.__remove_recursive(self.root, data)
        
    def __remove_recursive(self, node: Node, data):
        if node is None:
            return None

        if (data < node.data):
            node.left = self.__remove_recursive(node.left, data)
        elif (data > node.data):
            node.right = self.__remove_recursive(node.right, data)
        else:
            # Case 1: No child or one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Case 2: Two children
                # Find the maximum value in the left subtree
                temp = self.__max_left_value(node.left)
                node.data = temp.data
                # Remove the node that originally contained the max value
                node.left = self.__remove_recursive(node.left, temp.data)

        return node

    def __max_left_value(self, node: Node):
        current = node
        while current.right is not None:
            current = current.right
        return current
    
    ### Traversals
    def in_order_traversal(self):
        self.__in_order_traversal_recursive(self.root)
    def __in_order_traversal_recursive(self, node: Node):
        if node is not None:
            self.__in_order_traversal_recursive(node.left)
            print(node.data)
            self.__in_order_traversal_recursive(node.right)

    def pre_order_traversal(self):
        self.__pre_order_traversal_recursive(self.root)
    def __pre_order_traversal_recursive(self, node: Node):
        if node is not None:
            print(node.data)
            self.__pre_order_traversal_recursive(node.left)
            self.__pre_order_traversal_recursive(node.right)

    def post_order_traversal(self):
        self.__post_order_traversal_recursive(self.root)
    def __post_order_traversal_recursive(self, node: Node):
        if node is not None:
            self.__post_order_traversal_recursive(node.left)
            self.__post_order_traversal_recursive(node.right)
            print(node.data)
    
    def find_min(self):
        if(self.root == None):
            return None
        current = self.root
        while(current.left != None):
            current = current.left
        return current
    
    def find_max(self):
        if(self.root == None):
            return None
        current = self.root
        while(current.right != None):
            current = current.right
        return current
    
    def find_height(self):
        return self.__find_height_recursive(self.root)
    def __find_height_recursive(self, node:Node):
        if node is None:
            return -1
        else:
            left_height = self.__find_height_recursive(node.left)
            right_height = self.__find_height_recursive(node.right)
            return max(right_height, left_height) + 1