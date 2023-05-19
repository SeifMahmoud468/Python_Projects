class Node():
    def __init__(self, val):
        self.val = val                                   # Value of Node
        self.parent = None                               # Parent of Node
        self.left = None                                 # Left Child of Node
        self.right = None                                # Right Child of Node
        self.color = 1                                   # 1 for Red


class RBTree():
    def __init__(self):
        self.NULL = Node('0')
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL
    # Insert New Node

    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.left = self.NULL                            # Set left node Null
        node.right = self.NULL                           # Set right node Null

        temp_parent = None
        temp_node = self.root

        while temp_node != self.NULL:                           # Find position for new node
            temp_parent = temp_node
            if node.val < temp_node.val:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right
        node.parent = temp_parent                                  # Set parent of Node as Temp_parent

        if temp_parent == None:                                   # If parent i.e, is none then it is root node
            self.root = node
        elif node.val < temp_parent.val:                          # Check if it is right Node or Left Node by checking the value
            temp_parent.left = node
        else:
            temp_parent.right = node

        if node.parent == None:                         # Root node is always Black
            node.color = 0
            return
        if node.parent.parent == None:                  # If parent of node is Root Node
            return

        self.fixInsert ( node )                          # Else call for Fix Up
    # Code for left rotate
    def Rotate_left(self,x):
        y = x.right                                      # Y = Right child of x
        x.right = y.left                                 # Change right child of x to left child of y
        if y.left != self.NULL:
            y.left.parent = x
        y.parent = x.parent                              # Change parent of y as parent of x
        if x.parent == None:                            # If parent of x == None ie. root node
            self.root = y                                # Set y as root
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    # Code for right rotate
    def Rotate_right(self,x):
        y = x.left                                       # Y = Left child of x
        x.left = y.right                                 # Change left child of x to right child of y
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent                              # Change parent of y as parent of x
        if x.parent == None :                            # If x is root node
            self.root = y                                # Set y as root
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y
    # Function of fixing
    def fixInsert(self, k):
        while k.parent.color == 1:                        # While parent is red
            if k.parent == k.parent.parent.right:         # if parent is right child of its parent
                u = k.parent.parent.left                  # Left child of grandparent
                if u.color == 1:                          # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set both children of grandparent node as black
                    k.parent.color = 0
                    k.parent.parent.color = 1             # Set grandparent node as Red
                    k = k.parent.parent                   # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.parent.left:                # If k is left child of it's parent
                        k = k.parent
                        self.Rotate_right(k)              # Call for right rotation
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.Rotate_left(k.parent.parent)
            else:                                         # if parent is left child of its parent
                u = k.parent.parent.right                 # Right child of grandparent
                if u.color == 1:                          # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set color of childs as black
                    k.parent.color = 0
                    k.parent.parent.color = 1             # set color of grandparent as Red
                    k = k.parent.parent                   # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.parent.right:               # if k is right child of its parent
                        k = k.parent
                        self.Rotate_left(k)  # Call left rotate on parent of k
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.Rotate_right(k.parent.parent)  # Call right rotate on grandparent
            if k == self.root:                            # If k reaches root then break
                break
        self.root.color = 0                               # Set color of root as black
    # Function return the size
    def __sizeCall(self,node):
        if node is self.NULL:
            return 0
        return self.__sizeCall(node.right)+self.__sizeCall(node.left)+1
    # Function to call the size
    def size(self):
        return self.__sizeCall(self.root)
    # Function of the height
    def __heightCall(self, node):
        if node is self.NULL:
            return 0
        return max(self.__heightCall(node.left), self.__heightCall(node.right)) + 1
    # Function to call the height
    def height(self):
        return self.__heightCall(self.root)
    # Function to search in the tree
    def __searchCall(self,node,value):
        if str(node.val).casefold() == value.casefold():
            return True
        elif node == self.NULL:
            return False
        if value < node.val:
            return self.__searchCall(node.left, value)
        else:
            return self.__searchCall(node.right, value)
    # Function to call search
    def search(self,value):
        return self.__searchCall(self.root,value)
def loading_Dic(Tree):
    file = open("E:\SEIF\My Projects\Python\RedBlack\EN-US-Dictionary.txt")
    for line in file:
        line = line.strip('\n')
        Tree.insertNode(line)
    file.close()
if __name__ == "__main__":
    Tree = RBTree()
    while True:
        print("1-Search\n2-Insert word\n3-Print Tree Size\n4-Print Tree Height\n5-Load EN-US-Dictionary\n6-Exit")
        try:
            x = int(input())
        except:
            print("Invaled choice, try again\n")
            continue
        if x in range(1 , 7):
            if x == 1:
                print("\nEnter the Word: ")
                x = input()
                if Tree.search(x):
                    print("Word is Found\n")
                else:
                    print("Word is not Found\n")
            elif x == 2:
                print("\nEnter the Word: ")
                x = input()
                Tree.insertNode(x)
                print("Word is inserted\nTree size: {Size}\nTree height: {Height} \n".format(Size=Tree.size(),
                                                                                             Height=Tree.height()))
            elif x == 3:
                print("\nTree Size: {size}\n".format(size=Tree.size()))
            elif x == 4:
                print("\nTree Height: {height}\n".format(height=Tree.height()))
            elif x == 5:
                loading_Dic(Tree)
                print("\nDictionary is loaded\n")
            else:
                break
        else:
            print("Invaled choice, try again\n")
            continue