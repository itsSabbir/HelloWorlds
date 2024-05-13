# Hello World Scripts

This repository contains "Hello, World!" scripts written in various programming languages. It also includes shell scripts to check the installation of these languages and to create the "Hello, World!" scripts in a directory. The goal is to ensure that your development environment is correctly set up regardless of the operating system.

## Directory Structure

```
hello_world/
|-- check_languages.sh
|-- create_hello_worlds.sh
|-- setup_langauges.sh
|-- hello.c
|-- hello.cpp
|-- Hello.cs
|-- hello.go
|-- hello.hs
|-- Hello.java
|-- hello.jl
|-- hello.js
|-- hello.kt
|-- hello.m
|-- hello.php
|-- hello.pl
|-- hello.py
|-- hello.R
|-- hello.rb
|-- hello.rs
|-- hello.sh
|-- hello.swift
|-- hello.ts
|-- LICENSE
```

## Shell Scripts

### `check_languages.sh`

This script checks if the required programming languages are installed on your system.

**Usage:**
```bash
./check_languages.sh
```

### `create_hello_worlds.sh`

This script creates "Hello, World!" files in various programming languages within a specified directory.

**Usage:**
```bash
./create_hello_worlds.sh
```

### `setup_langauges.sh`

This script checks for the presence of various programming languages on your Mac and installs the latest versions if they are not already installed.

**Usage:**
```bash
./setup_langauges.sh
```

## Hello World Scripts

The following "Hello, World!" scripts are included in this repository:

- **C**: `hello.c`
- **C++**: `hello.cpp`
- **C#**: `Hello.cs`
- **Go**: `hello.go`
- **Haskell**: `hello.hs`
- **Java**: `Hello.java`
- **Julia**: `hello.jl`
- **JavaScript (Node.js)**: `hello.js`
- **Kotlin**: `hello.kt`
- **MATLAB**: `hello.m`
- **PHP**: `hello.php`
- **Perl**: `hello.pl`
- **Python**: `hello.py`
- **R**: `hello.R`
- **Ruby**: `hello.rb`
- **Rust**: `hello.rs`
- **Shell**: `hello.sh`
- **Swift**: `hello.swift`
- **TypeScript**: `hello.ts`

## How to Run the Scripts

### C
```bash
gcc hello.c -o hello
./hello
```

### C++
```bash
g++ hello.cpp -o hello
./hello
```

### C#
```bash
mcs Hello.cs
mono Hello.exe
```

### Go
```bash
go run hello.go
```

### Haskell
```bash
runhaskell hello.hs
```

### Java
```bash
javac Hello.java
java Hello
```

### Julia
```bash
julia hello.jl
```

### JavaScript (Node.js)
```bash
node hello.js
```

### Kotlin
```bash
kotlinc hello.kt -include-runtime -d hello.jar
java -jar hello.jar
```

### MATLAB
```bash
matlab -batch "hello"
```

### PHP
```bash
php hello.php
```

### Perl
```bash
perl hello.pl
```

### Python
```bash
python3 hello.py
```

### R
```bash
Rscript hello.R
```

### Ruby
```bash
ruby hello.rb
```

### Rust
```bash
rustc hello.rs
./hello
```

### Shell
```bash
bash hello.sh
```

### Swift
```bash
swift hello.swift
```

### TypeScript
```bash
tsc hello.ts
node hello.js
```

## Contributing

Contributions are welcome! If you would like to add support for more languages or improve the existing scripts, please feel free to open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Future Plans

- Ensure compatibility across different operating systems (Linux, Windows).
- Add more programming languages and their respective "Hello, World!" scripts.
- Automate the setup process for all major operating systems.
