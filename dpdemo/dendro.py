DENDRO=0
GRAPH=1
LEFT=2
RIGHT=3

class block():
    def __init__(self,x,y):
        self.x=x
        self.y=x

class ipair():
        def __init__(self,x,y,t,sp):
            self.x=x
            self.y=x
            self.t=t
            self.sp=sp



class interns :
    def __init__(self,q):
        # ipair class
        self.edgelist=[]
        # table of indices of internal edges in edgelist
        self.indexLUT=[]

        # number of internal edges
        self.q=q

        # (for adding edges) edgelist index of new edge to add
        self.count=0

        #  Mersenne Twister random number generator instance/// MTRand class
        self.mtr=mtr
        for i in range(0,q+1) :
            self.indexLUT[i]= []
            self.indexLUT[i][0] = -1
            self.indexLUT[i][1] = -1

