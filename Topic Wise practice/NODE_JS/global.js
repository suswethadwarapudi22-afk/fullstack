// Program to demonstrate the global object in Node.js

// Create a global variable
global.studentName = "Suswetha";
global.course = "AIML";
global.age = 20;

// Access global variables
console.log("Student Name:", global.studentName);
console.log("Course:", global.course);
console.log("Age:", global.age);

// Access the global variable without using 'global'
console.log("Student Name:", studentName);

global.x = 42;
console.log("Value of x:", global.x);
console.log("Value of x:", x);