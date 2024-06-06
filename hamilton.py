import random

class graph():

    def __init__(self):
        matrix=[]

    def gen_Hamiltonian_graph(self, node_count,saturation):
        matrix=[[0 for j in range(node_count)] for i in range(node_count)]
        edge_count=int(saturation/100*node_count*(node_count-1)//2)
        if(node_count==1):
            return matrix
        if(edge_count<node_count):
            print("Nie można stworzyć grafu nieskierowanego z cyklem Hamiltona.")
            return None
        used=[False]*node_count
        curr=random.randint(0,node_count-1)
        start=curr
        used[curr]=True
        for i in range(node_count-1): #make cycle
            prev=curr
            curr=random.randint(0,node_count-1)
            while(used[curr]==True):
                curr=random.randint(0,node_count-1)
            used[curr]=True
            matrix[prev][curr]=1
            matrix[curr][prev]=1
        matrix[start][curr] = 1
        matrix[curr][start] = 1
        for i in range(edge_count-node_count): #add edges so graph can have given saturation
            v1=random.randint(0,node_count-1)
            v2=random.randint(0,node_count-1)
            while(v2==v1):
                v2=random.randint(0,node_count-1)
            while(matrix[v1][v2]==1):
                v1 = random.randint(0, node_count - 1)
                v2 = random.randint(0, node_count - 1)
                while (v2 == v1):
                    v2 = random.randint(0, node_count - 1)
            matrix[v1][v2]=1
            matrix[v2][v1]=1
        self.matrix =  matrix


    def generate_non_hamiltonian_graph(self, n):
        edges_amount = 0.5 * (n * (n - 1) / 2)
        matrix = [[0] * n for _ in range(n)]
        count = 0
        if edges_amount < n - 1:
            print("Wrong node count or saturation")
            return

        start = random.randint(0, n-1)
        lst = []
        tmp = start
        lst.append(start)
        while count < n - 1:
            v2 = random.randint(0, n-1)
            if v2 not in lst:
                matrix[tmp][v2] = 1
                matrix[v2][tmp] = 1
                lst.append(v2)
                tmp = v2
                count += 1

        matrix[start][tmp] = 1
        matrix[tmp][start] = 1
        count += 1

        while count <= edges_amount:
            v1 = random.randint(0, n-1)
            v2 = random.randint(0, n-1)
            v3 = random.randint(0, n-1)
            if v1 != v2 and v1 != v3 and v2 != v3 and v1 != start and v3 != start and v2 != start:
                if matrix[v1][v2] == 0 and matrix[v2][v3] == 0 and matrix[v1][v3] == 0:
                    matrix[v1][v2] = 1
                    matrix[v2][v1] = 1
                    matrix[v1][v3] = 1
                    matrix[v3][v1] = 1
                    matrix[v3][v2] = 1
                    matrix[v2][v3] = 1
                    count += 3

        for i in range(n):
            matrix[start][i] = 0
        for i in range(n):
            matrix[i][start] = 0

        self.matrix = matrix



    # Array to mark visited vertices
    # Counter for visited vertices
    # List to keep track of visited vertices in the current path

    # node (number), graph
    def Hamiltonian(self, v,  node_count, visited, Visited_vert, current_path):
        adj_matrix = self.matrix
        start = node_count - 1
        Visited_vert[v] = True
        visited += 1
        current_path.append(v)

        for i in range(node_count):
            if adj_matrix[v][i] != 0:
                if i == start and visited == node_count:
                    return True
                if not Visited_vert[i]:
                    if self.Hamiltonian(i, node_count, visited, Visited_vert, current_path):
                        return True

        Visited_vert[v] = False
        visited -= 1
        current_path.pop()
        return False

    # graph
    def Hcycle(self, node_count, visited, Visited_vert, current_path):
        adj_matrix = self.matrix;
        if self.Hamiltonian(node_count - 1, node_count, visited, Visited_vert, current_path):
            current_path.append(node_count - 1)
            return current_path
        else:
            return None

    # graph, node (number), list 
    def euler(self, matrix, v, s, node_count):

        for i in range(node_count):
            if matrix[v][i] == 1:
                matrix[v][i] = 0
                matrix[i][v] = 0
                self.euler(matrix, i, s, node_count)
        s.append(v)
        return s
    

    def __str__(self):
        res=""
        nodeCount=len(self.matrix)
        res+=" |"
        for i in range(nodeCount):
            res+=str(i+1)+" "
        res+="\n_+"
        for i in range(nodeCount):
            res+="__"
        res+="\n"
        for i, row in enumerate(self.matrix):
            res+=str(i+1)+"|"+str(row).replace("[","").replace("]","").replace(",","")+"\n"
        return res