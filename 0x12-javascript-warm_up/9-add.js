#!/usr/bin/node

const argv = process.argv.slice(2);

const a = parseInt(argv[0], 10);
const b = parseInt(argv[1], 10);

function add (a, b) {
  return a + b;
}
if (!isNaN(a) && !isNaN(b)) {
  console.log(add(a, b));
} else {
  console.log('NaN');
}
