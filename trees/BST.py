class BSTnode:

    def __init__(self, value: int):
        self.value=value
        self.left=None
        self.right=None
    
    def minNode(self) -> int:
        if self.left==None:
            return self.value
        return self.left.minNode()
    
    def maxNode(self) -> int:
        if self.right==None:
            return self.value
        return self.right.minNode()
    
    def addNode(self, newValue: int):
        if newValue>self.value:
            if self.right==None:
                self.right=BSTnode(newValue)
                return
            self.right.addNode(newValue)
            return
        if self.left==None:
            self.left=BSTnode(newValue)
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
    
    #dopracować
    def TiKZgenerate(self) -> str:
        res=f"node {self.value}"
        if self.left==None and self.right==None:
            return res
        left=f"child {self.left.TiKZgenerate()[0:]}" if self.left!=None else "child[missing]"
        right=f"child {self.right.TiKZgenerate()[0:]}" if self.right!=None else "child[missing]"
        res+=" \{"+left+"} \{"+right+"}"
        return "\\"+res
    
    def delete(self, value):
        if self.value==value:
            if self.left==None and self.right==None:
                self=None
                return
            if self.left==None:
                self=self.right
                return
            if self.right==None:
                self=self.left
                return
            if abs(self.left.maxNode())-abs(value<self.right.minNode()-value):
                value=self.left.maxNode()
                self.value=value
                self.left.delete(value)
                return
            else:
                value=self.right.minNode()
                self.value=value
                self.right.delete(value)
                return
        else:
            if self.left==None and self.right==None:
                return
            if value>self.value:
                self.right.delete(value)
                return
            self.left.delete(value)
            return
            
inp=input("Podaj liste: ")
inp=[int(x) for x in inp.strip().split()]

print(inp)

tree=BSTnode(inp.pop(0))
for num in inp:
    tree.addNode(num)
    
print("Max "+str(tree.maxNode()))
print("Min "+str(tree.minNode()))

print("In-order: "+tree.inOrder())
print("Pre-order: "+tree.preOrder())
print("Post-order: "+tree.postOrder())
print(tree.TiKZgenerate())