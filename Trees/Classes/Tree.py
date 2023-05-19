class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = "Red"
class RedBlack:
    def __int__(self,value):
        self.root = Node(value)
        self.root.color= "Black"
def whichChild(node):
    if node.value <= node.parent.value:
        return "left"
    else:
        return "right"
def rotateCase(node):

def redUncleCase(node):
    if "Red" in node.parent.color:
        child = whichChild(node.parent)
        if "left" in child and "Red" in node.parent.parent.right.color:
            node.parent.parent.right.color = "Black"
            node.parent.parent.color = "Red"
            node.parent.color = "Black"
            redUncleCase(node.parent.parent)
        elif "right" in child and "Red" in node.parent.parent.left.color:
            node.parent.parent.left.color = "Black"
            node.parent.parent.color = "Red"
            node.parent.color = "Black"
            redUncleCase(node.parent.parent)
        else:
            rotateCase(node)
    else:
        return
def insertTree(node,value):
    if node == None:
        newNode = node(value,None,None,None,"Red")
        return newNode
    if value <= node.value:
        node.left = insertTree(node.left,value)
        node.left.parent = node
    else:
        node .right = insertTree(node.right,value)
        node.right.parent = node