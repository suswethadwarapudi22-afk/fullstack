const fs = require('fs');

// 1. Writing to a file
const content = 'This is new content for the file.';
fs.writeFile('newfile.txt', content, err => {
  if (err) throw err;
  console.log('File has been saved! - create.js:7');

  // 2. Reading the file
  fs.readFile('newfile.txt', 'utf8', (err, data) => {
    if (err) throw err;
    console.log('Read data: - create.js:12', data);

    // 3. Appending to the file
    fs.appendFile('newfile.txt', '\nThis is appended content.', err => {
      if (err) throw err;
      console.log('Content appended! - create.js:17');

      // 4. Checking if the file exists
      fs.access('newfile.txt', fs.constants.F_OK, (err) => {
        if (err) {
          console.log('File does not exist. - create.js:22');
        } else {
          console.log('File exists. - create.js:24');

          // 5. Deleting the file
          fs.unlink('newfile.txt', err => {
            if (err) throw err;
            console.log('File was deleted. - create.js:29');
          });
        }
      });
    });
  });
});