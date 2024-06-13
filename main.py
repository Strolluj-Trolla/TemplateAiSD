import time
import sys
from plecak import plecak


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def save_time(startTime :float, size: int, isHamilton: bool, filename :str) -> None:
    timeElapsed = time()-startTime
    if isHamilton:
        filename+="_Hamilton.csv"
    else:
        filename+="_non_Hamilton.csv"
    with open(filename, "a") as file:
        file.write(str(size)+", "+str(timeElapsed)+"\n")
    return


def help():
    print("Available instructions:")
    print("Help - display this information;")
    print("Print - print the problem's parameters;")
    print("Dynamic - solve using dynamic programming;")
    print("Greedy - solve using a greedy algorythm;")
    print("Brute-force - solve using brute force;")
    print("Exit - exit the program.")
    print("")

# Checks if the Python script is being run as the main program (not imported as a module)
if __name__ == "__main__":

    #check arguments
    if len(sys.argv)<2 or not sys.argv[1] in ["--keyboard", "--file", "--random"]:
        print("Usage: main.py --keyboard or main.py --random")
        sys.exit(1)

    
    sys.setrecursionlimit(10**7)

    backpack = plecak()

    if sys.argv[1]=="--keyboard":
        backpack.from_input()
    
    if sys.argv[1]=="--random":
        n=input("Number of elements>")
        if is_number(n):
            n=int(n)
        else:
            print("Invalid value")
            sys.exit(5)
        c=input("Capacity>")
        if is_number(c):
            c=int(c)
        else:
            print("Invalid value")
            sys.exit(5)
        backpack.gen(n,c)

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
            print(backpack)

        if response=="Dynamic":
            solution, weight, value=backpack.dynamic()
            print("Packed elements: "+str(solution).replace("[","").replace("]","").replace(",", "")+"; weight: "+str(weight)+"; value: "+str(value)+".")

        if response=="Greedy":
            solution, weight, value=backpack.greedy()
            print("Packed elements: "+str(solution).replace("[","").replace("]","").replace(",", "")+"; weight: "+str(weight)+"; value: "+str(value)+".")

        if response=="Brute-force":
            solution, weight, value=backpack.dynamic()
            print("Packed elements: "+str(solution).replace("[","").replace("]","").replace(",", "")+"; weight: "+str(weight)+"; value: "+str(value)+".")

sys.exit(0)
