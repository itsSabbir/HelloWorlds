import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class javastuff {

    public static void main(String[] args) {
        // Function calls to demonstrate various Java concepts
        basicDataTypes();
        controlStructures();
        usingCollections();
        fileIO();
        usingClassesAndObjects();
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

        // Map of Strings to Integers
        Map<String, Integer> map = new HashMap<>();
        map.put("Alice", 25);
        map.put("Bob", 30);

        // Print the contents of the list and map
        System.out.println("List: " + list);
        System.out.println("Map: " + map);
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
}
