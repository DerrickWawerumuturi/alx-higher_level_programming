#!/usr/bin/node

const args = process.argv;

if (args.length === 2) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log(args[2]);
} else if (args.length >= 4) {
  console.log(args[2]);
}
