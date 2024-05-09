import random
import copy

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
                self.data[edge[1]][edge[0]]=-1
                self.data[edge[0]][edge[1]]=1
        elif self.type=="list":
            for i in range(nodeCount):
                self.data.append([])
            for edge in self._randomEdges(nodeCount, int((nodeCount*(nodeCount-1)/2)*(saturation/100))):
                self.data[edge[0]].append(edge[1])
        elif self.type=="table":
            for edge in self._randomEdges(nodeCount, int((nodeCount*(nodeCount-1)/2)*(saturation/100))):
                self.data.append(edge)
        return nodeCount
    
    def dataProvided(self, data):
        if self.type=="matrix":
            for i in range(len(data)):
                temp=[]
                for j in range(len(data)):
                    temp.append(0)
                self.data.append(temp)
            for i, node1 in enumerate(data):
                for node2 in node1:
                    self.data[i][node2]=1
                    self.data[node2][i]=-1
        if self.type=="list":
            self.data=data
        if self.type=="table":
            for i, node1 in enumerate(data):
                for node2 in node1:
                    self.data.append([i, node2])
        return
    
    def __str__(self):
        res=""
        if self.type=="matrix":
            nodeCount=len(self.data)
            res+=" |"
            for i in range(nodeCount):
                res+=str(i+1)+" "
            res+="\n_+"
            for i in range(nodeCount):
                res+="__"
            res+="\n"
            for i, row in enumerate(self.data):
                res+=str(i+1)+"|"+str(row).replace("[","").replace("]","").replace(",","")+"\n"
        elif self.type=="list":
            for i, node in enumerate(self.data):
                res+=str(i+1)+" | "
                for successor in node:
                    res+=str(successor+1)+", "
                res+="\n"
        elif self.type=="table":
            for edge in self.data:
                res+=str([x+1 for x in edge]).replace("[","").replace("]","").replace(", ","---")+"\n"
        return res
    
    def edgeExists(self, node1: int, node2: int) -> bool:
        #if node2<node1:
        #    node1, node2= node2, node1
        # or self.data[node1][node2]==-1
        #node1-=1
        #node2-=1
        if self.type=="matrix":
            return (self.data[node1][node2]==1)
        elif self.type=="list":
            return (node2 in self.data[node1])
        else:
            return ([node1, node2] in self.data)
        
    def BFS(self):
        visited=[]
        queue=[0]
        while(len(queue)>0):
            if self.type=="matrix":
                for successor, check in enumerate(self.data[queue[0]]):
                    if check==1 and not successor in visited and not successor in queue:
                        queue.append(successor)
            if self.type=="list":
                for successor in self.data[queue[0]]:
                    if not successor in visited and not successor in queue:
                        queue.append(successor)
            if self.type=="table":
                for edge in self.data:
                    if edge[0]==queue[0] and not edge[1] in visited and not edge[1] in queue:
                        queue.append(edge[1])
            visited.append(queue.pop(0))
        return [x+1 for x in visited]
    
    def DFS(self):
        visited=[]
        queue=[0]
        while(len(queue)>0):
            currentIndex=len(queue)-1
            if self.type=="matrix":
                for successor, check in enumerate(self.data[queue[currentIndex]]):
                    if check==1 and not successor in visited:
                        queue.append(successor)
            if self.type=="list":
                for successor in self.data[queue[currentIndex]]:
                    if not successor in visited:
                        queue.append(successor)
            if self.type=="table":
                for edge in self.data:
                    if edge[0]==queue[currentIndex] and not edge[1] in visited:
                        queue.append(edge[1])
            visited.append(queue.pop(currentIndex))
        return [x+1 for x in visited]
    
    def Kahn(self, nodect: int):
        #global nodect
        tmp = copy.deepcopy(self.data)
        L = []
        if self.type == "matrix":
            in_deg = [0]*len(tmp)
            for i in range(len(tmp)):
                for j in tmp[i]:
                    if j == -1:
                        in_deg[i]+=1

            queue = []
            for index, i in enumerate(in_deg):
                if i == 0:
                    queue.append(index)
            while queue != []:
                for index, i in enumerate(queue):
                    L.append(i+1)
                    for j in range(len(tmp[i])):
                        if tmp[i][j]==1:
                            in_deg[j] -= 1
                            if in_deg[j] == 0:
                                queue.append(j)
                for x in range(len(L)):
                    queue.pop(0)
            if max(in_deg)>0:
                print("Cycle detected")
            else:
                print(str(L).replace("[", "").replace("]", ""))

        if self.type == "list":
            in_deg = [0]*len(tmp)
            for i in tmp:
                for j in i:
                    in_deg[j]+=1
            queue = []
            for index, i in enumerate(in_deg):
                if i == 0:
                    queue.append(index)
            while queue != []:
                for index, i in enumerate(queue):
                    L.append(i+1)
                    for j in tmp[i]:
                        in_deg[j] -= 1
                        if in_deg[j] == 0:
                            queue.append(j)
                for x in range(len(L)):
                    queue.pop(0)
            if max(in_deg)>0:
                print("Cycle detected")
            else:
                print(str(L).replace("[", "").replace("]", ""))

        if self.type == "table":
            in_deg = [0]*nodect
            for i in tmp:
                in_deg[i[1]] += 1
            queue = []
            for index, i in enumerate(in_deg):
                if i == 0:
                    queue.append(index)
            while queue != []:
                for index, i in enumerate(queue):
                    L.append(i+1)
                    for j in tmp:
                        if j[0]==i:
                            in_deg[j[1]] -=1
                            if in_deg[j[1]] == 0:
                                queue.append(j[1])
                for x in range(len(L)):
                    queue.pop(0)
            if max(in_deg)>0:
                print("Cycle detected")
            else:
                print(str(L).replace("[", "").replace("]", ""))



    def Tarjan(self, nodect: int):
        #global nodect
        tmp = copy.deepcopy(self.data)
        x = 0
        L = []
        unmarked = []
        temporary = [0]*nodect
        if self.type == "matrix":
            def visitm(n):
                if pernament[n]==1:
                    return
                if temporary[n]==1:
                    print("cycle detected")
                temporary[n] = 1

                for index, i in enumerate(tmp[n]):
                    if i == 1:
                        visitm(index)
                pernament[n] = 1
                L.append(n+1)
                return



            for i in range(nodect):
                unmarked.append(i)
            pernament = [-1]*nodect

            while min(pernament)==-1:
                visitm(x)
                x+=1
            L.reverse()
            print(str(L).replace("[", "").replace("]", ""))
        
        
        if self.type == "list":

            def visitl(n):
                if pernament[n]==1:
                    return
                if temporary[n]==1:
                    print("cycle detected")
                temporary[n] = 1

                for i in tmp[n]:
                    visitl(i)
                pernament[n] = 1
                L.append(n+1)
                return


            for i in range(nodect):
                unmarked.append(i)
            pernament = [-1]*nodect

            while min(pernament)==-1:
                visitl(x)
                x+=1
            L.reverse()
            print(str(L).replace("[", "").replace("]", ""))
        
        if self.type == "table":

            def visitt(n):
                if pernament[n]==1:
                    return
                if temporary[n]==1:
                    print("cycle detected")
                temporary[n] = 1

                for i in tmp:
                    if i[0]==n:
                        visitt(i[1])
                pernament[n] = 1
                L.append(n+1)
                return


            for i in range(nodect):
                unmarked.append(i)
            pernament = [-1]*nodect

            while min(pernament)==-1:
                visitt(x)
                x+=1
            L.reverse()
            print(str(L).replace("[", "").replace("]", ""))

# graf=graph("table")
# nodect = graf.generate(5,50)
# # graf.dataProvided([[1,9],[2, 6],[3],[5],[1, 6],[8],[7,8],[3,5,8],[],[4,5]])
# # graf.dataProvided([[0,0,1,0],[0,0,-1,-1],[-1,1,0,1],[0,1,-1,0]])
# print(graf)
# print(graf.data)
# graf.Tarjan()


# graf.dataProvided([[1,9],[2, 6],[3],[5],[1, 6],[8],[7,8],[3,5,8],[],[4,5]])
# print(graf.data)

# graf.Kahn()
# print(str(graf.edgeExists(2,5)))

# print(str(graf.BFS()).replace("[","").replace("]", "").replace(",", ""))
# print(str(graf.DFS()).replace("[","").replace("]", "").replace(",", ""))
