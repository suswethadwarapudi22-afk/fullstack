const fs = require('fs').promises;

async function readFile() {
  try {
    // 'utf8' ensures you get plain text instead of raw Buffer bytes
    const data = await fs.readFile('task.txt', 'utf8');
    console.log(data);
  } catch (err) {
    console.error('Failed to read file: - read.js:9', err.message);
  }
}

readFile();