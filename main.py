import hamilton
import sys
import copy
from time import time

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
        response=input("saturation> ")
        if int(response) not in [30 ,70]:
            print("Invalid type.")
            sys.exit(2)
        response=int(response)
        saturation=response

        graph = hamilton.gen_Hamiltonian_graph(node_count, saturation)
    
    if sys.argv[1]=="--non-hamilton":
        #get nodes count
        response=input("nodes> ")
        if not is_number(response):
            print("Invalid type.")
            sys.exit(2)
        node_count = int(response)

        graph = hamilton.generate_non_hamiltonian_graph(node_count)

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
            print(hamilton.Hcycle(graph, node_count, visited, Visited_vert, current_path))

        if response=="Euler":
            #Visited_vert = [False] * node_count
            #visited = 0
            #current_path = []
            tmp = copy.deepcopy(graph)
            print(hamilton.euler(tmp, 0, [], node_count))

sys.exit(0)