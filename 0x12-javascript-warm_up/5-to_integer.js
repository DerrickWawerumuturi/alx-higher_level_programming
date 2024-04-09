#!/usr/bin/node

const args = process.argv;

function isIntStr (str) {
  return /^\d+$/.test(str);
}

if (args[2] === undefined) {
  console.log('Not a number');
} else if (args[2] % 1 === 0 || args[2] !== 0) {
  console.log('My number:', Math.trunc(args[2]));
} else if (isIntStr(args[2]) === true) {
  console.log('My number:', args[2]);
} else {
  console.log('Not a number');
}
