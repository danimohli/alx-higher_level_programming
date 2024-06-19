#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length) {
  let idx = 0;
  while (idx < argv.length) {
    console.log(argv[idx]);
    idx++;
  }
} else {
  console.log('No argument');
}
