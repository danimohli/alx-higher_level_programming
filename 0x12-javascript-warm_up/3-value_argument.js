#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv[0]) {
	console.log(argv.join(' '));
} else {
  console.log('No argument');
}
