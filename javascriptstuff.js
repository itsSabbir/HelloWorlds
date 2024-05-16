// Introduction to Basic Data Types in JavaScript
function basicDataTypes() {
    console.log("Basic Data Types:");
    let integerVar = 42;              // Number
    let floatVar = 3.14159;           // Floating-point number (also Number)
    let strVar = "Hello, JavaScript!"; // String
    let boolVar = true;               // Boolean
    let nullVar = null;               // Null
    let undefinedVar;                 // Undefined

    console.log("Integer:", integerVar);
    console.log("Float:", floatVar);
    console.log("String:", strVar);
    console.log("Boolean:", boolVar);
    console.log("Null:", nullVar);
    console.log("Undefined:", undefinedVar);
}

// Demonstrating Control Structures
function controlStructures() {
    console.log("Control Structures:");
    let x = 10;
    if (x > 5) {
        console.log("x is greater than 5");
    } else {
        console.log("x is not greater than 5");
    }

    for (let i = 0; i < 5; i++) {
        console.log("For loop iteration:", i);
    }

    let y = 3;
    while (y > 0) {
        console.log("While loop iteration:", y);
        y--;
    }
}

// Functions in JavaScript
function sampleFunction(a, b) {
    return a + b;
}

// Working with Arrays
function workingWithArrays() {
    console.log("Working with Arrays:");
    let array = [1, 2, 3, 4, 5];
    console.log("Array:", array);
    console.log("Access third element:", array[2]); // Accessing the third element

    // Adding elements to an array
    array.push(6);
    console.log("Array after push:", array);
}

// Objects in JavaScript
function workingWithObjects() {
    console.log("Working with Objects:");
    let object = {
        firstName: "John",
        lastName: "Doe",
        age: 30
    };

    console.log("Object:", object);
    console.log("Access property:", object.firstName); // Accessing property

    // Adding a new property
    object.gender = "Male";
    console.log("Object after adding property:", object);
}

// Event handling in JavaScript
function addClickEvent() {
    let button = document.getElementById("clickButton");
    button.addEventListener("click", function() {
        alert("Button was clicked!");
    });
}

// DOM Manipulation
function modifyDOM() {
    let content = document.getElementById("content");
    content.textContent = "Changed the content of the div!";
}

// Calling the functions to demonstrate concepts
basicDataTypes();
controlStructures();
workingWithArrays();
workingWithObjects();

// Uncomment these in an HTML environment where DOM elements exist
// addClickEvent();
// modifyDOM();

