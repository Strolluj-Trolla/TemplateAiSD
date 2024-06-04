import hamilton
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
    print("")

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
    
    if sys.argv[1]=="--non-hamilton":
        #get nodes count
        print("Provide node count")
        response=input("nodes> ")
        if not is_number(response):
            print("Invalid type.")
            sys.exit(2)
        node_count = int(response)

    #display instructions
    help()
    #main loop
    while True:
        response=input(">")

        if response=="Exit":
            break

        if response=="Help":
            help()

        if response=="Non-hamilton":
            graph = hamilton.generate_non_hamiltonian_graph(node_count)
        
        if response=="Print":
            print(graph)


sys.exit(0)