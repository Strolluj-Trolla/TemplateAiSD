from math import log2

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
        return self.right.maxNode()
    
    def addNode(self, newValue: int):
        if self.value == None:
            self.value = newValue
            return
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
    
    def delete(self, value) -> int:
        if self.value==value:
            if self.left==None and self.right==None:
                self.value=None
                return 1
            if self.left==None:
                self=self.right
                return 3
            if self.right==None:
                self=self.left
                return 2
            if abs(self.left.maxNode())-abs(value<self.right.minNode()-value):
                value=self.left.maxNode()
                self.value=value
                res=self.left.delete(value)
                if res==1:
                    self.left=None
                if res==2:
                    self.left=self.left.left
                if res==3:
                    self.left=self.left.right
                return 0
            else:
                value=self.right.minNode()
                self.value=value
                self.right.delete(value)
                if res==1:
                    self.right=None
                if res==2:
                    self.right=self.right.left
                if res==3:
                    self.right=self.right.right
                return 0
        else:
            if self.left==None and self.right==None:
                return 0
            if value>self.value:
                res=self.right.delete(value)
                if res==1:
                    self.right=None
                if res==2:
                    self.right=self.right.left
                if res==3:
                    self.right=self.right.right
                return 0
            if value<self.value:
                res=self.left.delete(value)
                if res==1:
                    self.left=None
                if res==2:
                    self.left=self.left.left
                if res==3:
                    self.left=self.left.right
                return 0
            return 0
        
    def ereaseTree(self):
        elems=self.postOrder().replace(",","").split()
        for elem in elems:
            self.delete(int(elem))

    #rotator is not pivot
    def rotateLeft(self, rotator: int):
        if rotator==self.value:
            newLeft=BSTnode(self.value)
            newLeft.left=self.left
            newLeft.right=self.right.left
            self.value=self.right.value
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
            newRight=BSTnode(self.value)
            newRight.right=self.right
            newRight.left=self.left.right
            self.value=self.left.value
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
    
    def degenerate(self, count: int):
        if self.left != None:
            self.rotateRight(self.value)
            count = self.degenerate(count)
        else:
            if self.right != None:
                count = self.right.degenerate(count)
            return count+1
        return count

    def DSW(self):
        count = 0
        count = self.degenerate(count)
        rotationCount = count + 1 - 2**(int(log2(count + 1)))
        node = self
        ct = rotationCount
        while ct>0:
            node.rotateLeft(node.value)
            node=node.right
            ct -= 1
            
        
        y = count - rotationCount
        while y>1:
            node = self
            tmp = int(y/2)
            while tmp > 0:
                node.rotateLeft(node.value)
                node=node.right
                tmp -= 1
            y=int(y/2)

# inp=input("Podaj liste: ")
# inp=[int(x) for x in inp.strip().split()]

# print(inp)

# tree=BSTnode(inp.pop(0))
# for num in inp:
#     tree.addNode(num)
    
# print("Max "+str(tree.maxNode()))
# print("Min "+str(tree.minNode()))

# print("In-order: "+tree.inOrder())
# print("Pre-order: "+tree.preOrder())
# print("Post-order: "+tree.postOrder())
#print(tree.TiKZgenerate())

# tree.rotateRight(2)
# tree.rotateRight(7)

# print("")

# print("In-order: "+tree.inOrder())
# print("Pre-order: "+tree.preOrder())
# print("Post-order: "+tree.postOrder())

# tree.rotateLeft(2)

# print("")
# print("In-order: "+tree.inOrder())
# print("Pre-order: "+tree.preOrder())
# print("Post-order: "+tree.postOrder())
# print("Degenerated: ")
# tree.DSW()
# tree.delete(10)
# tree.addNode(9)
# tree.addNode(5)
# tree.addNode(11)
# # tree.ereaseTree()
# print("In-order: "+tree.inOrder())
# print("Pre-order: "+tree.preOrder())
# print("Post-order: "+tree.postOrder())
