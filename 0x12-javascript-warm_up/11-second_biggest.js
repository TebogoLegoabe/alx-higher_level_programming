#!/usr/bin/node

const { argv } = require('process');

const integers = argv.slice(2).map(Number);

if (integers.length > 1) {
  const nextMax = integers.sort((a, b) => b - a)[1];
  console.log(nextMax);
} else {
  console.log(0);
}
