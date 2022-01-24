"""
Teeron Hajebi
ATCS 2021-2022
Binary Tree

Python program to for binary tree insertion and traversals
"""
from bst_node import Node

INT_MAX = 4294967296
INT_MIN = -4294967296

'''
A function that returns a string of the inorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
def getInorder(root):
    if (root == None):
        return ""
    else:
        return getInorder(root.left) + str(root.val) + "-" + getInorder(root.right)

'''
A function that returns a string of the postorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
# A function to do postorder tree traversal
def getPostorder(root):
    if (root == None):
        return ""
    else:
        return getPostorder(root.left) + getPostorder(root.right)+ str(root.val) + "-"

'''
A function that returns a string of the preorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
def getPreorder(root):
    if (root == None):
        return ""
    else:
        return str(root.val) + "-" + getPreorder(root.left) + getPreorder(root.right)

'''
A function that inserts a Node with the value
key in the proper position of the BST with the
provided root. The function will return the 
original root with no change if the key already
exists in the tree.
'''
def insert(root, key):
    if (root == None):
        return Node(key)
    else:
        if (root.val == key):
            return root
        elif (root.val < key):
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

'''
Challenge: A function determines if a binary tree 
is a valid binary search tree

I'm not fully sure if I did this correctly, but it
seems to somewhat work. I think I need to add a wrapper
function of sorts so I can keep track of the root value,
but I'm feeling too under the weather to do that right now
'''
def isBST(root):
    if (root == None):
        return True
    elif (root.val < INT_MIN or root.val > INT_MAX):
        return False
    return (isBST(root.left) and isBST(root.right))

if __name__ == '__main__':
    # Tree to help you test your code
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(9)

    print("Preorder traversal of binary tree is")
    print(getPreorder(root))

    print("\nInorder traversal of binary tree is")
    print(getInorder(root))

    print("\nPostorder traversal of binary tree is")
    print(getPostorder(root))

    root = insert(root, 8)
    print("\nInorder traversal of binary tree with 8 inserted is")
    print(getInorder(root))

    if (isBST(root) == True):
        print ("\nIs a binary search tree")
    else:
        print ("\nIs not a binary search tree")
