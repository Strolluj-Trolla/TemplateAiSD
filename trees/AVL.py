class AVLnode:

    def __init__(self, value: int):
        self.value=value
        self.left=None
        self.right=None
        self.balanceFactor=0

    def __str__(self):
        return str(self.value)+", balance "+str(self.balanceFactor)

    def rebalance(self):
        #return
        if abs(self.balanceFactor)>1:
            if self.right==None:
                high="left"
            elif self.left==None:
                high="right"
            else:
                high="right" if self.right.balanceFactor>self.left.balanceFactor else "left"
            if high=="right":
                if self.right.balanceFactor>=0:
                    self.rotateLeft(self.value)
                else:
                    self.rotateRight(self.right.value)
                    self.rotateLeft(self.value)
            if high=="left":
                if self.left.balanceFactor<=0:
                    self.rotateRight(self.value)
                else:
                    self.rotateLeft(self.left.value)
                    self.rotateRight(self.value)
        return

    def addNode(self, newValue: int):
        if self.value == None:
            self.value = newValue
            return 1
        if newValue>self.value:
            if self.right==None:
                self.balanceFactor+=1
                self.right=AVLnode(newValue)
                if self.balanceFactor==0:
                    return 0
                return 1
            change=self.right.addNode(newValue)
            self.balanceFactor+=abs(change)
            change=0 if self.balanceFactor==0 else change
            if abs(self.balanceFactor)>1:
                self.rebalance()
                return 0
            return change
        if self.left==None:
            self.balanceFactor-=1
            self.left=AVLnode(newValue)
            if self.balanceFactor==0:
                return 0
            return -1
        change=self.left.addNode(newValue)
        self.balanceFactor-=abs(change)
        change=0 if self.balanceFactor==0 else change
        if abs(self.balanceFactor)>1:
            self.rebalance()
            return 0
        return change
    
    def addNodeUnbalanced(self, newValue: int):
        if self.value == None:
            self.value = newValue
            return 1
        if newValue>self.value:
            if self.right==None:
                self.balanceFactor+=1
                self.right=AVLnode(newValue)
                if self.balanceFactor==0:
                    return 0
                return 1
            change=self.right.addNodeUnbalanced(newValue)
            self.balanceFactor+=abs(change)
            change=0 if self.balanceFactor==0 else change
            if abs(self.balanceFactor)>1:
                #self.rebalance()
                return 0
            return change
        if self.left==None:
            self.balanceFactor-=1
            self.left=AVLnode(newValue)
            if self.balanceFactor==0:
                return 0
            return -1
        change=self.left.addNodeUnbalanced(newValue)
        self.balanceFactor-=abs(change)
        change=0 if self.balanceFactor==0 else change
        if abs(self.balanceFactor)>1:
            #self.rebalance()
            return 0
        return change
    
    def preOrder(self) -> str:
        res=""
        res+=str(self.value)+", "
        if self.left!=None:
            res+=self.left.preOrder()
        if self.right!=None:
            res+=self.right.preOrder()
        return res

    def inOrder(self) -> str:
        res=""
        if self.left!=None:
            res+=self.left.inOrder()
        res+=str(self.value)+", "
        if self.right!=None:
            res+=self.right.inOrder()
        return res
    
    def postOrder(self) -> str:
        res=""
        if self.left!=None:
            res+=self.left.postOrder()+", "
        if self.right!=None:
            res+=self.right.postOrder()+", "
        res+=str(self.value)
        return res
    
    def minNode(self) -> int:
        if self.left==None:
            return self.value
        return self.left.minNode()
    
    def maxNode(self) -> int:
        if self.right==None:
            return self.value
        return self.right.maxNode()
    
    def delete(self, value) -> int:
        if self.value==value:
            if self.left==None and self.right==None:
                self.value=None
                self.balanceFactor=0
                return 3
            if self.left==None:
                #self=self.right
                return -1
            if self.right==None:
                #self=self.left
                return 1
            if abs(self.left.maxNode()-self.value)<abs(self.right.minNode()-value):
                value=self.left.maxNode()
                self.value=value
                prev_bal=self.left.balanceFactor
                res=self.left.delete(value)
                if res==3:
                    self.left=None
                if res==1:
                    self.left=self.left.left
                if res==-1:
                    self.left=self.left.right
                    res=1
                if res!=0:
                    self.balanceFactor+=1
                    if abs(self.balanceFactor)>1:
                        self.rebalance()
                        if prev_bal==0:
                            return 2
                        return 0
                    return 2
                return 0
            else:
                value=self.right.minNode()
                self.value=value
                self.right.delete(value)
                prev_bal=self.right.balanceFactor
                if res==3:
                    self.right=None
                if res==1:
                    self.right=self.right.left
                if res==-1:
                    self.right=self.right.right
                    res=1
                if res!=0:
                    self.balanceFactor-=1
                    if abs(self.balanceFactor)>1:
                        self.rebalance()
                        if prev_bal==0:
                            return 2
                        return 0
                    return 2
                return 0
        else:
            if self.left==None and self.right==None:
                return 0
            if value>self.value:
                prev_bal=self.right.balanceFactor
                res=self.right.delete(value)
                if res==3:
                    self.right=None
                if res==1:
                    self.right=self.right.left
                if res==-1:
                    self.right=self.right.right
                    res=1
                if res!=0:
                    self.balanceFactor-=1
                    if abs(self.balanceFactor)>1:
                        self.rebalance()
                        if prev_bal==0:
                            return 2
                        return 0
                    return 2
                return 0
            if value<self.value:
                prev_bal=self.left.balanceFactor
                res=self.left.delete(value)
                if res==3:
                    self.left=None
                if res==1:
                    self.left=self.left.left
                if res==-1:
                    self.left=self.left.right
                if res!=0:
                    self.balanceFactor+=1
                    if abs(self.balanceFactor)>1:
                        self.rebalance()
                        if prev_bal==0:
                            return 2
                        return 0
                    return 2
                return 0
            return 0
        
    def ereaseTree(self):
        elems=self.postOrder().replace(",","").split()
        for elem in elems:
            self.delete(int(elem))

    #rotator is not pivot
    def rotateLeft(self, rotator: int):
        if rotator==self.value:
            newLeft=AVLnode(self.value)
            newLeft.left=self.left
            newLeft.right=self.right.left
            newLeft.balanceFactor=0
            self.value=self.right.value
            self.balanceFactor=0
            self.left=newLeft
            self.right=self.right.right
            return 0
        else:
            if rotator>self.value and self.right!=None:
                self.right.rotateLeft(rotator)
                return 0
            if rotator<self.value and self.left!=None:
                self.left.rotateLeft(rotator)
                return 0
        return 0

    #rotator is not pivot
    def rotateRight(self, rotator: int):
        if rotator==self.value:
            newRight=AVLnode(self.value)
            newRight.right=self.right
            newRight.left=self.left.right
            newRight.balanceFactor=0
            self.value=self.left.value
            self.balanceFactor=0
            self.left=self.left.left
            self.right=newRight
            return 0
        else:
            if rotator>self.value and self.right!=None:
                self.right.rotateRight(rotator)
                return 0
            if rotator<self.value and self.left!=None:
                self.left.rotateRight(rotator)
                return 0
        return 0

    def AVLconstruct(self, list):
        #loops=1
        #while len(list)>0:
        #    added=0
        #    median = int(len(list)/2**loops)
        #    for i in range(0,loops, 1):
        #        self.addNode(list.pop(median*(i+1)))
        #        added+=1
        #    loops+=1
        #return
        if len(list)==0:
            return
        median = int(len(list)/2)
        self.addNodeUnbalanced(list[median])
        if median>0:
            self.AVLconstruct(list[:median])
        if median<len(list):
            self.AVLconstruct(list[median+1:])
        return


inp=input("Podaj liste: ")
inp=[int(x) for x in inp.strip().split()]
inp.sort()
print(inp)
tree=AVLnode(None)
tree.AVLconstruct(inp)
print(tree.preOrder())
print(tree.postOrder())
tree.delete(4)
print(tree.preOrder())
print(tree.postOrder())