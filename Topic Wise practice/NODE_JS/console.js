// Program to demonstrate the console object in Node.js

// Display normal message
console.log("Hello World");

// Display information
console.info("This is an information message");

// Display warning
console.warn("This is a warning message");

// Display error
console.error("This is an error message");

// Display multiple values
let name = "Suswetha";
let age = 20;
console.log("Name:", name);
console.log("Age:", age);

//table 
let students = [
    { name: "Ravi", age: 20 },
    { name: "Sita", age: 21 },
    { name: "John", age: 19 }
];

console.table(students);

//console.time() and console.timeend()
console.time("Loop");

for (let i = 0; i < 1000000; i++) {
    // some work
}

console.timeEnd("Loop");

//console.count()
console.count("Button clicked");
console.count("Button clicked");
console.count("Button clicked");

//comsole.dir
let student = {
    name: "Suswetha",
    age: 20,
    course: "AIML"
};

console.dir(student);