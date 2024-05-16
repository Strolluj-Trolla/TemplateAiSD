#!/bin/bash

# Function to run the script
benchmark() {
    input_file=$1
    # List of supported languages and their run commands
    runpython="python3 ../main.py"
    runcurrent=$runpython

    echo "Benchmarking with input $input_file"
    #${runcurrent} --tree BST < $input_file 2>&1 >/dev/null
    ${runcurrent} --generate < $input_file 2>&1 >/dev/null
    echo "------------------------"
}

# List of input file types
input_files=("generate")

# Create or clear the CSV file
python3 ../bench_reset.py

# Run the benchmark for each input file and size
for input_type in "${input_files[@]}"; do
    for input_file in "benchmark/"*".txt"; do
        benchmark $input_file
        benchmark $input_file
        benchmark $input_file
        benchmark $input_file
        benchmark $input_file
        benchmark $input_file
        benchmark $input_file
        benchmark $input_file
        benchmark $input_file
        benchmark $input_file
    done
done