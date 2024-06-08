#!/bin/bash

# Function to run the script
benchmark() {
    input_file=$1
    type=$2
    # List of supported languages and their run commands
    runpython="python3 ../main.py"
    runcurrent=$runpython

    echo "Benchmarking with input $input_file"
    #${runcurrent} --tree BST < $input_file 2>&1 >/dev/null
    ${runcurrent} $type < $input_file 2>&1 >/dev/null
    echo "------------------------"
}

# List of input file types
graph_types=("--hamilton" "--non-hamilton")

# Create or clear the CSV file
python3 ../bench_reset.py

# Run the benchmark for each input file and size
for graph_type in "${graph_types[@]}"; do
    for input_file in "benchmark/"*".txt"; do
        benchmark $input_file $graph_type
        benchmark $input_file $graph_type
        benchmark $input_file $graph_type
        benchmark $input_file $graph_type
        benchmark $input_file $graph_type
        benchmark $input_file $graph_type
        benchmark $input_file $graph_type
        benchmark $input_file $graph_type
        benchmark $input_file $graph_type
        benchmark $input_file $graph_type
    done
done