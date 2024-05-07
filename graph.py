import random

class graph():
     
    def __init__(self, type: str):
        self.type=type
        self.data=[]

    def _randomEdges(self, nodeCount, edgeCount):
        edges=[]
        for i in range(nodeCount-1):
            for j in range(i+1, nodeCount):
                edges.append([i,j])
        random.shuffle(edges)
        edges=edges[:edgeCount]
        edges.sort()
        return edges



    def generate(self, nodeCount: int, saturation: int):
        if self.type=="matrix":
            for i in range(nodeCount):
                temp=[]
                for j in range(nodeCount):
                    temp.append(0)
                self.data.append(temp)
            for edge in self._randomEdges(nodeCount, int((nodeCount*(nodeCount-1)/2)*(saturation/100))):
                self.data[edge[0]][edge[1]]=1
        elif self.type=="list":
            for i in range(nodeCount):
                self.data.append([])
            for edge in self._randomEdges(nodeCount, int((nodeCount*(nodeCount-1)/2)*(saturation/100))):
                self.data[edge[0]].append(edge[1])
        elif self.type=="table":
            for edge in self._randomEdges(nodeCount, int((nodeCount*(nodeCount-1)/2)*(saturation/100))):
                self.data.append(edge)
        return
    
    def dataProvided(self, data):
        self.data=data
        return
    
    def __str__(self):
        res=""
        if self.type=="matrix":
            nodeCount=len(self.data)
            res+=" |"
            for i in range(nodeCount):
                res+=str(i)+" "
            res+="\n_+"
            for i in range(nodeCount):
                res+="__"
            res+="\n"
            for i, row in enumerate(self.data):
                res+=str(i)+"|"+str(row).replace("[","").replace("]","").replace(",","")+"\n"
        elif self.type=="list":
            for i, node in enumerate(self.data):
                res+=str(i)+" | "
                for successor in node:
                    res+=str(successor)+", "
                res+="\n"
        elif self.type=="table":
            for edge in self.data:
                res+=str(edge).replace("[","").replace("]","").replace(", ","---")+"\n"
        return res

graf=graph("matrix")
graf.generate(5,50)
print(graf)
