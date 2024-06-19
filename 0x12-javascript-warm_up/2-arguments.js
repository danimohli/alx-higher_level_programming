#!/usr/bin/node

const argv = process.argv;

const argc = argv.length - 2;

if (argc === 0) {
  console.log('No argument');
} else if (argc === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
