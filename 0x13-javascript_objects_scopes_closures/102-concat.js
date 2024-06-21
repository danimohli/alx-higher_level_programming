#!/usr/bin/node

const fs = require('fs');

// Get file from command-line arguments
const [,, firstFile, secondFile, destinationFile] = process.argv;

// Read first file
fs.readFile(firstFile, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading file ${firstFile}:`, err);
    return;
  }

  // Read second file
  fs.readFile(secondFile, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading file ${secondFile}:`, err);
      return;
    }

    // contents of both files
    const concatenatedData = data1 + data2;

    // Write file  to the final file
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to file ${destinationFile}:`, err);
      }
    });
  });
});
