#Remember to pip3 install numpy
import numpy as np

def generate_increasing_array(size):
    return np.arange(size)

# Set the sizes for the arrays
sizes = [100*x for x in range(1, 101)]

for size in sizes:
    # Generate arrays
    increasing_array = generate_increasing_array(size)

    # Add instance size as the first number and save arrays to files
    with open(f'benchmark/increasing_array_{size:08d}.txt', "w") as file:
        for num in increasing_array:
            file.write(str(num)+" ")
        file.write("\nMin\nMax\nPrint\nRebalance\nExit\n")



print("Arrays have been generated and saved to files.")
