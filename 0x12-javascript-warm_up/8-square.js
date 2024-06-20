#!/usr/bin/node

const argv = process.argv.slice(2);

const size = parseInt(argv[0], 10);

if (!isNaN(size) && size > 0) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
