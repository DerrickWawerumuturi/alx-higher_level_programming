#!/usr/bin/node

const args = process.argv;

if (args[2] === undefined) {
  console.log('undefined is undefined');
} else if (args[2] && args[3]) {
  console.log(args[2], 'is', args[3]);
} else {
  console.log(args[2], 'is undefined');
}
