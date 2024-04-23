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
        if self.right==None:
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
            res+=self.right.preOrder()[:-2]
        return res

    def inOrder(self) -> str:
        res=""
        if self.left!=None:
            res+=self.left.inOrder()
        res+=str(self.value)+", "
        if self.right!=None:
            res+=self.right.inOrder()[:-2]
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
        return 0
            
    
tree=BSTnode(9)
tree.addNode(6)
tree.addNode(12)
print(tree.maxNode())
print(tree.minNode())
print(tree.inOrder())
print(tree.preOrder())
print(tree.postOrder())
print(tree.TiKZgenerate())