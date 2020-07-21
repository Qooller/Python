# бинарное дерево


class BinaryTree:
    def __init__(self, rootObj):
        self.root = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self ,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self ,obj):
        self.root = obj

    def getRootVal(self):
        return self.root

    def __str__(self):
        output = str(self.root)
        if self.leftChild:
            output = '/'.join([self.leftChild.__str__(), output])
        else:
            output = '[' + output
        if self.rightChild:
            output = '\\'.join([output, self.rightChild.__str__()])
        else:
            output = output + ']'
        return output


r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
print("Root:", r.getRootVal())
print("Left child:", r.getLeftChild())
print("Tree:", r)
r.getLeftChild().insertLeft('d')
r.getLeftChild().insertRight('e')
print("Tree:", r)
r.getRightChild().insertLeft('f')
r.getRightChild().insertRight('g')
print("Tree:", r)

#      a
#    /   \
#   b     c
#  / \   / \
# d   e f   g

