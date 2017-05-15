class Node(object):


    def __init__(self,node):
        self.state = node
        self.visited = False
        self.nextNodes = []
        self.color = ""
        self.prevNode = 0

    def addChild(self,child):
        self.nextNodes.append(child)

    def getNeighbors(self):
        return self.nextNodes

    def isVisited(self):
        return self.visited

    def markVisited(self):
        self.visited = True

    def colorBlue(self):
        self.color = "Blue"

    def colorRed(self):
        self.color = "Red"

    def colorOpposite(self,parentColor):
        if(parentColor=="Red"):
            self.color = "Blue"
        else:
            self.color = "Red"

    def getColor(self):
        return self.color

    def getState(self):
        return self.state

    def assignPrev(self,pNode):
        self.prevNode = pNode

    def getPrev(self):
        return self.prevNode
