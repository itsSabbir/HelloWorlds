import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.*;
import java.util.stream.Collectors;



public class javastuff {

    public static void main(String[] args) {
        // Function calls to demonstrate various Java concepts
        basicDataTypes();
        operatorsAndExpressions();
        controlStructures();
        usingCollections();
        fileIO();
        usingClassesAndObjects();
        exceptionHandling();
        lambdaExpressionsAndStreams();
        multithreading();
        designPatterns();
        solidPrinciples();
    }

    // Demonstrates basic data types in Java
    public static void basicDataTypes() {
        System.out.println("Basic Data Types:");
        // Integer (whole number)
        int integerVar = 42;
        // Double (floating-point number)
        double doubleVar = 3.14159;
        // Character (single Unicode character)
        char charVar = 'A';
        // Boolean (true or false)
        boolean boolVar = true;
        // String (sequence of characters)
        String strVar = "Hello, Java!";

        // Print out the values of each variable
        System.out.println("Integer: " + integerVar);
        System.out.println("Double: " + doubleVar);
        System.out.println("Char: " + charVar);
        System.out.println("Boolean: " + boolVar);
        System.out.println("String: " + strVar + "\n");

        // Type casting
        int intVar = 10;
        double dblVar = intVar; // Widening casting (automatic)
        int intVar2 = (int) dblVar; // Narrowing casting (manual)
    }

    // Demonstrates operators and expressions in Java
    public static void operatorsAndExpressions() {
        System.out.println("Operators and Expressions:");
        int a = 10, b = 5;

        // Arithmetic operators
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("a / b = " + (a / b));
        System.out.println("a % b = " + (a % b));

        // Relational operators
        System.out.println("a == b: " + (a == b));
        System.out.println("a != b: " + (a != b));
        System.out.println("a > b: " + (a > b));
        System.out.println("a < b: " + (a < b));
        System.out.println("a >= b: " + (a >= b));
        System.out.println("a <= b: " + (a <= b));

        // Logical operators
        boolean x = true, y = false;
        System.out.println("x && y: " + (x && y));
        System.out.println("x || y: " + (x || y));
        System.out.println("!x: " + (!x));
        System.out.println();
    }

    // Demonstrates control structures in Java
    public static void controlStructures() {
        System.out.println("Control Structures:");
        int x = 10;
        // Conditional statement (if-else)
        if (x > 5) {
            System.out.println("x is greater than 5");
        } else {
            System.out.println("x is not greater than 5");
        }

        // Conditional statement (switch)
        int dayOfWeek = 3;
        switch (dayOfWeek) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            default:
                System.out.println("Other day");
        }

        // Looping with a for loop
        for (int i = 0; i < 5; i++) {
            System.out.println("For loop iteration: " + i);
        }

        // Looping with a while loop
        int y = 3;
        while (y > 0) {
            System.out.println("While loop iteration: " + y);
            y--;
        }

        // Looping with a do-while loop
        int z = 0;
        do {
            System.out.println("Do-while loop iteration: " + z);
            z++;
        } while (z < 3);

        // Enhanced for loop (for-each loop)
        int[] numbers = {1, 2, 3, 4, 5};
        for (int number : numbers) {
            System.out.println("Enhanced for loop iteration: " + number);
        }
        System.out.println();
    }

    // Demonstrates the use of collections in Java
    public static void usingCollections() {
        System.out.println("Using Collections:");
        // List of Strings
        List<String> list = new ArrayList<>();
        list.add("Java");
        list.add("Python");
        list.add("C++");

        // Iterate over a list using a for loop
        for (int i = 0; i < list.size(); i++) {
            System.out.println("List item (for loop): " + list.get(i));
        }

        // Iterate over a list using an enhanced for loop
        for (String item : list) {
            System.out.println("List item (enhanced for loop): " + item);
        }

        // Map of Strings to Integers
        Map<String, Integer> map = new HashMap<>();
        map.put("Alice", 25);
        map.put("Bob", 30);

        // Iterate over a map using entrySet()
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println("Map entry: " + entry.getKey() + " - " + entry.getValue());
        }

        // Set of unique elements
        Set<String> set = new HashSet<>();
        set.add("Apple");
        set.add("Banana");
        set.add("Apple"); // Duplicate entry, will be ignored

        // Iterate over a set using an enhanced for loop
        for (String item : set) {
            System.out.println("Set item: " + item);
        }

        // Queue (FIFO - First In, First Out)
        Queue<String> queue = new LinkedList<>();
        queue.offer("First");
        queue.offer("Second");
        queue.offer("Third");

        // Process elements in the queue
        while (!queue.isEmpty()) {
            System.out.println("Queue item: " + queue.poll());
        }

        // Stack (LIFO - Last In, First Out)
        Stack<String> stack = new Stack<>();
        stack.push("First");
        stack.push("Second");
        stack.push("Third");

        // Process elements in the stack
        while (!stack.isEmpty()) {
            System.out.println("Stack item: " + stack.pop());
        }
        System.out.println();
    }

    // Demonstrates file input/output operations in Java
    public static void fileIO() {
        String filename = "example.txt";
        // Writing to a file
        try (FileWriter writer = new FileWriter(filename)) {
            writer.write("Hello, Java file IO!\n");
        } catch (IOException e) {
            System.out.println("An error occurred during writing the file.");
            e.printStackTrace();
        }

        // Reading from a file
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            System.out.println("Reading from file:");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("An error occurred during reading the file.");
            e.printStackTrace();
        }
        System.out.println();
    }

    // Demonstrates the use of classes and objects in Java
    public static void usingClassesAndObjects() {
        System.out.println("Using Classes and Objects:");
        // Create an instance of BasicClass
        BasicClass basicObject = new BasicClass("JavaClass");
        // Call a method on the instance
        basicObject.greet();

        // Create an instance of MyClass
        MyClass myObject = new MyClass();
        // Call a method defined by the MyInterface interface
        myObject.interfaceMethod();
        System.out.println();
    }

    // Demonstrates exception handling in Java
    public static void exceptionHandling() {
        System.out.println("Exception Handling:");
        try {
            int result = 10 / 0; // Throws ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Caught ArithmeticException: " + e.getMessage());
        } finally {
            System.out.println("Finally block executed.");
        }

        // Custom exception
        try {
            throw new CustomException("Custom exception message");
        } catch (CustomException e) {
            System.out.println("Caught CustomException: " + e.getMessage());
        }
        System.out.println();
    }

    // Demonstrates lambda expressions and streams in Java
    public static void lambdaExpressionsAndStreams() {
        System.out.println("Lambda Expressions and Streams:");
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

        // Lambda expression to square each number
        List<Integer> squaredNumbers = numbers.stream()
                .map(x -> x * x)
                .collect(Collectors.toList());
        System.out.println("Squared numbers: " + squaredNumbers);

        // Lambda expression to filter even numbers
        List<Integer> evenNumbers = numbers.stream()
                .filter(x -> x % 2 == 0)
                .collect(Collectors.toList());
        System.out.println("Even numbers: " + evenNumbers);

        // Lambda expression to calculate the sum of numbers
        int sum = numbers.stream()
                .reduce(0, (a, b) -> a + b);
        System.out.println("Sum of numbers: " + sum);
        System.out.println();
    }

    // Demonstrates multithreading in Java
    public static void multithreading() {
        System.out.println("Multithreading:");
        // Create and start threads
        Thread thread1 = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Thread 1: " + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread thread2 = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Thread 2: " + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        thread1.start();
        thread2.start();

        // Wait for threads to complete
        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println();
    }

    // Demonstrates design patterns in Java
    public static void designPatterns() {
        System.out.println("Design Patterns:");

        // Singleton pattern
        Singleton singleton1 = Singleton.getInstance();
        Singleton singleton2 = Singleton.getInstance();
        System.out.println("Singleton instances are equal: " + (singleton1 == singleton2));

        // Factory pattern
        ShapeFactory factory = new ShapeFactory();
        Shape circle = factory.getShape("Circle");
        Shape rectangle = factory.getShape("Rectangle");
        circle.draw();
        rectangle.draw();

        // Observer pattern
        Subject subject = new Subject();
        Observer observer1 = new ConcreteObserver("Observer 1");
        Observer observer2 = new ConcreteObserver("Observer 2");
        subject.registerObserver(observer1);
        subject.registerObserver(observer2);
        subject.notifyObservers("New message");

        System.out.println();
    }

    // Demonstrates SOLID principles in Java
    public static void solidPrinciples() {
        System.out.println("SOLID Principles:");

        // Single Responsibility Principle (SRP)
        // Each class should have a single responsibility and encapsulate that responsibility entirely.

        // Open/Closed Principle (OCP)
        // Classes should be open for extension but closed for modification.

        // Liskov Substitution Principle (LSP)
        // Derived classes should be substitutable for their base classes.

        // Interface Segregation Principle (ISP)
        // Clients should not be forced to depend on interfaces they do not use.

        // Dependency Inversion Principle (DIP)
        // High-level modules should depend on abstractions, not on low-level modules.

        System.out.println("SOLID principles are design guidelines to write maintainable and extensible code.");
        System.out.println();
    }

    // Interface definition
    interface MyInterface {
        void interfaceMethod();
    }

    // A simple class demonstrating constructors and methods
    static class BasicClass {
        private String name;

        public BasicClass(String name) {
            this.name = name;
        }

        public void greet() {
            System.out.println("Hello from " + name + "!");
        }
    }

    // A class that extends BasicClass and implements MyInterface
    static class MyClass extends BasicClass implements MyInterface {
        public MyClass() {
            super("MyClass");
        }

        public void interfaceMethod() {
            System.out.println("This is an interface method implemented in MyClass.");
        }
    }

    // Custom exception class
    static class CustomException extends Exception {
        public CustomException(String message) {
            super(message);
        }
    }

    // Singleton pattern
    static class Singleton {
        private static Singleton instance = new Singleton();

        private Singleton() {
        }

        public static Singleton getInstance() {
            return instance;
        }
    }

    // Factory pattern
    interface Shape {
        void draw();
    }

    static class Circle implements Shape {
        public void draw() {
            System.out.println("Drawing a circle.");
        }
    }

    static class Rectangle implements Shape {
        public void draw() {
            System.out.println("Drawing a rectangle.");
        }
    }

    static class ShapeFactory {
        public Shape getShape(String shapeType) {
            if (shapeType.equalsIgnoreCase("Circle")) {
                return new Circle();
            } else if (shapeType.equalsIgnoreCase("Rectangle")) {
                return new Rectangle();
            }
            return null;
        }
    }

    // Observer pattern
    interface Observer {
        void update(String message);
    }

    static class Subject {
        private List<Observer> observers = new ArrayList<>();

        public void registerObserver(Observer observer) {
            observers.add(observer);
        }

        public void removeObserver(Observer observer) {
            observers.remove(observer);
        }

        public void notifyObservers(String message) {
            for (Observer observer : observers) {
                observer.update(message);
            }
        }
    }

    static class ConcreteObserver implements Observer {
        private String name;

        public ConcreteObserver(String name) {
            this.name = name;
        }

        public void update(String message) {
            System.out.println(name + " received message: " + message);
        }
    }
}