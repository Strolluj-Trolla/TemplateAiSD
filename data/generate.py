# Set the sizes for the arrays
sizes = [x for x in range(1, 101)]
saturations = [x for x in range(5, 101, 5)]
types = ["matrix" , "list", "table"]

for type in types:
    for size in sizes:
        for saturation in saturations:
            # Add instance size as the first number and save arrays to files
            with open(f'benchmark/{type}_{size:08d}_{saturation:03d}.txt', "w") as file:
                file.write(str(type)+"\n")
                file.write(str(size)+"\n")
                file.write(str(saturation)+"\n")
                file.write("\nFind\n1\n"+str(size)+"\nKahn\nTarjan\n\nExit\n")



print("Arrays have been generated and saved to files.")