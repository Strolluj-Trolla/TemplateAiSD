from trees import BST
from trees import AVL
import sys
import time

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


"""
To run this file issue this command:
python3 HelloWorld.py

Python as a interpreted language executes code directly without a separate compilation step, 
translating and running the source code on-the-fly during execution.
"""

# Checks if the Python script is being run as the main program (not imported as a module)
if len(sys.argv) != 3 or sys.argv[1] != "--tree":
        print("Usage: python script.py --tree <BST or AVL>")
        sys.exit(1)

sys.setrecursionlimit(100000000)

if sys.argv[2] == "BST":
    if __name__ == "__main__":
        userInput = ""
        print("Give nodes to add (numbers separated by space)")
        node = input("node> ").split()
        for i in range(len(node)-1,-1,-1):
            if not is_number(node[i]):
                node.pop(i)
        node = list(map(int, node))
        size=len(node)
        print("insert> "+str(node).replace(",","").replace("[","").replace("]",""))
        timeElapsed=time.time()
        tree = BST.BSTnode(node[0])
        for i in node[1:]:
            tree.addNode(i)
        timeElapsed=time.time()-timeElapsed
        with open("BST_creation.csv", "a") as results:
            results.write(str(size)+", "+str(timeElapsed)+"\n")
        print("Type 'Help' for more informations.")
        while True:

            if userInput == "Exit":
                break

            userInput = input("action> ")

            if userInput == "Help":
                print("List of acction you can perform:")
                print("Help - Show this message")
                print("Print - Print the tree using Pre-order, In-order, Post-order")
                print("Remove - Remove elements of a tree")
                print("Delete - Delete whole tree")
                print("Export - Export the tree to tickzpicture")
                print("Rebalance - Rebalance the tree")
                print("Max - Find the maximal node")
                print("Min - Find the minimal node")
                print("Add - Add new node to the tree")
                print("Exit - Exits the program")
                
            if userInput == "Print":
                timeElapsed=time.time()
                print("In-order: "+tree.inOrder())
                timeElapsed=time.time()-timeElapsed
                with open("BST_print.csv", "a") as results:
                    results.write(str(size)+", "+str(timeElapsed)+"\n")
                print("Pre-order: "+tree.preOrder())
                print("Post-order: "+tree.postOrder())
            
            if userInput == "Remove":
                print("Give nodes to remove (numbers separated by space)")
                node = input("node> ").split()
                for i in range(len(node)-1,-1,-1):
                    if not is_number(node[i]):
                        node.pop(i)
                node = list(map(int, node))
                for i in node:
                    tree.delete(i)

            if userInput == "Delete":
                tree.ereaseTree()

            if userInput == "Rebalance":
                timeElapsed=time.time()
                tree.DSW()
                timeElapsed=time.time()-timeElapsed
                with open("BST_rebalance.csv", "a") as results:
                    results.write(str(size)+", "+str(timeElapsed)+"\n")
            
            if userInput == "Max":
                timeElapsed=time.time()
                print("Max node: "+str(tree.maxNode()))
                timeElapsed=time.time()-timeElapsed
                with open("BST_max.csv", "a") as results:
                    results.write(str(size)+", "+str(timeElapsed)+"\n")
            
            if userInput == "Min":
                timeElapsed=time.time()
                print("Min node: "+str(tree.minNode()))
                timeElapsed=time.time()-timeElapsed
                with open("BST_min.csv", "a") as results:
                    results.write(str(size)+", "+str(timeElapsed)+"\n")

            if userInput=="Export":
                print(tree.TiKZgenerate())

            if userInput == "Add":
                print("Give nodes to add (numbers separated by space)")
                node = input("node> ").split()
                for i in range(len(node)-1,-1,-1):
                    if not is_number(node[i]):
                        node.pop(i)
                node = list(map(int, node))
                print("insert> "+str(node).replace(",","").replace("[","").replace("]",""))
                for i in node:
                    tree.addNode(i) 


if sys.argv[2] == "AVL":
    if __name__ == "__main__":
        userInput = ""
        print("Give nodes to add (numbers separated by space)")
        node = input("node> ").split()
        for i in range(len(node)-1,-1,-1):
            if not is_number(node[i]):
                node.pop(i)
        node = list(map(int, node))
        size=len(node)
        print("insert> "+str(node).replace(",","").replace("[","").replace("]",""))
        tree=AVL.AVLnode(None)
        timeElapsed=time.time()
        tree.AVLconstruct(node)
        timeElapsed=time.time()-timeElapsed
        with open("AVL_creation.csv", "a") as results:
            results.write(str(size)+", "+str(timeElapsed)+"\n")
        print("Type 'Help' for more informations.")
        while True:

            if userInput == "Exit":
                break

            userInput = input("action> ")

            if userInput == "Help":
                print("List of acction you can perform:")
                print("Help - Show this message")
                print("Print - Print the tree using Pre-order, In-order, Post-order")
                print("Remove - Remove elements of a tree")
                print("Delete - Delete whole tree")
                print("Export - Export the tree to tickzpicture")
                # print("Rebalance - Rebalance the tree")
                print("Max - Find the maximal node")
                print("Min - Find the minimal node")
                print("Add - Add new node to the tree")
                print("Exit - Exits the program")
                
            if userInput == "Print":
                timeElapsed=time.time()
                print("In-order: "+tree.inOrder())
                timeElapsed=time.time()-timeElapsed
                with open("AVL_print.csv", "a") as results:
                    results.write(str(size)+", "+str(timeElapsed)+"\n")
                print("Pre-order: "+tree.preOrder())
                print("Post-order: "+tree.postOrder())
            
            if userInput == "Remove":
                print("Give nodes to remove (numbers separated by space)")
                node = input("node> ").split()
                for i in range(len(node)-1,-1,-1):
                    if not is_number(node[i]):
                        node.pop(i)
                node = list(map(int, node))
                for i in node:
                    tree.delete(i)

            if userInput == "Delete":
                tree.ereaseTree()

            if userInput == "Rebalance":
                #tree.rebalance()
                print(":)")
            
            if userInput == "Max":
                timeElapsed=time.time()
                print("Max node: "+str(tree.maxNode()))
                timeElapsed=time.time()-timeElapsed
                with open("AVL_max.csv", "a") as results:
                    results.write(str(size)+", "+str(timeElapsed)+"\n")
            
            if userInput == "Min":
                timeElapsed=time.time()
                print("Min node: "+str(tree.minNode()))
                timeElapsed=time.time()-timeElapsed
                with open("AVL_min.csv", "a") as results:
                    results.write(str(size)+", "+str(timeElapsed)+"\n")

            if userInput=="Export":
                print(tree.TiKZgenerate())

            if userInput == "Add":
                print("Give nodes to add (numbers separated by space)")
                node = input("node> ").split()
                for i in range(len(node)-1,-1,-1):
                    if not is_number(node[i]):
                        node.pop(i)
                node = list(map(int, node))
                print("insert> "+str(node).replace(",","").replace("[","").replace("]",""))
                for i in node:
                    tree.addNode(i)
