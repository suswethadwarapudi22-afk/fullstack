// PATH MODULE
// Used to work with files, file system and folders

// Import Path module
const path = require('path');

const filePath = 'C:\\Users\\anits-csm\\Documents\\os.txt';

// Get the directory name
console.log(`Directory Name: ${path.dirname(filePath)}`);

// Get the filename
console.log(`File Name: ${path.basename(filePath)}`);

// Get the file extension
console.log(`File Extension: ${path.extname(filePath)}`);

// Join path segments to create a new path
const newPath = path.join(__dirname, 'data', 'config.json');

console.log(`Joined Path: ${newPath}`);