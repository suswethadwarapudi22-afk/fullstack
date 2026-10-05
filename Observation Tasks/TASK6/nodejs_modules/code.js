// os module
const os = require("os");

console.log("Operating System: - code.js:4", os.platform());
console.log("CPU Architecture: - code.js:5", os.arch());
console.log("Home Directory: - code.js:6", os.homedir());
console.log("Number of CPUs: - code.js:7", os.cpus().length);

// path module
const path = require("path");

const filePath = path.join("students", "data.txt");

console.log("File Path: - code.js:14", filePath);
console.log("File Name: - code.js:15", path.basename(filePath));
console.log("Extension: - code.js:16", path.extname(filePath));

// fs module
const fs = require("fs");

fs.writeFileSync("message.txt", "Hello from Node.js!");

const data = fs.readFileSync("message.txt", "utf8");

console.log("File Content: - code.js:25", data);