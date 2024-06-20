# Importing necessary libraries
import os
import sys
import math
import random
import json
import re
import datetime
import time
import itertools
import functools
from collections import defaultdict, Counter, namedtuple, deque
from typing import List, Tuple, Set, Dict, Union, Optional

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

    # List comprehension
    squared_numbers = [x ** 2 for x in range(1, 6)]
    print("List comprehension:", squared_numbers)

    # Dictionary comprehension
    cube_dict = {x: x ** 3 for x in range(1, 6)}
    print("Dictionary comprehension:", cube_dict)

    # Accessing elements
    print("List element at index 2:", list_var[2])
    print("Dictionary value for 'two':", dict_var['two'])

    # Modifying elements
    list_var[2] = 'Python3'
    dict_var['language'] = 'Python3'
    print("Modified list:", list_var)
    print("Modified dictionary:", dict_var)

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

    # Break and continue
    for i in range(10):
        if i == 5:
            break
        if i % 2 == 0:
            continue
        print(i, end=' ')
    print()

def file_io():
    """Demonstrates file input/output."""
    filename = 'example.txt'
    with open(filename, 'w') as f:
        f.write("Hello, Python file IO!\n")

    with open(filename, 'r') as f:
        content = f.read()
        print("Read from file:", content)

    # JSON serialization and deserialization
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    json_data = json.dumps(data)
    print("JSON serialized data:", json_data)

    deserialized_data = json.loads(json_data)
    print("JSON deserialized data:", deserialized_data)

def error_handling():
    """Demonstrates try, except, finally structure."""
    try:
        # Trying to divide by zero
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught division by zero error")
    finally:
        print("This is the finally block executing.")

    # Raising custom exceptions
    try:
        raise ValueError("Custom exception raised")
    except ValueError as e:
        print("Caught custom exception:", str(e))

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

class InheritedClass(BasicClass):
    """A class that inherits from BasicClass and overrides the greet method."""
    def greet(self):
        """Overridden greet method."""
        print(f"Greetings from {self.name} in InheritedClass!")

def using_classes():
    """Function to demonstrate creating and using objects."""
    my_object = BasicClass("BasicClassObject")
    my_object.greet()
    BasicClass.example_static_method()

    inherited_object = InheritedClass("InheritedClassObject")
    inherited_object.greet()

def functional_programming():
    """Demonstrates functional programming concepts."""
    # Lambda functions
    square = lambda x: x ** 2
    print("Square of 5 using lambda:", square(5))

    # Map, filter, reduce
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print("Squared numbers using map:", squared_numbers)

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers using filter:", even_numbers)

    sum_of_numbers = functools.reduce(lambda x, y: x + y, numbers)
    print("Sum of numbers using reduce:", sum_of_numbers)

def decorators():
    """Demonstrates the usage of decorators."""
    def uppercase_decorator(func):
        def wrapper():
            result = func()
            return result.upper()
        return wrapper

    @uppercase_decorator
    def greet():
        return "hello, world!"

    print("Decorated function output:", greet())

def generators():
    """Demonstrates the usage of generators."""
    def square_generator(numbers):
        for num in numbers:
            yield num ** 2

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(square_generator(numbers))
    print("Squared numbers using generator:", squared_numbers)

def context_managers():
    """Demonstrates the usage of context managers."""
    class FileManager:
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None

        def __enter__(self):
            self.file = open(self.filename, self.mode)
            return self.file

        def __exit__(self, exc_type, exc_value, exc_traceback):
            if self.file:
                self.file.close()

    with FileManager('example.txt', 'w') as f:
        f.write("Hello, context manager!\n")

    with FileManager('example.txt', 'r') as f:
        content = f.read()
        print("Read from file using context manager:", content)

def advanced_topics():
    """Demonstrates advanced Python topics."""
    # Regular expressions
    text = "The quick brown fox jumps over the lazy dog."
    pattern = r"fox"
    match = re.search(pattern, text)
    if match:
        print("Found match:", match.group())

    # Date and time
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().time()
    print("Current date:", current_date)
    print("Current time:", current_time)

    # Iteration tools
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(itertools.map(lambda x: x ** 2, numbers))
    print("Squared numbers using itertools.map:", squared_numbers)

    # Partial functions
    def multiply(x, y):
        return x * y

    double = functools.partial(multiply, 2)
    print("Double of 5 using partial function:", double(5))

    # Named tuples
    Point = namedtuple('Point', ['x', 'y'])
    point = Point(3, 4)
    print("Point created using namedtuple:", point)

    # Counters
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    word_counts = Counter(words)
    print("Word counts using Counter:", word_counts)

# Entry point of the script
if __name__ == "__main__":
    print("Python Basics and Fundamentals\n")
    basic_data_types()
    collections_demo()
    control_structures()
    file_io()
    error_handling()
    using_classes()
    functional_programming()
    decorators()
    generators()
    context_managers()
    advanced_topics()