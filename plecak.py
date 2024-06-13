import random

def mergeSort(bp):
    if (len(bp)>1):
        middle=len(bp)//2
        left=bp[:middle]
        right=bp[middle:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while (i<len(left) and j<len(right)):
            if (left[i][0]/left[i][1]>=right[j][0]/right[j][1]):
                bp[k]=left[i]
                i+=1
            else:
                bp[k]=right[j]
                j+=1
            k+=1
        while (j<len(right)):
            bp[k]=right[j]
            k+=1
            j+=1
        while (i<len(left)):
            bp[k]=left[i]
            k+=1
            i+=1

class plecak():
    
    def __init__(self):
        self.bp = []
        self.n = 0
        self.c = 0


    def __init__(self, bp, n, c):
        self.bp = bp
        self.n = n
        self.c = c


    def _check(self, temp):
        if (len(temp)!=2):
            return True
        for i in range(2):
            try:
                temp[i]=int(temp[i])
                if(temp[i]<1):
                    return True
            except ValueError:
                return True
        return False
    

    def from_input(self):
        temp=input("Podaj ilość elementów i rozmiar plecaka: ").split(" ")
        while(self._check(temp)):
            print("Podano niewłaściwe dane.")
            temp=input("Podaj ilość elementów i rozmiar plecaka: ").split(" ")
        #(n,b)=(int(x) for x in input("Podaj ilość elementów i rozmiar plecaka: ").split(" "))
        (self.n,self.c)=temp
        self.bp=[]
        for i in range(self.n):
            #(w,r)=(int(x) for x in input("Podaj rozmiar i wartość przedmiotu: ").split(" "))
            temp=input("Podaj rozmiar i wartość przedmiotu: ").split(" ")
            while(self._check(temp)):
                print("Podajno niewłaściwe dane.")
                temp=input("Podaj rozmiar i wartość przedmiotu: ").split(" ")
            (w,r)=temp
            (r,w)=(w,r) # ROZMIAR WARTOŚĆ
            self.bp.append([w,r])
        return
    

    def from_file(self, file):
        f=open(file,"r")
        (self.n,self.c)=[int(x) for x in f.readline().split(" ")]
        bp=[]
        for _ in range(self.n):
            (value,size)=(int(x) for x in f.readline().split(" "))
            (size,value)=(value,size)  # ROZMIAR WARTOŚĆ
            self.bp.append([value,size])
        f.close()
        return
    

    def gen(self):
        self.bp=[]
        for _ in range(self.n):
            self.bp.append([random.randint(1,10),random.randint(1,10)])
        return


    def dynamic(self):
        matrix=[[0 for _ in range(self.c+1)] for _ in range(self.n+1)]
        for i in range(1,self.n+1):
            for j in range(self.c+1):
                value=self.bp[i-1][0]
                size=self.bp[i-1][1]
                if(size>j):
                    matrix[i][j]=matrix[i-1][j]
                else:
                    matrix[i][j]=max(matrix[i-1][j],matrix[i-1][j-size]+value)
        
        solution=[]
        j=self.c
        sum_size=0
        for i in range(self.n,-1,-1):
            if(matrix[i][j]>matrix[i-1][j]):
                solution.insert(0,self.bp[i-1])
                j-=self.bp[i-1][1]
                sum_size+=self.bp[i-1][1]
        
        return (solution, sum_size,matrix[self.n][self.c])
    
    def greedy(self):
        solution=[]
        size=0
        value=0
        i=0
        mergeSort(self.bp)
        #print(self.bp)
        while(i<self.n and size<=self.c):
            if(size+self.bp[i][1]<=self.c):
                solution.insert(0,self.bp[i])
                size+=self.bp[i][1]
                value+=self.bp[i][0]
            i+=1
        return (solution, size, value)
    
    def brute(self):
        max_value=0
        max_size=0
        solution=[]
        for x in range(1,2**self.n):
            x=bin(x)[2:][::-1]
            size=0
            value=0
            temp=[]
            for i in range(len(x)):
                if(int(x[i])):
                    size+=self.bp[i][1]
                    value+=self.bp[i][0]
                    temp.append(self.bp[i])
            if(size<=self.c):
                if(value>max_value):
                    max_value=value
                    max_size=size
                    solution=temp
        return (solution, max_size, max_value)

