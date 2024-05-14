#include <stdio.h>   // Include standard I/O library
#include <stdlib.h>  // Include standard library for memory allocation and process control
#include <string.h>  // Include string library for string manipulation functions

/* Function Prototypes */
int multiply(int a, int b);
void demonstratePointers();
void manipulateStrings();
void dynamicMemory();
void fileIOOperations();

/* Main function: Entry point of any C program */
int main() {
    printf("Welcome to the Complete C Programming Crash Course!\n");

    /* Basic Data Types */
    // Integers are fundamental data types in C used for numerical operations.
    int integerVar = 10;
    // Floats and doubles are used for floating-point arithmetic. Double has double the precision of float.
    float floatVar = 10.5;
    double doubleVar = 3.14;
    // Characters typically represent single characters or ASCII values.
    char charVar = 'C';
    // Boolean data type (_Bool) introduced in C99 to explicitly evaluate true or false conditions.
    _Bool boolVar = 1; 

    printf("Data Types - Integer: %d, Float: %f, Double: %f, Char: %c, Boolean: %d\n",
           integerVar, floatVar, doubleVar, charVar, boolVar);

    /* Operators */
    // Demonstrating basic arithmetic operators and their use in expressions.
    printf("Operators - Sum: %d, Division: %f\n", integerVar + 5, floatVar / 2.0);

    /* Control Structures */
    // If-else conditionals are used to direct flow based on comparisons.
    if (integerVar == 10) {
        printf("If-else structure: Integer is 10\n");
    } else {
        printf("If-else structure: Integer is not 10\n");
    }

    // For loops provide a mechanism to iterate over a block of code multiple times.
    for (int i = 0; i < 5; i++) {
        printf("For loop: i = %d\n", i);
    }

    /* Arrays */
    // Arrays are used to store multiple values of the same type in a single variable.
    int array[5] = {1, 2, 3, 4, 5};
    printf("Array - First element: %d, Last element: %d\n", array[0], array[4]);

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
}

void manipulateStrings() {
    char str1[20] = "Hello";
    char str2[20] = "World";
    strcat(str1, str2); // Concatenating two strings.
    printf("Strings - Concatenate: %s\n", str1); // Output the result of the concatenation.
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
}
