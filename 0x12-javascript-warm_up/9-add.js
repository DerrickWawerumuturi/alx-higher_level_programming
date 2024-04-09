#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  return (a + b);
}

if (args[2] && args[3]) {
  console.log(add(args[2], args[3]));
} else {
  console.log('NaN');
}
