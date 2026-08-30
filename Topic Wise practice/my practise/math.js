// math.js

// Create functions
function add(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    return a / b;
}

// Export the functions
module.exports = {
    add,
    subtract,
    multiply,
    divide
};

// app.js

// Import the custom module
const math = require("./math");

// Use the functions from math.js
console.log("Addition: - math.js:34", math.add(10, 5));
console.log("Subtraction: - math.js:35", math.subtract(10, 5));
console.log("Multiplication: - math.js:36", math.multiply(10, 5));
console.log("Division: - math.js:37", math.divide(10, 5));

// Node.js Global Objects

console.log("\n Global Objects - math.js:41");

console.log("Current Directory: - math.js:43", __dirname);
console.log("Current File: - math.js:44", __filename);
console.log("Node.js Version: - math.js:45", process.version);
console.log("Platform: - math.js:46", process.platform);

// Console is also a global object
console.log("This is the console global object. - math.js:49");