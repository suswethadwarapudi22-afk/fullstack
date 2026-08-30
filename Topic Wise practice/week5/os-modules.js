// OS MODULE
// Provides information about the OS and computer

// IMPORT OS MODULE
const os = require('os');

console.log(`OS platform: ${os.platform()}`); 
// OS platform

console.log(`CPU architecture: ${os.arch()}`); 
// CPU architecture

console.log(`Hostname: ${os.hostname()}`);

console.log(`Total memory: ${os.totalmem()} bytes`);

console.log(`Free memory: ${os.freemem()} bytes`);
// Available/free memory

console.log('Current user info:', os.userInfo());