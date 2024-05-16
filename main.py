import graph
import sys
from time import time

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def help():
    print("")
    print("Menu instructions:")
    print("Help | display these instructions.")
    print("Print | Display graph in the chosen representation.")
    print("Find | Check whether a given edge exists in the graph.")
    print("Breadth-first search | traverse the graph using breadth-first search.")
    print("Depth-first search | traverse the graph using depth-first search.")
    print("Kahn | Sort the graph topologically using Kahn's algorithm.")
    print("Tarjan | Sort the graph topologically using Tarjan's algorithm.")
    print("Exit | Sort the program.")
    print("")

# Checks if the Python script is being run as the main program (not imported as a module)
if __name__ == "__main__":

    #check arguments
    if len(sys.argv)<2 or not sys.argv[1] in ["--generate", "--user-provided"]:
        print("Usage: main.py --generate or main.py --user-provided")
        sys.exit(1)

    sys.setrecursionlimit(10**7)
    
    #create graph
    print("Graph types: matrix, list, table")
    response=input("Type> ")
    if response not in ["matrix", "list", "table"]:
        print("Invalid type.")
        sys.exit(2)
    graf=graph.graph(response)

    #get node count
    response=input("Nodes> ")
    if not is_number(response):
        print("Invalid type.")
        sys.exit(2)
    response=int(response)
    nodeCount=response

    #fill graph
    if sys.argv[1]=="--generate":
        sat=input("Saturation[0-100]> ")
        if not is_number(sat):
            print("Saturation value must be an integer.")
            sys.exit(2)
        sat=int(sat)
        if sat<0 or sat>100:
            print("Saturation value must be between 0 and 100.")
            sys.exit(2)
        graf.generate(nodeCount, sat)
    else:
        sat=0
        print("Input successors for the specified nodes:")
        data=[]
        for i in range(response):
            successors=input(str(i+1)+"> ")
            try:
                successors=[int(x)-1 for x in successors]
            except:
                print("Invalid data.")
                sys.exit(2)
            data.append(successors)
        graf.dataProvided(data)
    

    #display instructions
    help()
    #main loop
    while True:
        response=input(">")

        if response=="Exit":
            break

        if response=="Help":
            help()

        if response=="Find":
            start=input("Start>")
            if not is_number(start):
                print("Start must be a node number")
                sys.exit(2)
            start=int(start)-1
            if start<0 or start>=nodeCount:
                print("Node number out of range")
                sys.exit(2)
            end=input("End>")
            if not is_number(end):
                print("End must be a node number")
                sys.exit(2)
            end=int(end)-1
            if end<0 or end>=nodeCount:
                print("Node number out of range")
                sys.exit(2)
            timeElapsed=time()
            print(str(graf.edgeExists(start, end)))
            timeElapsed=time()-timeElapsed
            with open("./find_edge.csv", "a") as res:
                res.write(graf.type+", "+str(nodeCount)+", "+str(sat)+", "+str(timeElapsed)+"\n")

        if response=="Print":
            print(str(graf))
        
        if response=="Breadth-first search":
            print(str(graf.BFS()).replace("[", "").replace("]", ""))

        if response=="Depth-first search":
            print(str(graf.DFS()).replace("[", "").replace("]", ""))
    
        if response=="Kahn":
            timeElapsed=time()
            graf.Kahn(nodeCount)
            timeElapsed=time()-timeElapsed
            with open("./sort_Kahn.csv", "a") as res:
                res.write(graf.type+", "+str(nodeCount)+", "+str(sat)+", "+str(timeElapsed)+"\n")

        if response=="Tarjan":
            timeElapsed=time()
            graf.Tarjan(nodeCount)
            timeElapsed=time()-timeElapsed
            with open("./sort_Tarjan.csv", "a") as res:
                res.write(graf.type+", "+str(nodeCount)+", "+str(sat)+", "+str(timeElapsed)+"\n")

sys.exit(0)