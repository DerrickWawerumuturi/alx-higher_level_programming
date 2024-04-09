#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  return (parseInt(a) + parseInt(b));
}

if (args[2] && args[3]) {
  let total = add(args[2], args[3]);
  console.log(total);
} else {
  console.log('NaN');
}
