# Python Cheat Sheet: Data Types and Variables

# 1. Basic Data Types
# Integer: Whole numbers (positive, negative, or zero)
integer_var = 42
print(f"Integer: {integer_var}")  # Output: Integer: 42

# Float: Decimal numbers
float_var = 3.14159
print(f"Float: {float_var}")  # Output: Float: 3.14159

# String: Sequence of characters
str_var = "Hello, Python!"
print(f"String: {str_var}")  # Output: String: Hello, Python!

# Boolean: True or False
bool_var = True
print(f"Boolean: {bool_var}")  # Output: Boolean: True

# NoneType: Represents absence of a value
none_var = None
print(f"NoneType: {none_var}")  # Output: NoneType: None

# Tip: Use type() function to check the type of a variable
print(type(integer_var))  # Output: <class 'int'>

# 2. Type Conversion and Casting
# Converting between types
str_to_int = int("42")
float_to_int = int(3.14)
int_to_float = float(42)
int_to_str = str(42)

# Tip: Be careful when converting floats to integers, as it truncates the decimal part
print(int(3.9))  # Output: 3

# 3. Mutable vs Immutable Data Types
# Immutable: int, float, str, tuple
# Mutable: list, dict, set

# Immutable example (string)
immutable_str = "Hello"
# immutable_str[0] = "h"  # This would raise a TypeError

# Mutable example (list)
mutable_list = [1, 2, 3]
mutable_list[0] = 4  # This is allowed
print(mutable_list)  # Output: [4, 2, 3]

# Tip: Use id() to check if the object's identity changes
original_id = id(mutable_list)
mutable_list.append(5)
new_id = id(mutable_list)
print(original_id == new_id)  # Output: True (same object, mutable)

original_id = id(immutable_str)
immutable_str += " World"
new_id = id(immutable_str)
print(original_id == new_id)  # Output: False (new object created, immutable)

# 4. Complex Numbers
complex_var = 2 + 3j
print(f"Complex: {complex_var}")  # Output: Complex: (2+3j)
print(f"Real part: {complex_var.real}, Imaginary part: {complex_var.imag}")

# 5. Variables
# Python uses dynamic typing
x = 5
x = "Now I'm a string"
print(x)  # Output: Now I'm a string

# Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)  # Output: 1 2 3

# Swapping variables
a, b = b, a
print(a, b)  # Output: 2 1

# 6. Constants
# Python doesn't have built-in constant types, but it's a convention to use
# uppercase names for constants
PI = 3.14159
MAX_SIZE = 100

# 7. String Operations
# Concatenation
greeting = "Hello" + " " + "World"
print(greeting)  # Output: Hello World

# Repetition
repeated = "Python " * 3
print(repeated)  # Output: Python Python Python

# Indexing and Slicing
text = "Python"
print(text[0])    # Output: P
print(text[-1])   # Output: n
print(text[1:4])  # Output: yth

# String formatting
name = "Alice"
age = 30
print(f"{name} is {age} years old")  # Output: Alice is 30 years old

# 8. Type Hints (Python 3.5+)
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Tip: Type hints are not enforced at runtime, they're for documentation and tooling

# 9. Memory Management
# Python uses reference counting and garbage collection
# del statement can be used to delete references
x = 42
del x
# print(x)  # This would raise a NameError

# Tip: Use sys.getsizeof() to check the memory size of an object
import sys
print(sys.getsizeof(int_var))  # Shows memory size of the integer object

# Python Cheat Sheet: Operators

# 1. Arithmetic Operators
a, b = 10, 3

# Addition
print(f"a + b = {a + b}")  # Output: 13

# Subtraction
print(f"a - b = {a - b}")  # Output: 7

# Multiplication
print(f"a * b = {a * b}")  # Output: 30

# Division (always returns a float)
print(f"a / b = {a / b}")  # Output: 3.3333333333333335

# Floor Division (returns the largest integer less than or equal to the result)
print(f"a // b = {a // b}")  # Output: 3

# Modulus (remainder)
print(f"a % b = {a % b}")  # Output: 1

# Exponentiation
print(f"a ** b = {a ** b}")  # Output: 1000

# Tip: Use parentheses to control the order of operations
print((a + b) * 2)  # Output: 26

# 2. Comparison Operators
x, y = 5, 10

# Equal to
print(f"x == y: {x == y}")  # Output: False

# Not equal to
print(f"x != y: {x != y}")  # Output: True

# Greater than
print(f"x > y: {x > y}")  # Output: False

# Less than
print(f"x < y: {x < y}")  # Output: True

# Greater than or equal to
print(f"x >= y: {x >= y}")  # Output: False

# Less than or equal to
print(f"x <= y: {x <= y}")  # Output: True

# Tip: Comparison operators return boolean values (True or False)

# 3. Logical Operators
p, q = True, False

# AND
print(f"p and q: {p and q}")  # Output: False

# OR
print(f"p or q: {p or q}")  # Output: True

# NOT
print(f"not p: {not p}")  # Output: False

# Tip: Logical operators are often used in conditional statements
if x < y and y < 20:
    print("Both conditions are true")

# 4. Bitwise Operators
m, n = 60, 13  # 60 = 0011 1100, 13 = 0000 1101 in binary

# Bitwise AND
print(f"m & n: {m & n}")  # Output: 12 (0000 1100)

# Bitwise OR
print(f"m | n: {m | n}")  # Output: 61 (0011 1101)

# Bitwise XOR
print(f"m ^ n: {m ^ n}")  # Output: 49 (0011 0001)

# Bitwise NOT
print(f"~m: {~m}")  # Output: -61 (1100 0011)

# Left shift
print(f"m << 2: {m << 2}")  # Output: 240 (1111 0000)

# Right shift
print(f"m >> 2: {m >> 2}")  # Output: 15 (0000 1111)

# Tip: Bitwise operators are useful for low-level operations and optimizations

# 5. Membership Operators
fruits = ["apple", "banana", "cherry"]

# in
print(f"'banana' in fruits: {'banana' in fruits}")  # Output: True

# not in
print(f"'grape' not in fruits: {'grape' not in fruits}")  # Output: True

# Tip: Membership operators work with strings, lists, tuples, and other sequences
print(f"'a' in 'apple': {'a' in 'apple'}")  # Output: True

# 6. Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# is (checks if two variables refer to the same object in memory)
print(f"list1 is list2: {list1 is list2}")  # Output: False
print(f"list1 is list3: {list1 is list3}")  # Output: True

# is not
print(f"list1 is not list2: {list1 is not list2}")  # Output: True

# Tip: 'is' compares object identity, '==' compares value
print(f"list1 == list2: {list1 == list2}")  # Output: True (same value)
print(f"list1 is list2: {list1 is list2}")  # Output: False (different objects)

# 7. Assignment Operators
a = 10

# Addition assignment
a += 5  # Equivalent to: a = a + 5
print(f"a after +=: {a}")  # Output: 15

# Subtraction assignment
a -= 3  # Equivalent to: a = a - 3
print(f"a after -=: {a}")  # Output: 12

# Multiplication assignment
a *= 2  # Equivalent to: a = a * 2
print(f"a after *=: {a}")  # Output: 24

# Division assignment
a /= 4  # Equivalent to: a = a / 4
print(f"a after /=: {a}")  # Output: 6.0

# Floor division assignment
a //= 2  # Equivalent to: a = a // 2
print(f"a after //=: {a}")  # Output: 3.0

# Modulus assignment
a %= 2  # Equivalent to: a = a % 2
print(f"a after %=: {a}")  # Output: 1.0

# Exponentiation assignment
a **= 3  # Equivalent to: a = a ** 3
print(f"a after **=: {a}")  # Output: 1.0

# Tip: Assignment operators provide a concise way to update variables

# 8. Operator Precedence
# Python follows the PEMDAS rule (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)
result = 2 + 3 * 4 ** 2 - 6 / 2
print(f"2 + 3 * 4 ** 2 - 6 / 2 = {result}")  # Output: 47.0

# Tip: Use parentheses to make your code more readable and to ensure the intended order of operations
result = ((2 + 3) * 4 ** 2) - (6 / 2)
print(f"((2 + 3) * 4 ** 2) - (6 / 2) = {result}")  # Output: 77.0

# Python Cheat Sheet: Control Structures

# 1. Conditional Statements

# if statement
x = 10
if x > 0:
    print("x is positive")  # Output: x is positive

# if-else statement
y = -5
if y > 0:
    print("y is positive")
else:
    print("y is non-positive")  # Output: y is non-positive

# if-elif-else statement
z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")  # Output: z is zero

# Ternary operator (conditional expression)
a = 5
result = "positive" if a > 0 else "non-positive"
print(result)  # Output: positive

# Tip: You can chain multiple conditions using logical operators
if x > 0 and y < 0:
    print("x is positive and y is negative")

# Tip: Be careful with indentation, it defines the block of code for each condition

# 2. Loops

# for loop with range
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
print()

# for loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")  # Output: apple banana cherry
print()

# for loop with enumerate (to get index and value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# while loop
count = 0
while count < 5:
    print(count, end=" ")
    count += 1  # Output: 0 1 2 3 4
print()

# Infinite loop (be careful!)
# while True:
#     print("This will run forever unless broken")

# 3. Loop Control

# break: exits the loop
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")  # Output: 0 1 2 3 4
print()

# continue: skips the rest of the current iteration
for i in range(5):
    if i == 2:
        continue
    print(i, end=" ")  # Output: 0 1 3 4
print()

# pass: does nothing, used as a placeholder
for i in range(3):
    pass  # This loop will run but do nothing

# Tip: 'pass' is often used when you need a syntactically correct statement but don't want to execute any code

# 4. Nested Loops

# Nested for loops
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})", end=" ")
    print()
# Output:
# (0, 0) (0, 1)
# (1, 0) (1, 1)
# (2, 0) (2, 1)

# 5. Comprehensions (compact way to create lists, sets, and dictionaries)

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0, 4, 16, 36, 64}

# Dictionary comprehension
char_count = {char: fruits.count(char) for char in "abc"}
print(char_count)  # Output: {'a': 3, 'b': 1, 'c': 1}

# 6. else clause in loops
# The else clause executes when the loop completes normally (without break)

# for-else
for i in range(5):
    if i == 10:  # This condition is never true
        break
    print(i, end=" ")
else:
    print("Loop completed normally")
# Output: 0 1 2 3 4 Loop completed normally

# while-else
count = 0
while count < 3:
    print(count, end=" ")
    count += 1
else:
    print("While loop completed normally")
# Output: 0 1 2 While loop completed normally

# Tip: The else clause in loops is rarely used but can be helpful in certain scenarios

# 7. Switch-Case Alternative (Python 3.10+)
# Python doesn't have a switch statement, but you can use match-case (structural pattern matching)

def check_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Unknown Status"

print(check_status(200))  # Output: OK
print(check_status(500))  # Output: Unknown Status

# Tip: For earlier Python versions, you can use if-elif chains or dictionaries to mimic switch-case behavior

# Python Cheat Sheet: Functions

# 1. Defining and Calling Functions

# Basic function definition
def greet(name):
    """This is a docstring. It describes what the function does."""
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))  # Output: Hello, Alice!

# Tip: Use descriptive function names and include docstrings for better code documentation

# 2. Arguments and Return Values

# Function with multiple parameters and a return value
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

# Function with multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 5, 2, 8, 3])
print(f"Min: {minimum}, Max: {maximum}")  # Output: Min: 1, Max: 8

# 3. Default Arguments

def power(base, exponent=2):
    return base ** exponent

print(power(3))     # Output: 9 (uses default exponent 2)
print(power(3, 3))  # Output: 27 (uses provided exponent 3)

# Tip: Default arguments must come after non-default arguments in the function definition

# 4. Keyword Arguments

def greet_person(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_person("Bob"))                  # Output: Hello, Bob!
print(greet_person("Charlie", "Good day"))  # Output: Good day, Charlie!
print(greet_person(greeting="Hi", name="David"))  # Output: Hi, David!

# 5. Variable-length Arguments

# *args: Variable number of positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))       # Output: 6
print(sum_all(1, 2, 3, 4, 5)) # Output: 15

# **kwargs: Variable number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

# Combining *args and **kwargs
def multi_purpose(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

multi_purpose(1, 2, 3, name="Alice", age=30)
# Output:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}

# 6. Lambda Functions

# Lambda functions are small anonymous functions
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda functions are often used with map(), filter(), and sorted()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# 7. Scopes and Namespaces

# Global scope
global_var = 10

def outer_function():
    # Enclosing scope
    enclosing_var = 20
    
    def inner_function():
        # Local scope
        local_var = 30
        print(f"Access from inner_function: global_var={global_var}, enclosing_var={enclosing_var}, local_var={local_var}")
    
    inner_function()
    print(f"Access from outer_function: global_var={global_var}, enclosing_var={enclosing_var}")

outer_function()
print(f"Access from global scope: global_var={global_var}")

# Modifying global variables
def modify_global():
    global global_var
    global_var = 100

modify_global()
print(f"Modified global_var: {global_var}")  # Output: Modified global_var: 100

# Nonlocal variables
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print(f"x from outer: {x}")  # Output: x from outer: inner

outer()

# Tip: Use global and nonlocal keywords sparingly, as they can make code harder to understand and maintain

# 8. Function Annotations (Python 3.0+)

def greet_annotated(name: str) -> str:
    return f"Hello, {name}!"

print(greet_annotated("Eve"))  # Output: Hello, Eve!
print(greet_annotated.__annotations__)  # Output: {'name': <class 'str'>, 'return': <class 'str'>}

# Tip: Annotations are metadata and don't affect the function's behavior, but they can be used for documentation and type checking tools

# 9. Recursive Functions

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Tip: Be cautious with recursive functions, as they can lead to stack overflow for large inputs

# Python Cheat Sheet: Data Collections

# 1. Lists
# Ordered, mutable, allows duplicate elements

# Creating lists
fruits = ['apple', 'banana', 'cherry']
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]

# Accessing elements
print(fruits[0])    # Output: apple
print(fruits[-1])   # Output: cherry (last element)

# Slicing
print(fruits[1:3])  # Output: ['banana', 'cherry']

# Modifying lists
fruits.append('date')        # Add to the end
fruits.insert(1, 'blueberry')  # Insert at index 1
fruits.remove('banana')      # Remove first occurrence
popped = fruits.pop()        # Remove and return last element
fruits.sort()                # Sort in place
sorted_fruits = sorted(fruits)  # Return new sorted list

# List operations
combined = fruits + numbers  # Concatenation
repeated = fruits * 2        # Repetition

# Useful list methods
print(len(fruits))           # Length of the list
print(fruits.count('apple')) # Count occurrences
print(fruits.index('cherry'))  # Find index of first occurrence

# 2. Tuples
# Ordered, immutable, allows duplicate elements

# Creating tuples
coordinates = (3, 4)
single_element = (42,)  # Comma is necessary for single-element tuples

# Accessing elements (similar to lists)
print(coordinates[0])  # Output: 3

# Tuple unpacking
x, y = coordinates
print(f"x: {x}, y: {y}")  # Output: x: 3, y: 4

# Tuples are immutable
# coordinates[0] = 5  # This would raise a TypeError

# 3. Sets
# Unordered, mutable, no duplicate elements

# Creating sets
unique_numbers = {1, 2, 3, 4, 5}
another_set = set([3, 4, 5, 6, 7])

# Set operations
union = unique_numbers | another_set
intersection = unique_numbers & another_set
difference = unique_numbers - another_set
symmetric_difference = unique_numbers ^ another_set

# Modifying sets
unique_numbers.add(6)        # Add an element
unique_numbers.remove(1)     # Remove an element (raises KeyError if not found)
unique_numbers.discard(10)   # Remove if present, do nothing if not found

# Checking membership
print(2 in unique_numbers)  # Output: True

# 4. Dictionaries
# Unordered (Python 3.7+ preserves insertion order), mutable, key-value pairs

# Creating dictionaries
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
another_dict = dict(name='Bob', age=25)

# Accessing values
print(person['name'])        # Output: Alice
print(person.get('gender', 'Not specified'))  # Output: Not specified (default value)

# Modifying dictionaries
person['occupation'] = 'Engineer'  # Add new key-value pair
person['age'] = 31                 # Modify existing value
del person['city']                 # Remove a key-value pair

# Dictionary methods
print(person.keys())         # View of all keys
print(person.values())       # View of all values
print(person.items())        # View of all key-value pairs

# Dictionary comprehension (covered in more detail later)
squared = {x: x**2 for x in range(5)}

# 5. List Comprehensions
# Concise way to create lists based on existing lists or other iterables

# Basic syntax: [expression for item in iterable if condition]

# Example: Create a list of squares of even numbers from 0 to 9
squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
print(squares_of_evens)  # Output: [0, 4, 16, 36, 64]

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 6. Dictionary Comprehensions
# Concise way to create dictionaries

# Basic syntax: {key_expr: value_expr for item in iterable if condition}

# Example: Create a dictionary of squares of numbers from 0 to 4
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Example with condition: Even numbers and their squares
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 7. Set Comprehensions
# Concise way to create sets

# Basic syntax: {expr for item in iterable if condition}

# Example: Create a set of squares of numbers from 0 to 4
squares_set = {x**2 for x in range(5)}
print(squares_set)  # Output: {0, 1, 4, 9, 16}

# Example with condition: Set of even numbers
even_set = {x for x in range(10) if x % 2 == 0}
print(even_set)  # Output: {0, 2, 4, 6, 8}

# 8. Sequence Operations and Functions

# Common operations for sequences (lists, tuples, strings)
numbers = [1, 2, 3, 4, 5]

# Indexing and slicing (works for lists, tuples, and strings)
print(numbers[0])     # Output: 1
print(numbers[-1])    # Output: 5
print(numbers[1:4])   # Output: [2, 3, 4]
print(numbers[::-1])  # Output: [5, 4, 3, 2, 1] (reverse)

# Membership testing
print(3 in numbers)   # Output: True

# Concatenation
combined = numbers + [6, 7]
print(combined)  # Output: [1, 2, 3, 4, 5, 6, 7]

# Repetition
repeated = numbers * 2
print(repeated)  # Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Common functions for sequences
print(len(numbers))    # Length
print(max(numbers))    # Maximum value
print(min(numbers))    # Minimum value
print(sum(numbers))    # Sum of all elements

# Enumerate function (useful in loops)
for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")

# Zip function (combine multiple sequences)
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# List-specific functions
numbers.reverse()  # Reverse in place
print(numbers)     # Output: [5, 4, 3, 2, 1]

numbers.sort()     # Sort in place
print(numbers)     # Output: [1, 2, 3, 4, 5]

# Useful functions for all iterables
print(list(reversed(numbers)))  # Create a reversed iterator
print(sorted(numbers, reverse=True))  # Create a new sorted list in descending order

# Tip: Many of these operations work on strings too!
text = "Hello, World!"
print(text[:5])    # Output: Hello
print(text[::-1])  # Output: !dlroW ,olleH (reverse)

# Python Cheat Sheet: Modules and Packages

# 1. Importing Modules

# Basic import
import math
print(math.pi)  # Output: 3.141592653589793

# Import with alias
import math as m
print(m.pi)  # Output: 3.141592653589793

# Import specific items
from math import pi, sqrt
print(pi)    # Output: 3.141592653589793
print(sqrt(16))  # Output: 4.0

# Import all (use cautiously)
from math import *
print(cos(pi))  # Output: -1.0

# Tip: Avoid using 'import *' in production code as it can lead to naming conflicts

# 2. Exploring Built-in Modules

# sys module
import sys

print(sys.version)  # Python version
print(sys.path)     # List of directories Python looks in for modules
sys.exit()  # Exit the program (commented out to continue execution)

# os module
import os

print(os.getcwd())  # Current working directory
print(os.listdir())  # List files and directories in the current directory
os.mkdir("new_directory")  # Create a new directory
os.rmdir("new_directory")  # Remove a directory
print(os.environ)  # Environment variables

# Tip: Use os.path for cross-platform file path handling
print(os.path.join("folder", "subfolder", "file.txt"))

# math module
import math

print(math.pi)       # Pi
print(math.e)        # Euler's number
print(math.sin(0))   # Sine function
print(math.log(10))  # Natural logarithm
print(math.factorial(5))  # Factorial

# datetime module
import datetime

now = datetime.datetime.now()
print(now)  # Current date and time
print(now.year, now.month, now.day)  # Year, month, day

# Create a specific date
date = datetime.date(2023, 6, 15)
print(date)  # Output: 2023-06-15

# Time delta
delta = datetime.timedelta(days=7)
future_date = now + delta
print(future_date)  # Date 7 days from now

# 3. Creating and Using Packages

# Assume we have the following directory structure:
# my_package/
#     __init__.py
#     module1.py
#     module2.py
#     subpackage/
#         __init__.py
#         module3.py

# Contents of my_package/module1.py
def greet(name):
    return f"Hello, {name}!"

# Contents of my_package/module2.py
def farewell(name):
    return f"Goodbye, {name}!"

# Contents of my_package/subpackage/module3.py
def calculate_square(n):
    return n ** 2

# Contents of my_package/__init__.py
from .module1 import greet
from .module2 import farewell
from .subpackage.module3 import calculate_square

# Using the package
import my_package

print(my_package.greet("Alice"))  # Output: Hello, Alice!
print(my_package.farewell("Bob"))  # Output: Goodbye, Bob!
print(my_package.calculate_square(5))  # Output: 25

# Alternative import methods
from my_package import greet, farewell
from my_package.subpackage.module3 import calculate_square

print(greet("Charlie"))  # Output: Hello, Charlie!
print(calculate_square(3))  # Output: 9

# 4. if __name__ == "__main__":

# This idiom is used to check whether a script is being run directly or being imported

# Contents of a script named 'my_script.py'
def main_function():
    print("This is the main function of my_script.py")

if __name__ == "__main__":
    print("my_script.py is being run directly")
    main_function()
else:
    print("my_script.py is being imported as a module")

# When you run 'my_script.py' directly:
# Output:
# my_script.py is being run directly
# This is the main function of my_script.py

# When you import 'my_script.py' in another script:
# Output:
# my_script.py is being imported as a module

# 5. Additional Module and Package Concepts

# Reloading a module
import importlib
importlib.reload(math)

# Finding the location of a module
print(math.__file__)

# Listing all names in a module
print(dir(math))

# Getting help on a module
help(math)

# Creating a module dynamically
import types

dynamic_module = types.ModuleType("dynamic_module", "This is a dynamically created module")
dynamic_module.dynamic_variable = 42
print(dynamic_module.dynamic_variable)  # Output: 42

# Using __all__ in a module to control what's imported with 'from module import *'
# In a file named 'my_module.py':
__all__ = ['public_function']

def public_function():
    pass

def _private_function():
    pass

# When someone does 'from my_module import *', only 'public_function' will be imported

# 6. Virtual Environments

# Virtual environments allow you to create isolated Python environments for projects
# Here are some commands (to be run in the terminal, not in Python):

# Create a virtual environment
# python -m venv myenv

# Activate the virtual environment
# On Windows: myenv\Scripts\activate
# On Unix or MacOS: source myenv/bin/activate

# Deactivate the virtual environment
# deactivate

# 7. Package Management with pip

# pip is the package installer for Python. Some common commands:

# Install a package
# pip install package_name

# Install a specific version
# pip install package_name==1.0.4

# Upgrade a package
# pip install --upgrade package_name

# Uninstall a package
# pip uninstall package_name

# List installed packages
# pip list

# Generate a requirements file
# pip freeze > requirements.txt

# Install packages from a requirements file
# pip install -r requirements.txt

# Python Cheat Sheet: File Handling

import os
import json
import csv
import pickle
import shutil

# 1. Reading and Writing Text Files

# Opening a file
file = open('example.txt', 'r')  # 'r' for read mode
content = file.read()
print(content)
file.close()  # Always close the file when done

# Using 'with' statement (recommended)
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed after the 'with' block

# Writing to a file
with open('output.txt', 'w') as file:  # 'w' for write mode (overwrites existing content)
    file.write('Hello, World!\n')
    file.write('This is a new line.')

# Appending to a file
with open('output.txt', 'a') as file:  # 'a' for append mode
    file.write('\nThis line is appended.')

# Reading lines
with open('example.txt', 'r') as file:
    lines = file.readlines()  # Returns a list of lines
    for line in lines:
        print(line.strip())  # strip() removes leading/trailing whitespace

# Reading line by line (memory-efficient for large files)
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# 2. Handling Different File Formats

# CSV Files
# Writing CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# JSON Files
# Writing JSON
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Reading JSON
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)

# Binary Files
# Writing binary data
data = bytes([0, 1, 2, 3, 4, 5])
with open('binary_file.bin', 'wb') as file:  # 'wb' for write binary
    file.write(data)

# Reading binary data
with open('binary_file.bin', 'rb') as file:  # 'rb' for read binary
    binary_data = file.read()
    print(binary_data)

# Pickle (for serializing Python objects)
data = {'a': [1, 2.0, 3, 4+6j],
        'b': ('string', u'Unicode string'),
        'c': None}

# Writing pickle
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

# Reading pickle
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)

# 3. Working with File Paths

# Current working directory
print(os.getcwd())

# Join path components
path = os.path.join('folder', 'subfolder', 'file.txt')
print(path)

# Absolute path
abs_path = os.path.abspath('relative_path.txt')
print(abs_path)

# Directory and file name of a path
dir_name = os.path.dirname(path)
file_name = os.path.basename(path)
print(f"Directory: {dir_name}, File: {file_name}")

# Check if a path exists
print(os.path.exists(path))

# Check if it's a file or directory
print(os.path.isfile(path))
print(os.path.isdir(path))

# File extension
_, extension = os.path.splitext(file_name)
print(f"File extension: {extension}")

# 4. File and Directory Operations

# List directory contents
print(os.listdir('.'))  # '.' represents the current directory

# Create a new directory
os.mkdir('new_directory')

# Rename a file or directory
os.rename('old_name.txt', 'new_name.txt')

# Remove a file
os.remove('file_to_delete.txt')

# Remove an empty directory
os.rmdir('empty_directory')

# Remove a directory and its contents
shutil.rmtree('directory_to_delete')

# Copy a file
shutil.copy('source.txt', 'destination.txt')

# Copy a directory and its contents
shutil.copytree('source_dir', 'destination_dir')

# Move a file or directory
shutil.move('source', 'destination')

# 5. Context Managers for Resource Management

# Custom context manager using a class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Using the custom context manager
with FileManager('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Context manager using contextlib
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()

# Using the contextlib-based context manager
with file_manager('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 6. Advanced File Operations

# Temporary files and directories
import tempfile

# Create a temporary file
with tempfile.NamedTemporaryFile(mode='w+') as temp:
    temp.write('This is temporary content')
    temp.seek(0)
    print(temp.read())

# Create a temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Created temporary directory: {temp_dir}")

# File locking (platform-dependent)
import fcntl  # Unix-based systems only

def lock_file(file):
    fcntl.flock(file.fileno(), fcntl.LOCK_EX)

def unlock_file(file):
    fcntl.flock(file.fileno(), fcntl.LOCK_UN)

with open('shared_file.txt', 'w') as file:
    lock_file(file)
    file.write('This write operation is atomic')
    unlock_file(file)

# Memory-mapped files
import mmap

with open('large_file.bin', 'rb') as f:
    mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(mmapped_file[0:10])  # Read first 10 bytes
    mmapped_file.close()

# 7. Working with compressed files
import gzip
import zipfile

# Writing to a gzip file
with gzip.open('data.txt.gz', 'wt') as f:
    f.write('This content will be compressed')

# Reading from a gzip file
with gzip.open('data.txt.gz', 'rt') as f:
    content = f.read()
    print(content)

# Working with ZIP files
with zipfile.ZipFile('archive.zip', 'w') as zipf:
    zipf.write('file1.txt')
    zipf.write('file2.txt')

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extractall('extracted_folder')

# Python Cheat Sheet: Exception Handling

# 1. Basic Try-Except Block

try:
    x = 1 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Output: Cannot divide by zero!

# 2. Catching the Exception Object

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")

# Output: An error occurred: division by zero

# 3. Catching Multiple Exceptions

try:
    # This could raise different types of exceptions
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 4. Catching Multiple Exceptions in One Line

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")

# 5. Catching All Exceptions (use sparingly)

try:
    # Some risky operation
    x = 1 / 0
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 6. Else Clause

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"The result is: {result}")  # This runs if no exception occurs

# 7. Finally Clause

try:
    file = open("example.txt", "r")
    # Perform some operations with the file
except FileNotFoundError:
    print("The file was not found.")
finally:
    file.close()  # This will always execute, even if an exception occurs

# 8. Combining Else and Finally

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")

# 9. Raising Exceptions

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 120:
        raise ValueError("Age is too high.")

try:
    validate_age(150)
except ValueError as e:
    print(f"Invalid age: {e}")

# Output: Invalid age: Age is too high.

# 10. Re-raising Exceptions

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Caught an error, re-raising...")
    raise  # Re-raises the last exception

# 11. Custom Exceptions

class CustomError(Exception):
    """A custom exception class"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def raiseCustomError():
    raise CustomError("This is a custom error")

try:
    raiseCustomError()
except CustomError as e:
    print(f"Caught custom error: {e}")

# Output: Caught custom error: This is a custom error

# 12. Exception Hierarchy

# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       ...

# 13. Using assert Statements

def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

try:
    result = divide(10, 0)
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Output: Assertion failed: Divisor cannot be zero

# 14. Context Managers for Exception Handling

from contextlib import contextmanager

@contextmanager
def managed_resource():
    try:
        # Resource acquisition
        print("Resource acquired")
        yield "Resource"
    except Exception as e:
        # Exception handling
        print(f"An error occurred: {e}")
    finally:
        # Resource release
        print("Resource released")

with managed_resource() as resource:
    print(f"Using {resource}")
    raise ValueError("Something went wrong")

# Output:
# Resource acquired
# Using Resource
# An error occurred: Something went wrong
# Resource released

# 15. Chaining Exceptions (Python 3.3+)

try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Invalid operation") from e
except ValueError as e:
    print(f"Caught: {e}")
    print(f"Original exception: {e.__cause__}")

# Output:
# Caught: Invalid operation
# Original exception: division by zero

# 16. Suppressing Exceptions (Python 3.3+)

try:
    try:
        1 / 0
    except ZeroDivisionError:
        raise ValueError("Invalid operation") from None
except ValueError as e:
    print(f"Caught: {e}")
    print(f"Original exception: {e.__cause__}")

# Output:
# Caught: Invalid operation
# Original exception: None

# 17. Exception Groups (Python 3.11+)

def process_data(data):
    errors = []
    for item in data:
        try:
            # Process item
            if item < 0:
                raise ValueError(f"Negative value: {item}")
        except ValueError as e:
            errors.append(e)
    
    if errors:
        raise ExceptionGroup("Processing errors", errors)

try:
    process_data([1, -2, 3, -4])
except* ValueError as eg:
    print(f"Caught {len(eg.exceptions)} ValueError(s):")
    for i, e in enumerate(eg.exceptions, 1):
        print(f"  {i}. {e}")

# Output:
# Caught 2 ValueError(s):
#   1. Negative value: -2
#   2. Negative value: -4

# Python Cheat Sheet: Object-Oriented Programming

# 1. Classes and Objects

class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # Output: Buddy
print(dog2.bark())  # Output: Max says Woof!
print(Dog.species)  # Output: Canis familiaris

# 2. Attributes and Methods

class Circle:
    pi = 3.14159  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    def area(self):  # Instance method
        return self.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):  # Class method
        return cls(diameter / 2)

    @staticmethod
    def is_valid_radius(radius):  # Static method
        return radius > 0

circle = Circle(5)
print(circle.area())  # Output: 78.53975
print(Circle.is_valid_radius(5))  # Output: True

# 3. Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

cat = Cat("Whiskers")
dog = Dog("Rex")

print(cat.speak())  # Output: Whiskers says Meow!
print(dog.speak())  # Output: Rex says Woof!

# 4. Polymorphism

def animal_sound(animal):
    return animal.speak()

print(animal_sound(cat))  # Output: Whiskers says Meow!
print(animal_sound(dog))  # Output: Rex says Woof!

# 5. Encapsulation

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300

# 6. Special Methods

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

book = Book("1984", "George Orwell")
print(str(book))  # Output: 1984 by George Orwell
print(repr(book))  # Output: Book('1984', 'George Orwell')

# 7. Multiple Inheritance

class A:
    def method(self):
        print("Method from A")

class B:
    def method(self):
        print("Method from B")

class C(A, B):
    pass

c = C()
c.method()  # Output: Method from A (Method Resolution Order)

# 8. Abstract Base Classes

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# shape = Shape()  # This would raise TypeError
square = Square(5)
print(square.area())  # Output: 25

# 9. Properties

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius)  # Output: 25
print(temp.fahrenheit)  # Output: 77.0
temp.celsius = 30
print(temp.fahrenheit)  # Output: 86.0

# 10. Class and Static Methods

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def multiply(cls, x, y):
        return cls.add(x, 0) * y  # Using the static method

print(MathOperations.add(5, 3))  # Output: 8
print(MathOperations.multiply(4, 3))  # Output: 12

# 11. Method Overriding and Super()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Output: Buddy barks

# 12. Mixins

class SwimMixin:
    def swim(self):
        return f"{self.name} is swimming"

class FlyMixin:
    def fly(self):
        return f"{self.name} is flying"

class Duck(Animal, SwimMixin, FlyMixin):
    pass

duck = Duck("Donald")
print(duck.swim())  # Output: Donald is swimming
print(duck.fly())   # Output: Donald is flying

# 13. Dataclasses (Python 3.7+)

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

p = Point(3, 4)
print(p)  # Output: Point(x=3, y=4)
print(p.distance_from_origin())  # Output: 5.0

# 14. Type Hints in Classes (Python 3.5+)

from typing import List

class ShoppingCart:
    def __init__(self) -> None:
        self.items: List[str] = []

    def add_item(self, item: str) -> None:
        self.items.append(item)

    def get_items(self) -> List[str]:
        return self.items

cart = ShoppingCart()
cart.add_item("Apple")
print(cart.get_items())  # Output: ['Apple']

# Python Cheat Sheet: Advanced Features

# 10. Iterators and Generators

# Iterator
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Using the iterator
for num in CountDown(5):
    print(num)  # Output: 5, 4, 3, 2, 1

# Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(5):
    print(num)  # Output: 0, 1, 1, 2, 3

# 11. Decorators

# Function decorator
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world!"

print(greet())  # Output: HELLO, WORLD!

# Class decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        self.connection = "Connected"

# 12. Context Managers

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Using the context manager
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')

# Context manager using contextlib
from contextlib import contextmanager

@contextmanager
def temp_file(filename):
    try:
        f = open(filename, 'w')
        yield f
    finally:
        f.close()

# 13. Coroutines and Asyncio

import asyncio

async def fetch_data(url):
    print(f"Start fetching {url}")
    await asyncio.sleep(2)  # Simulating I/O operation
    print(f"Finished fetching {url}")
    return f"Data from {url}"

async def main():
    urls = ['http://example.com', 'http://example.org', 'http://example.net']
    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

# Run the event loop
asyncio.run(main())

# 14. Metaclasses

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True

# 15. Descriptor Protocol

class Validator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"{self.name} must be between {self.min_value} and {self.max_value}")
        instance.__dict__[self.name] = value

class Person:
    age = Validator(0, 150)

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
person = Person("Alice", 30)
print(person.age)  # Output: 30
# person.age = 200  # This would raise a ValueError

# Python Cheat Sheet: Concurrency and Parallelism

# 1. Threading

import threading
import time

def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)
    print(f"Worker {name} finished")

# Creating and starting threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Waiting for all threads to complete
for t in threads:
    t.join()

print("All threads completed")

# Using a ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor

def task(n):
    time.sleep(n)
    return f"Task {n} completed"

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(5)]
    for future in futures:
        print(future.result())

# Thread synchronization with Lock
counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        current = counter
        time.sleep(0.1)
        counter = current + 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final counter value: {counter}")

# 2. Multiprocessing

import multiprocessing

def process_worker(num):
    return num * num

if __name__ == '__main__':
    # Using Pool for parallel processing
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(process_worker, range(10))
        print(results)

    # Using Process class
    def info(title):
        print(title)
        print('module name:', __name__)
        print('parent process:', multiprocessing.parent_process())
        print('process id:', multiprocessing.current_process().pid)

    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=info, args=(f'Process {i}',))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Sharing data between processes
    def f(n, a):
        n.value = 3.14159265359
        for i in range(len(a)):
            a[i] = -a[i]

    num = multiprocessing.Value('d', 0.0)
    arr = multiprocessing.Array('i', range(10))

    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

# 3. Async Programming

import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

# Running the event loop
asyncio.run(main())

# Concurrent execution of tasks
async def main_concurrent():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main_concurrent())

# Asynchronous context managers
class AsyncContextManager:
    async def __aenter__(self):
        print("Entering the context")
        await asyncio.sleep(1)
        return "Context Value"

    async def __aexit__(self, exc_type, exc, tb):
        print("Exiting the context")
        await asyncio.sleep(1)

async def use_context_manager():
    async with AsyncContextManager() as value:
        print(f"Inside the context with value: {value}")

asyncio.run(use_context_manager())

# Asynchronous iteration
class AsyncIterator:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.stop:
            await asyncio.sleep(1)
            self.current += 1
            return self.current - 1
        else:
            raise StopAsyncIteration

async def use_async_iterator():
    async for num in AsyncIterator(5):
        print(num)

asyncio.run(use_async_iterator())

# Python Cheat Sheet: Regular Expressions

import re

# 1. Basic Patterns and Character Classes

# Basic matching
pattern = r"hello"
text = "hello world"
match = re.search(pattern, text)
print(match.group())  # Output: hello

# Character classes
digit_pattern = r"\d+"  # Matches one or more digits
word_pattern = r"\w+"  # Matches one or more word characters
space_pattern = r"\s+"  # Matches one or more whitespace characters

# Custom character classes
vowel_pattern = r"[aeiou]"  # Matches any vowel
not_digit_pattern = r"[^\d]"  # Matches any character that's not a digit

# Quantifiers
zero_or_more = r"a*"  # Matches zero or more 'a'
one_or_more = r"a+"  # Matches one or more 'a'
zero_or_one = r"a?"  # Matches zero or one 'a'
exactly_n = r"a{3}"  # Matches exactly 3 'a'
n_or_more = r"a{3,}"  # Matches 3 or more 'a'
between_n_and_m = r"a{3,5}"  # Matches between 3 and 5 'a'

# 2. Grouping and Capturing

# Basic grouping
pattern = r"(\d+)-(\d+)-(\d+)"
text = "Date: 2023-06-27"
match = re.search(pattern, text)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")

# Named groups
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, text)
if match:
    print(f"Year: {match.group('year')}, Month: {match.group('month')}, Day: {match.group('day')}")

# Non-capturing groups
pattern = r"(?:Mr|Mrs|Ms)\s(\w+)"
text = "Mr Smith and Mrs Johnson"
matches = re.findall(pattern, text)
print(matches)  # Output: ['Smith', 'Johnson']

# Backreferences
pattern = r"(\w+)\s+\1"
text = "hello hello world world"
matches = re.findall(pattern, text)
print(matches)  # Output: ['hello', 'world']

# 3. Lookahead and Lookbehind Assertions

# Positive lookahead
pattern = r"\d+(?=\s*dollars)"
text = "I have 50 dollars and 20 euros"
matches = re.findall(pattern, text)
print(matches)  # Output: ['50']

# Negative lookahead
pattern = r"\d+(?!\s*dollars)"
matches = re.findall(pattern, text)
print(matches)  # Output: ['20']

# Positive lookbehind
pattern = r"(?<=price:\s)\d+"
text = "The price: 100 dollars"
match = re.search(pattern, text)
if match:
    print(match.group())  # Output: 100

# Negative lookbehind
pattern = r"(?<!@)\b\w+\b"
text = "user@example.com and johndoe"
matches = re.findall(pattern, text)
print(matches)  # Output: ['and', 'johndoe']

# Tips and Tricks

# 1. Using re.VERBOSE for readable patterns
phone_pattern = re.compile(r"""
    (\d{3})  # Area code
    [-.\s]?  # Optional separator
    (\d{3})  # First 3 digits
    [-.\s]?  # Optional separator
    (\d{4})  # Last 4 digits
    """, re.VERBOSE)

# 2. Using re.IGNORECASE for case-insensitive matching
pattern = re.compile(r"python", re.IGNORECASE)
print(pattern.search("PYTHON is awesome").group())  # Output: PYTHON

# 3. Using \b for word boundaries
pattern = r"\bcat\b"
print(re.findall(pattern, "cat cats cat's catalog"))  # Output: ['cat', 'cat']

# 4. Non-greedy matching with '?'
pattern = r"<.*?>"
text = "<p>This is a <b>bold</b> paragraph</p>"
print(re.findall(pattern, text))  # Output: ['<p>', '<b>', '</b>', '</p>']

# 5. Using re.sub for string replacement
text = "I love cats, but I'm allergic to cats."
new_text = re.sub(r"cats", "dogs", text)
print(new_text)  # Output: I love dogs, but I'm allergic to dogs.

# 6. Using re.split for advanced string splitting
text = "apple,banana;cherry:date"
print(re.split(r"[,;:]", text))  # Output: ['apple', 'banana', 'cherry', 'date']

# 7. Using (?#...) for comments in complex patterns
pattern = r"(\d{3})(?#area code)[-.]?(\d{3})(?#prefix)[-.]?(\d{4})(?#line number)"

# 8. Using \A and \Z for start and end of string
pattern = r"\A\d+\Z"
print(re.match(pattern, "12345"))  # Matches
print(re.match(pattern, "12345\n"))  # Doesn't match

# 9. Using re.escape() to escape special characters
special_chars = ".^$*+?{}[]|/()"
pattern = re.escape(special_chars)
print(pattern)  # Output: \.\^\$\*\+\?\{\}\[\]\|/\(\)

# Python Cheat Sheet: Testing

# 1. Unit Testing with unittest

import unittest

# Sample function to test
def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)
    
    # Tip: Use assertAlmostEqual for floating-point comparisons
    def test_add_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
    
    # Tip: Use assertRaises to test exceptions
    def test_add_strings(self):
        with self.assertRaises(TypeError):
            add("2", "3")

# Tip: Use setUp and tearDown for common setup and cleanup
class TestWithSetupAndTeardown(unittest.TestCase):
    def setUp(self):
        self.test_file = open('test.txt', 'w')
    
    def tearDown(self):
        self.test_file.close()
    
    def test_write_to_file(self):
        self.test_file.write("Hello, World!")
        self.test_file.seek(0)
        content = self.test_file.read()
        self.assertEqual(content, "Hello, World!")

# Tip: Use subTest for parameterized tests
class TestParameterized(unittest.TestCase):
    def test_odd_even(self):
        test_cases = [
            (3, "odd"),
            (4, "even"),
            (0, "even"),
            (-1, "odd"),
        ]
        for num, expected in test_cases:
            with self.subTest(num=num):
                self.assertEqual("odd" if num % 2 else "even", expected)

# Tip: Use mock to isolate tests
from unittest.mock import patch

def get_user_input():
    return input("Enter a number: ")

def process_input():
    user_input = get_user_input()
    return int(user_input) * 2

class TestWithMock(unittest.TestCase):
    @patch('builtins.input', return_value='5')
    def test_process_input(self, mock_input):
        result = process_input()
        self.assertEqual(result, 10)
        mock_input.assert_called_once_with("Enter a number: ")

# Tip: Use custom test discovery and execution
if __name__ == '__main__':
    # Discover and run tests in all files named test_*.py
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    unittest.TextTestRunner().run(test_suite)

# 2. Introduction to pytest

# Note: pytest should be installed separately: pip install pytest

# pytest automatically discovers test functions prefixed with "test_"
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

# Tip: Use parametrize for multiple test cases
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# Tip: Use fixtures for setup and teardown
@pytest.fixture
def sample_file(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Hello, World!")
    return file

def test_read_file(sample_file):
    content = sample_file.read_text()
    assert content == "Hello, World!"

# Tip: Use markers to categorize tests
@pytest.mark.slow
def test_slow_operation():
    # Simulate a slow operation
    import time
    time.sleep(2)
    assert True

# Run only slow tests: pytest -v -m slow

# Tip: Use monkeypatch for modifying behavior
def get_os_name():
    import os
    return os.name

def test_get_os_name(monkeypatch):
    monkeypatch.setattr('os.name', 'test_os')
    assert get_os_name() == 'test_os'

# Tip: Use capsys to capture stdout/stderr
def print_hello():
    print("Hello, World!")

def test_print_hello(capsys):
    print_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"

# Tip: Use tmpdir for temporary directory
def test_with_tmpdir(tmpdir):
    file_path = tmpdir.join('test.txt')
    file_path.write("content")
    assert file_path.read() == "content"

# Additional Tips:

# 1. Use coverage.py to measure code coverage
# pip install coverage
# coverage run -m pytest
# coverage report

# 2. Use tox for testing across multiple Python versions
# pip install tox
# Create a tox.ini file and run: tox

# 3. Use hypothesis for property-based testing
# pip install hypothesis
from hypothesis import given
from hypothesis.strategies import integers

@given(integers(), integers())
def test_add_commutative(a, b):
    assert add(a, b) == add(b, a)

# 4. Use doctest for testing examples in docstrings
def multiply(a, b):
    """
    Multiply two numbers.

    >>> multiply(2, 3)
    6
    >>> multiply(-1, 4)
    -4
    """
    return a * b

# Run with: python -m doctest filename.py

# 5. Use asynctest for testing asynchronous code
import asyncio
import asynctest

async def async_add(a, b):
    await asyncio.sleep(0.1)
    return a + b

class TestAsyncAdd(asynctest.TestCase):
    async def test_async_add(self):
        result = await async_add(2, 3)
        self.assertEqual(result, 5)

# Run with: python -m asynctest filename.py

# Python Cheat Sheet: Web Development

# 1. Basics of Web Frameworks

## 1.1 Flask

# Installation: pip install Flask

from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

# Route with variable
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

# HTTP methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_login()
    else:
        return show_login_form()

# Rendering templates
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

# Redirects
@app.route('/redirect')
def redirect_example():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

# Tip: Use Flask-SQLAlchemy for database integration
# pip install Flask-SQLAlchemy

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Tip: Use Flask-WTF for form handling
# pip install Flask-WTF

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

# Tip: Use Flask-Login for user session management
# pip install Flask-Login

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    # ... (user model definition)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/protected')
@login_required
def protected():
    return f'Hello, {current_user.username}!'

## 1.2 Django

# Installation: pip install Django

# Create a new Django project
# django-admin startproject myproject

# Create a new Django app
# python manage.py startapp myapp

# settings.py
INSTALLED_APPS = [
    # ...
    'myapp',
]

# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    return HttpResponse("Hello, World!")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

# urls.py (in myapp)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
]

# urls.py (in myproject)
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

# Tip: Use Django Forms for form handling
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# Tip: Use Django's built-in authentication system
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    # ... (view logic)

# Tip: Use Django Rest Framework for building APIs
# pip install djangorestframework

# settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework',
]

# serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'pub_date']

# views.py
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 2. REST APIs with Flask

# pip install Flask-RESTful

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

# CRUD operations
todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

# Tip: Use request parsing for input validation
parser = reqparse.RequestParser()
parser.add_argument('task', type=str, required=True, help='Task cannot be blank')

class TodoList(Resource):
    def post(self):
        args = parser.parse_args()
        todo_id = max(todos.keys()) + 1
        todos[todo_id] = args['task']
        return {todo_id: todos[todo_id]}, 201

api.add_resource(TodoList, '/todos')

# Tip: Use Flask-JWT for authentication in APIs
# pip install Flask-JWT

from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

users = [User(1, 'user1', 'password1'), User(2, 'user2', 'password2')]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

jwt = JWT(app, authenticate, identity)

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        return {'current_identity': current_identity.username}

api.add_resource(ProtectedResource, '/protected')

if __name__ == '__main__':
    app.run(debug=True)

# Additional Tips and Best Practices:

# 1. Use virtual environments for project isolation
# python -m venv myenv
# source myenv/bin/activate (Linux/macOS) or myenv\Scripts\activate (Windows)

# 2. Use environment variables for sensitive information
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()

# 3. Implement proper error handling and logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 4. Use Flask-Migrate for database migrations in Flask
# pip install Flask-Migrate

# 5. Implement rate limiting for APIs
# pip install Flask-Limiter

# 6. Use Flask-CORS for handling Cross-Origin Resource Sharing (CORS)
# pip install Flask-CORS

# 7. Implement proper security measures (HTTPS, CSRF protection, etc.)

# 8. Use caching mechanisms for improved performance
# pip install Flask-Caching

# 9. Implement API versioning for better maintenance
@app.route('/api/v1/resource')
def api_v1_resource():
    # ...

# 10. Use Swagger/OpenAPI for API documentation
# pip install flask-swagger-ui

# 11. Implement proper testing for your web applications
# pytest for Flask, Django's built-in testing framework for Django

# 12. Use asynchronous frameworks for high-performance applications
# FastAPI, Quart (for Flask-like async), or Django Channels

# Python Cheat Sheet: Data Science and Visualization

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. NumPy

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
arr3 = np.linspace(0, 1, 5)  # [0., 0.25, 0.5, 0.75, 1.]

# Tip: Use np.zeros, np.ones, or np.empty for quick array initialization
zeros = np.zeros((3, 3))
ones = np.ones((2, 2))
empty = np.empty((2, 3))  # Uninitialized

# Reshaping arrays
arr = np.arange(12)
reshaped = arr.reshape((3, 4))
# Tip: Use -1 to automatically calculate the size of one dimension
auto_reshaped = arr.reshape((3, -1))

# Array operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # Element-wise addition
print(a * b)  # Element-wise multiplication
print(np.dot(a, b))  # Dot product

# Broadcasting
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)  # b is broadcast to match a's shape

# Indexing and slicing
arr = np.arange(10)
print(arr[2:5])  # [2, 3, 4]
print(arr[::2])  # [0, 2, 4, 6, 8]
# Tip: Use negative step for reverse order
print(arr[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Boolean indexing
arr = np.arange(12).reshape((3, 4))
bool_idx = arr > 5
print(arr[bool_idx])  # [6, 7, 8, 9, 10, 11]

# Tip: Use np.where for conditional selection
result = np.where(arr % 2 == 0, arr, -1)

# Statistical operations
arr = np.random.randn(5, 4)
print(arr.mean())
print(arr.std())
print(arr.var())
# Tip: Specify axis for row-wise or column-wise operations
print(arr.sum(axis=0))  # Column-wise sum
print(arr.max(axis=1))  # Row-wise maximum

# Linear algebra operations
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))
print(np.linalg.inv(a))  # Inverse
print(np.linalg.eig(a))  # Eigenvalues and eigenvectors

# Tip: Use @  operator for matrix multiplication (Python 3.5+)
print(a @ b)

# 2. Pandas

# Creating DataFrames
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
# Tip: Use pd.date_range for date indices
dates = pd.date_range('20230101', periods=6)
df_dates = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

# Reading and writing data
# Tip: Specify usecols to read only specific columns
df_csv = pd.read_csv('file.csv', usecols=['A', 'B'])
df_excel = pd.read_excel('file.xlsx', sheet_name='Sheet1')
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', sheet_name='Sheet1')

# Basic operations
print(df.head())  # First 5 rows
print(df.tail())  # Last 5 rows
print(df.info())  # Summary of DataFrame
print(df.describe())  # Statistical summary

# Selecting data
print(df['A'])  # Select column
print(df[['A', 'B']])  # Select multiple columns
print(df.loc[0])  # Select row by label
print(df.iloc[0])  # Select row by integer index
# Tip: Use .at and .iat for fast scalar value access
print(df.at[0, 'A'])
print(df.iat[0, 0])

# Filtering
print(df[df['A'] > 1])
# Tip: Use query method for string expressions
print(df.query('A > 1 and B < 6'))

# Handling missing data
df_missing = df.copy()
df_missing.loc[0, 'A'] = np.nan
print(df_missing.dropna())  # Drop rows with NaN
print(df_missing.fillna(0))  # Fill NaN with 0
# Tip: Use different fill methods
print(df_missing.fillna(method='ffill'))  # Forward fill

# Group operations
df_grouped = df.groupby('A')
print(df_grouped.mean())
# Tip: Use agg for multiple operations
print(df_grouped.agg({'B': 'mean', 'C': ['min', 'max']}))

# Merging and joining
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
print(pd.merge(df1, df2, on='key', how='outer'))

# Pivot tables
df_pivot = pd.DataFrame({'A': ['foo', 'foo', 'bar', 'bar'],
                         'B': ['one', 'two', 'one', 'two'],
                         'C': [1, 2, 3, 4]})
print(df_pivot.pivot_table(values='C', index='A', columns='B', aggfunc='sum'))

# Time series operations
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
print(ts.resample('M').mean())  # Monthly resampling
print(ts.rolling(window=7).mean())  # 7-day rolling average

# 3. Matplotlib

# Basic line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
# Tip: Use tight_layout to adjust subplot params
plt.tight_layout()
plt.show()

# Multiple plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, np.sin(x))
ax1.set_title('Sine')
ax2.plot(x, np.cos(x))
ax2.set_title('Cosine')
# Tip: Use suptitle for a figure-level title
fig.suptitle('Trigonometric Functions')
plt.show()

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.colorbar()
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
# Tip: Use density=True for probability density
plt.hist(data, bins=30, density=True, alpha=0.7)
plt.show()

# Bar plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]
plt.bar(categories, values)
# Tip: Use barh for horizontal bars
plt.barh(categories, values)
plt.show()

# Pie chart
sizes = [30, 40, 20, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# Tip: Use explode to emphasize a slice
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()

# 3D plot
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
ax.scatter(x, y, z)
plt.show()

# Customization
plt.style.use('seaborn')  # Change style
plt.rcParams['font.size'] = 14  # Change default font size
# Tip: Use context manager for temporary style changes
with plt.style.context('dark_background'):
    plt.plot(x, y)
    plt.show()

# 4. Seaborn

# Set style and color palette
sns.set_style("whitegrid")
sns.set_palette("deep")

# Scatter plot with regression line
tips = sns.load_dataset("tips")
sns.regplot(x="total_bill", y="tip", data=tips)
plt.show()

# Categorical plot
sns.catplot(x="day", y="total_bill", kind="box", data=tips)
plt.show()

# Distribution plot
sns.distplot(tips['total_bill'], kde=True, rug=True)
# Tip: Use histplot for more control over histograms
sns.histplot(tips['total_bill'], kde=True)
plt.show()

# Heatmap
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot("month", "year", "passengers")
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.show()

# Pair plot
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.show()

# Violin plot
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()

# Joint plot
sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
plt.show()

# FacetGrid for multi-plot grids
g = sns.FacetGrid(tips, col="time", row="smoker")
g.map(plt.scatter, "total_bill", "tip")
plt.show()

# Tips and Tricks

# 1. Use vectorized operations in NumPy and Pandas for better performance
# Bad: for loop
# Good: df['new_col'] = df['col1'] + df['col2']

# 2. Use .loc for label-based indexing and .iloc for position-based indexing in Pandas
# df.loc['row_label', 'column_label']
# df.iloc[0, 1]

# 3. Chainning methods in Pandas
result = (df.groupby('category')
          .agg({'value': 'mean'})
          .sort_values('value', ascending=False)
          .reset_index())

# 4. Use query() for complex filtering in Pandas
df.query('(column1 > 5) & (column2 < 10) | (column3 == "value")')

# 5. Efficient memory usage with categories in Pandas
df['category_column'] = df['category_column'].astype('category')

# 6. Use plt.subplots() for creating figure and axes objects in Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y)

# 7. Customize Seaborn plots with Matplotlib
g = sns.regplot(x="total_bill", y="tip", data=tips)
g.set(xlabel="Total Bill ($)", ylabel="Tip ($)")
g.set_title("Relationship between Bill and Tip")

# 8. Use sns.despine() to remove top and right spines in Seaborn plots
sns.despine()

# 9. Efficient data reading in Pandas
# Use chunksize for large files
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process(chunk)

# 10. Use context managers for temporary style changes in Matplotlib and Seaborn
with sns.axes_style("darkgrid"):
    plt.plot(x, y)

# 11. Utilize multiprocessing for parallel computations in NumPy
from multiprocessing import Pool

def parallel_operation(chunk):
    return np.sum(chunk)

with Pool() as p:
    result = p.map(parallel_operation, np.array_split(large_array, 4))

# 12. Use generators for memory-efficient data processing
def data_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield process_line(line)

for processed_data in data_generator('large_file.txt'):
    analyze(processed_data)

    # Python Cheat Sheet: Debugging and Profiling

# 1. Debugging with pdb (Python Debugger)

import pdb

def complex_function(x, y):
    result = x + y
    pdb.set_trace()  # Breakpoint
    for i in range(5):
        result *= i + 1
    return result

# To run:
# complex_function(3, 4)

# Basic pdb commands:
# n (next) - Execute the current line
# s (step) - Step into a function call
# c (continue) - Continue execution until the next breakpoint
# p variable_name - Print the value of a variable
# l (list) - Show the current location in the code
# q (quit) - Quit the debugger

# Tip: Use breakpoint() instead of pdb.set_trace() in Python 3.7+

# Post-mortem debugging
def buggy_function():
    x = 5
    y = 0
    return x / y

try:
    buggy_function()
except ZeroDivisionError:
    import pdb
    pdb.post_mortem()

# Conditional breakpoints
x = 10
if x > 5:
    breakpoint()

# Tip: Use PYTHONBREAKPOINT environment variable to control breakpoint() behavior
# export PYTHONBREAKPOINT=0  # Disable breakpoints
# export PYTHONBREAKPOINT=pdb.set_trace  # Use pdb (default)

# Using pdb in command line
# python -m pdb script.py

# 2. Debugging with IDEs

# Most IDEs (PyCharm, VS Code, etc.) provide graphical debuggers
# Common features:
# - Setting breakpoints
# - Step over, step into, step out
# - Variable inspection
# - Watch expressions
# - Call stack examination

# Tip: Learn keyboard shortcuts for efficient debugging in your IDE

# 3. Logging for Debugging

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def divide(x, y):
    logging.debug(f'Dividing {x} by {y}')
    try:
        result = x / y
    except ZeroDivisionError:
        logging.error('Division by zero!')
        raise
    logging.info(f'Result: {result}')
    return result

# Tip: Use different logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# for appropriate granularity

# 4. Assertions for Debugging

def calculate_average(numbers):
    assert len(numbers) > 0, "List is empty"
    return sum(numbers) / len(numbers)

# Tip: Use -O flag to disable assertions in production code
# python -O script.py

# 5. Profiling Code for Performance

# Using cProfile

import cProfile

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

cProfile.run('fibonacci(30)')

# Tip: Sort the output by cumulative time
# cProfile.run('fibonacci(30)', sort='cumtime')

# Using line_profiler for line-by-line profiling
# pip install line_profiler

@profile
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

# Run with: kernprof -l -v script.py

# Using memory_profiler to profile memory usage
# pip install memory_profiler

from memory_profiler import profile

@profile
def memory_hungry_function():
    return [i for i in range(1000000)]

# Run with: python -m memory_profiler script.py

# Tip: Use mprof for plotting memory usage over time
# mprof run script.py
# mprof plot

# 6. Timing Code Execution

import time

start_time = time.time()
# Your code here
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")

# Using timeit for more accurate timing
import timeit

def function_to_time():
    return sum(range(1000000))

execution_time = timeit.timeit(function_to_time, number=10)
print(f"Average execution time: {execution_time / 10} seconds")

# Tip: Use timeit in IPython/Jupyter for quick timing
# %timeit function_to_time()

# 7. Profiling with cProfile and visualization

import cProfile
import pstats
from pstats import SortKey

# Profile the code
cProfile.run('fibonacci(30)', 'output.prof')

# Analyze the results
with open('output_stats.txt', 'w') as f:
    p = pstats.Stats('output.prof', stream=f)
    p.sort_stats(SortKey.CUMULATIVE).print_stats(10)

# Tip: Use snakeviz for visualization
# pip install snakeviz
# snakeviz output.prof

# 8. Using tracemalloc for memory tracking

import tracemalloc

tracemalloc.start()

# Your code here

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)

# 9. Debugging Multithreaded Applications

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s')

def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def main():
    threading.Thread(target=worker, name='Worker-1').start()
    threading.Thread(target=worker, name='Worker-2').start()

# Tip: Use thread names for easier identification in logs

# 10. Remote Debugging

# For remote debugging, you can use tools like:
# - pdb over SSH
# - remote-pdb package
# - IDE remote debugging features (e.g., PyCharm Professional)

# Example using remote-pdb:
# pip install remote-pdb

from remote_pdb import set_trace
set_trace(host='0.0.0.0', port=4444)  # Listen on all interfaces

# Connect using: telnet localhost 4444

# Tips and Tricks

# 1. Use f-strings for easy debugging prints
x = 10
y = 20
print(f"{x=}, {y=}")  # Python 3.8+

# 2. Use breakpoint() with custom debuggers
# PYTHONBREAKPOINT=pudb.set_trace python script.py

# 3. Use @profile decorator selectively
if 'line_profiler' in globals():
    profile = globals()['profile']
else:
    profile = lambda x: x

# 4. Use context managers for timing
from contextlib import contextmanager
import time

@contextmanager
def timing(description: str) -> None:
    start = time.time()
    yield
    ellapsed_time = time.time() - start
    print(f"{description}: {ellapsed_time:.3f} seconds")

with timing("Complex operation"):
    # Your code here
    time.sleep(1)

# 5. Use functools.lru_cache for memoization and performance improvement
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 6. Use dis module to inspect bytecode
import dis

def simple_function(x, y):
    return x + y

dis.dis(simple_function)

# 7. Use sys.getsizeof() to check object memory usage
import sys

x = [1, 2, 3, 4, 5]
print(sys.getsizeof(x))  # Size in bytes

# 8. Use objgraph for object reference visualization
# pip install objgraph

import objgraph

x = [1, 2, 3]
y = [x, dict(key1=x)]
objgraph.show_refs([y], filename='sample-graph.png')

# 9. Use traceback module for better exception handling
import traceback

try:
    1 / 0
except Exception as e:
    print("An error occurred:")
    print(traceback.format_exc())

# 10. Use yappi for profiling multi-threaded applications
# pip install yappi

import yappi

yappi.set_clock_type("cpu")  # Use set_clock_type("wall") for wall time
yappi.start()

# Your multi-threaded code here

yappi.stop()
threads = yappi.get_thread_stats()
for thread in threads:
    print(f"Function stats for ({thread.name}) ({thread.id}):")
    yappi.get_func_stats(ctx_id=thread.id).print_all()

# Remember: "Premature optimization is the root of all evil" - Donald Knuth
# Profile first, optimize later, and always measure the impact of your optimizations.
