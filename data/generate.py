# Set the sizes for the arrays
sizes = [x for x in range(11, 31)]

for size in sizes:
    with open(f'benchmark/generate_{size:08d}.txt', "w") as file:
        file.write(str(size)+"\n")
        file.write("70\nHamiltonian\nEuler\nExit\n")



print("Arrays have been generated and saved to files.")