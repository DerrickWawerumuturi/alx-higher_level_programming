#!/usr/bin/node

const args = process.argv;
const string = 'C is fun';

function isIntStr (str) {
  return /^\d+$/.test(str);
}


if (args[2] < 0) {
  return;
} else if (isIntStr(args[2]) === false) {
  console.log('Missing number of occurrences');
} else {
  for (let i  = 0; i < args[2]; i++) {
    console.log(string);
  }
}
