#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install a package using Homebrew
install_with_brew() {
    if command_exists brew; then
        echo "Installing $1..."
        brew install "$1"
    else
        echo "Homebrew is not installed. Please install Homebrew first."
        exit 1
    fi
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

# Corresponding brew packages
brew_packages=(
    "python"
    "node"
    "openjdk"
    "gcc"
    "gcc"
    "mono"
    "ruby"
    "php"
    "perl"
    "swift"
    "kotlin"
    "go"
    "rust"
    "ghc"
    "bash"
    "r"
    ""
    "julia"
    "typescript"
)

# Check each language
for i in "${!languages[@]}"; do
    lang="${languages[$i]}"
    brew_package="${brew_packages[$i]}"
    if command_exists "$lang"; then
        echo "$lang is already installed."
    else
        echo "$lang is not installed."
        if [ -n "$brew_package" ]; then
            install_with_brew "$brew_package"
        else
            echo "No installation method for $lang. Please install it manually."
        fi
    fi
done

echo "All required languages are installed or already present."

# Additional checks for specific languages
if ! command_exists "matlab"; then
    echo "MATLAB is not installed. Please install MATLAB manually from the MathWorks website."
fi
