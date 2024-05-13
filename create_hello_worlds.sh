#!/bin/bash

# Create a directory for the hello world files
mkdir -p HelloLanguages
cd HelloLanguages

# Create the "Hello, World!" files for various programming languages

# Python
echo 'print("Hello, World!")' > hello.py

# JavaScript (Node.js)
echo 'console.log("Hello, World!");' > hello.js

# Java
cat <<EOL > Hello.java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
EOL

# C
cat <<EOL > hello.c
#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}
EOL

# C++
cat <<EOL > hello.cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
EOL

# C#
cat <<EOL > Hello.cs
using System;

class Hello {
    static void Main() {
        Console.WriteLine("Hello, World!");
    }
}
EOL

# Ruby
echo 'puts "Hello, World!"' > hello.rb

# PHP
echo '<?php echo "Hello, World!"; ?>' > hello.php

# Perl
echo 'print "Hello, World!\n";' > hello.pl

# Swift
echo 'print("Hello, World!")' > hello.swift

# Kotlin
cat <<EOL > hello.kt
fun main() {
    println("Hello, World!")
}
EOL

# Go
cat <<EOL > hello.go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
EOL

# Rust
cat <<EOL > hello.rs
fn main() {
    println!("Hello, World!");
}
EOL

# Haskell
echo 'main = putStrLn "Hello, World!"' > hello.hs

# Bash
echo 'echo "Hello, World!"' > hello.sh

# R
echo 'print("Hello, World!")' > hello.R

# MATLAB
echo 'disp(''Hello, World!'');' > hello.m

# Julia
echo 'println("Hello, World!")' > hello.jl

# TypeScript
echo 'console.log("Hello, World!");' > hello.ts

# Summary
echo "All 'Hello, World!' files have been created in the HelloLanguages directory."

# Make the Bash script executable
chmod +x hello.sh
