# Importing necessary libraries
import os
import sys

# Function Definitions
def basic_data_types():
    """Demonstrates Python's basic data types."""
    integer_var = 42
    float_var = 3.14159
    complex_var = 2 + 3j
    str_var = "Hello, Python!"
    bool_var = True
    none_var = None
    print("Integer:", integer_var)
    print("Float:", float_var)
    print("Complex:", complex_var)
    print("String:", str_var)
    print("Boolean:", bool_var)
    print("NoneType:", none_var)

def collections_demo():
    """Shows examples of collections - list, tuple, set, dictionary."""
    list_var = [1, 2, 3, 'Python']
    tuple_var = (1, 2, 3, 'Python')
    set_var = {1, 2, 3, 'Python'}
    dict_var = {'one': 1, 'two': 2, 'three': 3, 'language': 'Python'}
    print("List:", list_var)
    print("Tuple:", tuple_var)
    print("Set:", set_var)
    print("Dictionary:", dict_var)

def control_structures():
    """Demonstrates if, for, and while loops."""
    # If-else
    x = 10
    if x > 5:
        print("x is greater than 5")
    elif x < 5:
        print("x is less than 5")
    else:
        print("x is equal to 5")
    
    # For loop
    for i in range(5):
        print(i, end=' ')
    print()

    # While loop
    y = 5
    while y > 0:
        print(y, end=' ')
        y -= 1
    print()

def file_io():
    """Demonstrates file input/output."""
    filename = 'example.txt'
    with open(filename, 'w') as f:
        f.write("Hello, Python file IO!\n")
    
    with open(filename, 'r') as f:
        content = f.read()
        print("Read from file:", content)

def error_handling():
    """Demonstrates try, except, finally structure."""
    try:
        # Trying to divide by zero
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught division by zero error")
    finally:
        print("This is the finally block executing.")

# Object-oriented programming
class BasicClass:
    """A simple example class with an initializer, method, and a static method."""
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        """Method that prints a greeting."""
        print(f"Hello from {self.name}!")

    @staticmethod
    def example_static_method():
        """Static method that prints a static message."""
        print("This is a static method in BasicClass.")

def using_classes():
    """Function to demonstrate creating and using objects."""
    my_object = BasicClass("BasicClassObject")
    my_object.greet()
    BasicClass.example_static_method()

# Entry point of the script
if __name__ == "__main__":
    print("Python Basics and Fundamentals\n")
    basic_data_types()
    collections_demo()
    control_structures()
    file_io()
    error_handling()
    using_classes()
