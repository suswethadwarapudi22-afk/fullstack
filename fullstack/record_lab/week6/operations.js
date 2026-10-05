const fs = require('fs').promises;

async function writeFile() {
  try {
    const content = 'Hello, this is new text written to the file!';
    
    // (fileName, dataToWrite)
    await fs.writeFile('newfile.txt', content);
    
    console.log('File created and saved successfully! - operations.js:10');
  } catch (err) {
    console.error('Failed to write file: - operations.js:12', err.message);
  }
}

writeFile();