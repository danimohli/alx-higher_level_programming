#!/usr/bin/node

const argv = process.argv.slice(2);

const x = parseInt(argv[0], 10);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
