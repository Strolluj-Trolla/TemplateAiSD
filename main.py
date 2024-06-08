from hamilton import graph
import sys
import copy
#from time import time

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def help():
    print("Available instructions:")
    print("Help - display this information;")
    print("Print - print the graph;")
    print("Hamiltonian - find and print a hamiltonian path, if it exists;")
    print("Euler - find and print a Euler path, if it exists;")
    print("Exit - exit the program.")

# Checks if the Python script is being run as the main program (not imported as a module)
if __name__ == "__main__":

    #check arguments
    if len(sys.argv)<2 or not sys.argv[1] in ["--hamilton", "--non-hamilton"]:
        print("Usage: main.py --hamilton or main.py --non-hamilton")
        sys.exit(1)

    graph = graph()
    sys.setrecursionlimit(10**7)
    if sys.argv[1]=="--hamilton":
        #get nodes count
        print("Provide node count")
        response=input("nodes> ")
        if not is_number(response):
            print("Invalid type.")
            sys.exit(2)
        node_count = int(response)

        #get saturation
        response=input("saturation(30 or 70)> ")
        if int(response) not in [30 ,70]:
            print("Invalid type or unsupported value.")
            sys.exit(2)
        response=int(response)
        saturation=response

        if (graph.gen_Hamiltonian_graph(node_count, saturation)==-1):
            sys.exit(3)
    
    if sys.argv[1]=="--non-hamilton":
        #get nodes count
        response=input("nodes> ")
        if not is_number(response):
            print("Invalid type.")
            sys.exit(2)
        node_count = int(response)

        if (graph.generate_non_hamiltonian_graph(node_count)==-1):
            sys.exit(3)

    #display instructions
    help()
    #main loop
    while True:
        response=input(">")

        if response=="Exit":
            break

        if response=="Help":
            help()
        
        if response=="Print":
            print(graph)

        if response=="Hamiltonian":
            Visited_vert = [False] * node_count
            visited = 0
            current_path = []
            print(graph.Hcycle(node_count, visited, Visited_vert, current_path))

        if response=="Euler":
            tmp = copy.deepcopy(graph.matrix)
            print(graph.euler(tmp, 0, [], node_count))

sys.exit(0)