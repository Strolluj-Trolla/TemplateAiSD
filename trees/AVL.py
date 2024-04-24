class AVLnode:

    def __init__(self, value: int):
        self.value=value
        self.left=None
        self.right=None

    def addNode(self, newValue: int):
        if self.value == None:
            self.value = newValue
            return
        if newValue>self.value:
            if self.right==None:
                self.right=AVLnode(newValue)
                return
            self.right.addNode(newValue)
            return
        if self.left==None:
            self.left=AVLnode(newValue)
            return 
        self.left.addNode(newValue)
        return
    
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

    def AVLconstruct(self, list):
        if len(list)==0:
            return
        median = int(len(list)/2)
        self.addNode(list[median])
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
print(tree.postOrder())