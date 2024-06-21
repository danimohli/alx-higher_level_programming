#!/usr/bin/node

const { dict } = require('./101-data');

const newDict = {};

for (const [id, occur] of Object.entries(dict)) {
  if (newDict[occur]) {
    newDict[occur].push(id);
  } else {
    newDict[occur] = [id];
  }
}

console.log(newDict);
