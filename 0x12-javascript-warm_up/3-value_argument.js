#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv[0]) {
  let idx = 0;
  while (argv[idx]) {
    console.log(argv[idx]);
    idx++;
  }
} else {
  console.log('No argument');
}
