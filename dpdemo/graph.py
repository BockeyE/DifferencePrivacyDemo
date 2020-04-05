class Edge(object):
    def __init__(self):
        self.x = -1
        self.next = None


class Vert(object):

    def __init__(self):
        self.name = ''
        self.degree = 0


class Graph(object):

    def __init__(self, size):
        self.n = size
        self.m = 0
        self.nodes = []
        self.nodeLink = []
        self.nodeLinkTail = []
        for i in range(0, size):
            self.nodeLink[i] = None
            self.nodeLinkTail[i] = None

    def addLink(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            newedge = Edge()
            newedge.x = j
            if self.nodeLink[i] is None:
                self.nodeLink[i] = newedge
                self.nodeLinkTail[i] = newedge
                self.nodes[i].degree = 1
            else:
                self.nodeLinkTail[i].next = newedge
                self.nodeLink[i] = newedge
                self.nodes[i].degree = self.nodes[i].degree + 1
            self.m = self.m + 1
            return True
        else:
            return False

    def doesLinkExist(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            curr = self.nodeLink[i];
            while not (curr is None):
                if curr.x == j:
                    return True
                curr = curr.next
        return False

    def getDegree(self, i):
        if 0 <= i < self.n:
            return self.nodes[i].degree
        else:
            return -1

    def getName(self, i):
        if 0 <= i < self.n:
            return self.nodes[i].name
        else:
            return ''

    def getNeighborList(self, i):
        if 0 <= i < self.n:
            return self.nodeLink[i]
        else:
            return None

    def numLinks(self):
        return self.m

    def numNodes(self):
        return self.n

    def setName(self, i, text):
        if 0 <= i < self.n:
            self.nodes[i].name = text
            return True
        else:
            return False

    def printPairs(self):
        for i in range(0, self.n):
            print('[', i, ']')
            curr = self.nodeLink[i]
            while not (curr is None):
                print(curr.x)
                curr = curr.next
        print('end ')
        return
