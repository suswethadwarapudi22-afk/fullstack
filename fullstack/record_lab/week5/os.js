const os = require('os');


console.log(`OS Platform: ${os.platform()} - os.js:4`); // e.g., 'darwin', 'win32', 'linux'
console.log(`CPU Architecture: ${os.arch()} - os.js:5`); // e.g., 'x64'
console.log(`Total Memory: ${os.totalmem()} bytes - os.js:6`);
console.log(`Free Memory: ${os.freemem()} bytes - os.js:7`);
console.log(`Current User Info: - os.js:8`, os.userInfo());