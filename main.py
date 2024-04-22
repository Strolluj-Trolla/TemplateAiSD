import sys
from sortingAlgorithms import insertionSort as ins
from sortingAlgorithms import shellSort as shell
from sortingAlgorithms import quickSortLeft as qsl
from sortingAlgorithms import quickSortRand as qsr
from sortingAlgorithms import heapSort as heap
from sortingAlgorithms import selectionSort as sel


def sort_using_algorithm(data, algorithm):

    sorted_data=data
    if algorithm==1:
        ins.insertionSort(sorted_data)
    elif algorithm==2:
        shell.shellSort(sorted_data)
    elif algorithm==3:
        sel.selection_sort(sorted_data)
    elif algorithm==4:
        heap.heap_sort(sorted_data)
    elif algorithm==5:
        qsl.quickSortLeft(sorted_data,0, len(data)-1)
    elif algorithm==6:
        qsr.quickSortRand(sorted_data,0, len(data)-1)

    return sorted_data

def main():
    sys.setrecursionlimit(10000000)
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input[1:]]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm (ignored in this example)
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data[0:100])

if __name__ == "__main__":
    main()
