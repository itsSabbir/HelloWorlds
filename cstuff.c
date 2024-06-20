#include <stdio.h>   // Include standard I/O library
#include <stdlib.h>  // Include standard library for memory allocation and process control
#include <string.h>  // Include string library for string manipulation functions
#include <stdbool.h> // Include boolean library for boolean data type (C99 and later)
#include <limits.h>  // Include limits library for maximum and minimum values of data types
#include <float.h>   // Include float library for floating-point constants and limits
#include <ctype.h>   // Include character type library for character handling functions
#include <math.h>    // Include math library for mathematical functions
#include <assert.h>  // Include assertion library for runtime assertions
#include <time.h>    // Include time library for date and time functions

/* Function Prototypes */
int multiply(int a, int b);
void demonstratePointers();
void manipulateStrings();
void dynamicMemory();
void fileIOOperations();
void controlStructures();
void inputOutput();
void preprocessorDirectives();
void dataStructures();
void bitManipulation();
void miscellaneousConcepts();

/* Main function: Entry point of any C program */
int main() {
    printf("Welcome to the Complete C Programming Crash Course!\n");

    /* Basic Data Types */
    // Integers are fundamental data types in C used for numerical operations.
    int integerVar = 10;
    // Floats and doubles are used for floating-point arithmetic. Double has double the precision of float.
    float floatVar = 10.5f; // Use 'f' suffix for float literals
    double doubleVar = 3.14;
    // Characters typically represent single characters or ASCII values.
    char charVar = 'C';
    // Boolean data type (bool) introduced in C99 to explicitly evaluate true or false conditions.
    bool boolVar = true; 

    printf("Data Types - Integer: %d, Float: %.2f, Double: %.2lf, Char: %c, Boolean: %d\n",
           integerVar, floatVar, doubleVar, charVar, boolVar);

    /* Operators */
    // Demonstrating basic arithmetic operators and their use in expressions.
    printf("Operators - Sum: %d, Division: %.2f\n", integerVar + 5, floatVar / 2.0f);

    // Logical operators: && (AND), || (OR), ! (NOT)
    bool result = (integerVar > 5) && (floatVar < 20.0f);
    printf("Logical Operators - Result: %d\n", result);

    // Bitwise operators: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)
    int x = 10;     // Binary: 1010
    int y = 6;      // Binary: 0110
    int bitwise = x & y;
    printf("Bitwise Operators - Result: %d\n", bitwise); // Output: 2 (Binary: 0010)

    /* Control Structures */
    controlStructures();

    /* Arrays */
    // Arrays are used to store multiple values of the same type in a single variable.
    int array[5] = {1, 2, 3, 4, 5};
    printf("Array - First element: %d, Last element: %d\n", array[0], array[4]);

    // Multidimensional arrays
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    printf("Multidimensional Array - Element at (1, 1): %d\n", matrix[1][1]);

    /* Functions */
    // Demonstrating a simple function that multiplies two numbers.
    printf("Function - Multiply 5 by 3: %d\n", multiply(5, 3));

    /* Pointers and Memory Management */
    // Pointers are used to store the address of variables, which allows for dynamic memory management and array handling.
    demonstratePointers();

    /* String Manipulation */
    // Strings in C are arrays of characters terminated by a null character. String functions provide various utilities for string manipulation.
    manipulateStrings();

    /* Dynamic Memory Allocation */
    // Dynamic memory management allows the program to obtain memory during runtime which is crucial for programs with variable memory needs.
    dynamicMemory();

    /* File I/O */
    // File operations in C are used to store or retrieve data to/from files, enabling data persistence beyond the program execution.
    fileIOOperations();

    /* Input and Output */
    inputOutput();

    /* Preprocessor Directives */
    preprocessorDirectives();

    /* Data Structures */
    dataStructures();

    /* Bit Manipulation */
    bitManipulation();

    /* Miscellaneous Concepts */
    miscellaneousConcepts();

    return 0;
}

/* Function Definitions */

int multiply(int a, int b) {
    return a * b; // Simply multiplies two integers and returns the result.
}

void demonstratePointers() {
    int val = 20;
    int *ptr = &val; // Pointer to the integer variable val.
    printf("Pointer - Address: %p, Value: %d\n", (void *)ptr, *ptr); // Demonstrating how to access a pointer and the value to which it points.

    // Pointer arithmetic
    ptr++; // Increment the pointer by the size of the data type it points to
    printf("Pointer Arithmetic - Address after increment: %p\n", (void *)ptr);

    // Pointer to pointer (double pointer)
    int **doublePtr = &ptr;
    printf("Double Pointer - Address: %p, Value: %p\n", (void *)doublePtr, (void *)*doublePtr);
}

void manipulateStrings() {
    char str1[20] = "Hello";
    char str2[20] = "World";
    strcat(str1, str2); // Concatenating two strings.
    printf("Strings - Concatenate: %s\n", str1); // Output the result of the concatenation.

    // String comparison
    int result = strcmp(str1, "HelloWorld");
    printf("String Comparison - Result: %d\n", result); // Output: 0 (strings are equal)

    // String copying
    char str3[20];
    strcpy(str3, str1);
    printf("String Copy - str3: %s\n", str3);

    // String length
    int length = strlen(str1);
    printf("String Length - Length of str1: %d\n", length);
}

void dynamicMemory() {
    int *arr = (int *)malloc(5 * sizeof(int)); // Allocating memory dynamically for an array of 5 integers.
    if (arr == NULL) { // Always check if malloc succeeded.
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < 5; i++) {
        arr[i] = i * i; // Initializing array elements.
    }
    printf("Dynamic Memory - First element: %d\n", arr[0]); // Accessing the first element.

    // Reallocating memory
    arr = (int *)realloc(arr, 10 * sizeof(int)); // Resizing the array to hold 10 integers.
    if (arr == NULL) {
        fprintf(stderr, "Memory reallocation failed\n");
        exit(EXIT_FAILURE);
    }
    printf("Dynamic Memory - Size after reallocation: %zu\n", 10 * sizeof(int));

    free(arr); // It's crucial to free dynamically allocated memory to avoid memory leaks.
}

void fileIOOperations() {
    FILE *file = fopen("example.txt", "w+"); // Opening a file for reading and writing.
    if (file == NULL) {
        printf("File I/O - Failed to open file!\n");
        return;
    }
    fprintf(file, "Hello, file!\n"); // Writing to a file.
    fclose(file); // Closing the file to flush the buffer and release resources.

    char buffer[100];
    file = fopen("example.txt", "r"); // Re-opening the file for reading.
    if (fgets(buffer, sizeof(buffer), file)) { // Reading a line from the file.
        printf("File I/O - Read from file: %s", buffer);
    } else {
        printf("File I/O - Failed to read from file!\n");
    }
    fclose(file); // Closing the file.

    // Binary file I/O
    int data = 42;
    FILE *binFile = fopen("data.bin", "wb");
    fwrite(&data, sizeof(int), 1, binFile); // Writing binary data to a file.
    fclose(binFile);

    binFile = fopen("data.bin", "rb");
    int readData;
    fread(&readData, sizeof(int), 1, binFile); // Reading binary data from a file.
    printf("Binary File I/O - Read data: %d\n", readData);
    fclose(binFile);
}

void controlStructures() {
    /* If-else conditionals are used to direct flow based on comparisons. */
    int integerVar = 10;
    if (integerVar == 10) {
        printf("If-else structure: Integer is 10\n");
    } else {
        printf("If-else structure: Integer is not 10\n");
    }

    // Ternary operator: (condition) ? (if true) : (if false)
    char *result = (integerVar == 10) ? "Equal" : "Not Equal";
    printf("Ternary Operator - Result: %s\n", result);

    /* Switch statement: Used for multi-way branching based on a single variable. */
    int choice = 2;
    switch (choice) {
        case 1:
            printf("Switch Statement - Choice is 1\n");
            break;
        case 2:
            printf("Switch Statement - Choice is 2\n");
            break;
        default:
            printf("Switch Statement - Invalid choice\n");
            break;
    }

    /* For loops provide a mechanism to iterate over a block of code multiple times. */
    for (int i = 0; i < 5; i++) {
        printf("For loop: i = %d\n", i);
    }

    /* While loops: Execute a block of code while a condition is true. */
    int count = 0;
    while (count < 3) {
        printf("While loop: count = %d\n", count);
        count++;
    }

    /* Do-while loops: Similar to while loops, but the block of code is executed at least once. */
    int doWhileCount = 0;
    do {
        printf("Do-while loop: doWhileCount = %d\n", doWhileCount);
        doWhileCount++;
    } while (doWhileCount < 3);
}

void inputOutput() {
    /* printf: Used for formatted output to the console. */
    int value = 42;
    printf("Input/Output - Value: %d\n", value);

    /* scanf: Used for reading formatted input from the console. */
    int inputValue;
    printf("Enter an integer: ");
    scanf("%d", &inputValue);
    printf("Input/Output - Entered value: %d\n", inputValue);

    /* getchar and putchar: Used for reading and writing single characters. */
    char ch;
    printf("Enter a character: ");
    ch = getchar();
    printf("Input/Output - Entered character: ");
    putchar(ch);
    printf("\n");

    /* fgets and fputs: Used for reading and writing strings from/to files or console. */
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    printf("Input/Output - Entered string: ");
    fputs(str, stdout);
}

void preprocessorDirectives() {
    /* #define: Used for defining constants or macros. */
    #define PI 3.14159
    #define SQUARE(x) ((x) * (x))
    printf("Preprocessor Directives - PI: %.5f\n", PI);
    printf("Preprocessor Directives - Square of 5: %d\n", SQUARE(5));

    /* Conditional compilation: Used for including or excluding code blocks based on conditions. */
    #ifdef DEBUG
        printf("Debug mode is enabled.\n");
    #else
        printf("Debug mode is disabled.\n");
    #endif

    /* #include: Used for including header files. */
    // #include statements are typically placed at the top of the file.
}

void dataStructures() {
    /* Structures: Used for grouping related data items of different types. */
    struct Person {
        char name[50];
        int age;
        float height;
    };

    struct Person person1 = {"John Doe", 30, 1.75};
    printf("Data Structures - Person: %s, %d, %.2f\n", person1.name, person1.age, person1.height);

    /* Unions: Used for storing different data types in the same memory location. */
    union Data {
        int intValue;
        float floatValue;
        char charValue;
    };

    union Data data;
    data.intValue = 42;
    printf("Data Structures - Union: %d\n", data.intValue);
    data.floatValue = 3.14;
    printf("Data Structures - Union: %.2f\n", data.floatValue);

    /* Enumerations: Used for defining named constants. */
    enum DaysOfWeek {
        MONDAY,
        TUESDAY,
        WEDNESDAY,
        THURSDAY,
        FRIDAY,
        SATURDAY,
        SUNDAY
    };

    enum DaysOfWeek today = WEDNESDAY;
    printf("Data Structures - Today is day %d\n", today);
}

void bitManipulation() {
    /* Bitwise operators: Used for manipulating individual bits of integer values. */
    unsigned int a = 5;  // Binary: 0101
    unsigned int b = 12; // Binary: 1100

    unsigned int andResult = a & b;    // Binary: 0100
    unsigned int orResult = a | b;     // Binary: 1101
    unsigned int xorResult = a ^ b;    // Binary: 1001
    unsigned int notResult = ~a;       // Binary: 1111...1010
    unsigned int leftShift = a << 2;   // Binary: 0001 0100
    unsigned int rightShift = b >> 1;  // Binary: 0110

    printf("Bit Manipulation - AND: %u, OR: %u, XOR: %u, NOT: %u, Left Shift: %u, Right Shift: %u\n",
           andResult, orResult, xorResult, notResult, leftShift, rightShift);

    /* Bitwise assignment operators: Used for performing bitwise operations and assigning the result to a variable. */
    unsigned int x = 10; // Binary: 1010
    x &= 7;  // Binary: 0111
    printf("Bit Manipulation - AND assignment: %u\n", x);

    x |= 3;  // Binary: 0011
    printf("Bit Manipulation - OR assignment: %u\n", x);

    x ^= 5;  // Binary: 0101
    printf("Bit Manipulation - XOR assignment: %u\n", x);

    x <<= 1; // Binary: 1010
    printf("Bit Manipulation - Left shift assignment: %u\n", x);

    x >>= 2; // Binary: 0010
    printf("Bit Manipulation - Right shift assignment: %u\n", x);
}

void miscellaneousConcepts() {
    /* Type casting: Used for explicitly converting one data type to another. */
    int intValue = 10;
    float floatValue = (float)intValue;
    printf("Miscellaneous Concepts - Float value after casting: %.2f\n", floatValue);

    /* sizeof operator: Used for determining the size (in bytes) of a data type or variable. */
    printf("Miscellaneous Concepts - Size of int: %zu bytes\n", sizeof(int));

    /* Volatile keyword: Used for variables that may be modified by external factors, preventing compiler optimizations. */
    volatile int volatileVar = 10;
    printf("Miscellaneous Concepts - Volatile variable: %d\n", volatileVar);

    /* const keyword: Used for defining variables whose values cannot be modified. */
    const int MAX_VALUE = 100;
    printf("Miscellaneous Concepts - Constant value: %d\n", MAX_VALUE);

    /* typedef keyword: Used for creating aliases for existing data types. */
    typedef unsigned long long ULL;
    ULL largeValue = 1234567890ULL;
    printf("Miscellaneous Concepts - Large value using typedef: %llu\n", largeValue);

    /* Static variables: Used for variables that retain their values between function calls. */
    static int staticVar = 0;
    staticVar++;
    printf("Miscellaneous Concepts - Static variable: %d\n", staticVar);

    /* Recursion: A function that calls itself until a base case is reached. */
    int factorial = 5;
    int result = recursiveFactorial(factorial);
    printf("Miscellaneous Concepts - Factorial of %d: %d\n", factorial, result);

    /* Command-line arguments: Accessing arguments passed to the program from the command line. */
    // int main(int argc, char *argv[]) {
    //     printf("Miscellaneous Concepts - Number of command-line arguments: %d\n", argc);
    //     for (int i = 0; i < argc; i++) {
    //         printf("Argument %d: %s\n", i, argv[i]);
    //     }
    //     return 0;
    // }
}

int recursiveFactorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * recursiveFactorial(n - 1);
    }
}