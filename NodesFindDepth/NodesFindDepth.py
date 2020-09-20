#!/usr/bin/python3

class Node():
    def __init__(self, value):
        self.parent = None
        self.value = value
        self.children = {}
    def setParent(self, parent):
        self.parent = parent
    def getChild(self, childValue):
        return self.children[childValue]
    def addChild(self, childValue):
        self.children[childValue] = Node(childValue)
    def removeChild(self, child):
        self.children.remove(child)
    def removeParent(self, parent):
        self.parent = None
    def isLeaf(self):
        return True if ( len(self.children.keys()) <= 0 ) else False
    def findDeepest(self):
        self._findDeepest(self)
    def _findDeepest(self, head, depth=0, traced=""):
        if (traced == ""):
            traced = head.value
        breakRecursion = False
        if (head.isLeaf()):
            print("Leaf:", head.value, ", Path:", traced, ", Depth:", depth)
            breakRecursion = True
        if not breakRecursion:
            for childKey in head.children.keys():
                head._findDeepest(head.getChild(childKey), depth=depth+1, traced=traced+childKey)        
    def info(self):
        print(self.value, ':', self.children.keys())
        for childKey in self.children.keys():
            child = self.getChild(childKey)
            child.info()

def test():
    tree = Node('a')
    tree.addChild('b')
    tree.addChild('c')
    tree.getChild('b').addChild('d')
    tree.getChild('c').addChild('e')
    tree.getChild('c').addChild('f')
    tree.getChild('c').addChild('g')
    tree.getChild('c').getChild('f').addChild('h')
    tree.getChild('c').getChild('g').addChild('i')
    tree.getChild('c').getChild('g').getChild('i').addChild('j')

    tree.info()

    tree.findDeepest()

test()
