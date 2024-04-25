from trees import BST
from trees import AVL
import sys


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



if sys.argv[2] == "BST":
    if __name__ == "__main__":
        userInput = ""
        print("Give nodes to add (numbers separated by space)")
        node = list(map(int, input("node> ").split()))
        print("insert> "+str(node).replace(",","").replace("[","").replace("]",""))
        tree = BST.BSTnode(node[0])
        for i in node[1:]:
            tree.addNode(i)
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
                # print("Export - Export the tree to tickzpicture")
                print("Rebalance - Rebalance the tree")
                print("Max - Find the maximal node")
                print("Min - Find the minimal node")
                print("Add - Add new node to the tree")
                print("Exit - Exits the program")
                
            if userInput == "Print":
                print("In-order: "+tree.inOrder())
                print("Pre-order: "+tree.preOrder())
                print("Post-order: "+tree.postOrder())
            
            if userInput == "Remove":
                print("Give nodes to remove (numbers separated by space)")
                node = list(map(int, input("node> ").split()))
                for i in node:
                    tree.delete(i)

            if userInput == "Delete":
                tree.ereaseTree()

            if userInput == "Rebalance":
                tree.DSW()
            
            if userInput == "Max":
                print("Max node: "+str(tree.maxNode()))
            
            if userInput == "Min":
                print("Min node: "+str(tree.minNode()))

            if userInput == "Add":
                print("Give nodes to add (numbers separated by space)")
                node = list(map(int, input("node> ").split()))
                print("insert> "+str(node).replace(",","").replace("[","").replace("]",""))
                for i in node:
                    tree.addNode(i) 


if sys.argv[2] == "AVL":
    if __name__ == "__main__":
        userInput = ""
        print("Give nodes to add (numbers separated by space)")
        node = list(map(int, input("node> ").split()))
        print("insert> "+str(node).replace(",","").replace("[","").replace("]",""))
        tree = AVL.AVLnode(node[0])
        for i in node[1:]:
            tree.addNode(i)
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
                # print("Export - Export the tree to tickzpicture")
                # print("Rebalance - Rebalance the tree")
                print("Max - Find the maximal node")
                print("Min - Find the minimal node")
                print("Add - Add new node to the tree")
                print("Exit - Exits the program")
                
            if userInput == "Print":
                print("In-order: "+tree.inOrder())
                print("Pre-order: "+tree.preOrder())
                print("Post-order: "+tree.postOrder())
            
            if userInput == "Remove":
                print("Give nodes to remove (numbers separated by space)")
                node = list(map(int, input("node> ").split()))
                for i in node:
                    tree.delete(i)

            if userInput == "Delete":
                tree.ereaseTree()

            if userInput == "Rebalance":
                tree.rebalance()
            
            if userInput == "Max":
                print("Max node: "+str(tree.maxNode()))
            
            if userInput == "Min":
                print("Min node: "+str(tree.minNode()))

            if userInput == "Add":
                print("Give nodes to add (numbers separated by space)")
                node = list(map(int, input("node> ").split()))
                print("insert> "+str(node).replace(",","").replace("[","").replace("]",""))
                for i in node:
                    tree.addNode(i)
        