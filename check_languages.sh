#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# List of languages and their respective commands
languages=(
    "python3"
    "node"
    "javac"
    "gcc"
    "g++"
    "mono"
    "ruby"
    "php"
    "perl"
    "swift"
    "kotlinc"
    "go"
    "rustc"
    "ghc"
    "bash"
    "Rscript"
    "matlab"
    "julia"
    "tsc"
)

# Check each language
for lang in "${languages[@]}"; do
    if command_exists "$lang"; then
        echo "$lang is installed."
    else
        echo "$lang is not installed."
    fi
done
