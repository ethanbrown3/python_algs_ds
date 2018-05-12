#!/usr/bin/python

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    def __str__(self):
        return ('value: {0} left: {1} right: {2}').format(self.value, self.left, self.right)

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.value):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.value):
            return node
        elif(val < node.value and node.left != None):
            return self._find(val, node.left)
        elif(val > node.value and node.right != None):
            return self._find(val, node.right)



    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left)
            print str(node.value) + ' '
            self._printTree(node.right)

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print tree.find(3).value
print tree.find(1)
tree.add(1)
print tree.find(1)
tree.deleteTree()
tree.printTree()
