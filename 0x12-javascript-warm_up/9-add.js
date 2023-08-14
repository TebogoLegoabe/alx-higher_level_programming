#!/usr/bin/node

function add(a, b) {
  const sum = a + b;
  console.log(sum);
}
const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);

add(firstInt, secondInt);
