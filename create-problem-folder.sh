#!/bin/bash

# Check if a number is provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <number> [path]"
    exit 1
fi

number=$1
path=${2:-"./leetcode"}

# Construct the folder name and path
folder_name="$number"
folder_path="$path/$folder_name"

# Create the folder
mkdir -p "$folder_path"

# Create the files
touch "$folder_path/solution.py"
touch "$folder_path/problem.md"
touch "$folder_path/solution.md"

echo "Folder and files created at $folder_path"

git add $folder_path
