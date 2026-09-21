const os = require('os');
const path = require('path');
const dns = require('dns');
const net = require('net');

// ==========================================
// 1. OS MODULE: System Information
// ==========================================
console.log('1. OS MODULE - modules.js:9');
console.log(`OS Platform: ${os.platform()} - modules.js:10`);
console.log(`CPU Architecture: ${os.arch()} - modules.js:11`);
console.log(`Total Memory: ${os.totalmem()} bytes - modules.js:12`);
console.log(`Free Memory: ${os.freemem()} bytes - modules.js:13`);
console.log('Current User Info: - modules.js:14', os.userInfo());
console.log();

// ==========================================
// 2. PATH MODULE: Working with File Paths
// ==========================================
console.log('2. PATH MODULE - modules.js:20');
const filePath = '/users/john/documents/report.txt';

console.log(`Directory Name: ${path.dirname(filePath)} - modules.js:23`);
console.log(`File Name: ${path.basename(filePath)} - modules.js:24`);
console.log(`File Extension: ${path.extname(filePath)} - modules.js:25`);

const newPath = path.join(__dirname, 'data', 'config.json');
console.log(`Joined Path: ${newPath} - modules.js:28`);
console.log();

// ==========================================
// 3. DNS MODULE: Resolving Domains & IPs
// ==========================================
console.log('3. DNS MODULE - modules.js:34');
dns.lookup('google.com', (err, address, family) => {
  if (err) return console.error('DNS Lookup Error: - modules.js:36', err.message);
  console.log(`IP Address for google.com: ${address} - modules.js:37`);
  console.log(`IP Family: IPv${family} - modules.js:38`);
});

dns.resolve4('google.com', (err, addresses) => {
  if (err) return console.error('DNS Resolve Error: - modules.js:42', err.message);
  console.log('All IPv4 addresses for google.com: - modules.js:43', addresses);
  console.log();
});

// ==========================================
// 4. NET MODULE: TCP Server & Client
// ==========================================
const PORT = 3000;

// Create TCP Server
const server = net.createServer((socket) => {
  console.log('TCP Server: Client connected. - modules.js:54');
  socket.write('Hello from the server!');

  socket.on('data', (data) => {
    console.log(`TCP Server Received: ${data.toString()} - modules.js:58`);
  });

  socket.on('end', () => {
    console.log('TCP Server: Client disconnected. - modules.js:62');
  });
});

server.listen(PORT, () => {
  console.log(`4. NET MODULE - modules.js:67`);
  console.log(`TCP Server listening on port ${PORT} - modules.js:68`);

  // Create a local TCP Client to connect to the server above
  const client = net.createConnection({ port: PORT }, () => {
    console.log('TCP Client: Connected to server! - modules.js:72');
    client.write('Hello from the client!');
  });

  client.on('data', (data) => {
    console.log(`TCP Client Received: ${data.toString()} - modules.js:77`);
    // Close client connection and server after test run
    client.end();
  });

  client.on('end', () => {
    console.log('TCP Client: Disconnected. - modules.js:83');
    server.close();
  });
});

// ==========================================
// 5. MODERN ERROR HANDLING (Replaces Domain)
// ==========================================
process.on('uncaughtException', (err) => {
  console.error('Global Uncaught Exception: - modules.js:92', err.message);
});

process.on('unhandledRejection', (reason) => {
  console.error('Global Unhandled Rejection: - modules.js:96', reason);
});