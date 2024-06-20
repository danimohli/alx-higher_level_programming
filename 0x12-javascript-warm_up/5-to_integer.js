#!/usr/bin/node

const argv = process.argv.slice(2);

const number = parseInt(argv[0], 10);

if (!isNaN(number)) {
	console.log(`My number: ${number}`);
} else {
	console.log('Not a number');
}
