#!/usr/bin/node

const args = process.argv;
const array = [];
for (let i = 2; i < args.length; i++) {
  array.push(parseInt(args[i]));
}

function second (arr) {
  if (args[2] === undefined) {
    console.log(0);
  } else if (args.length === 3) {
    console.log(0);
  } else {
    arr.sort();

    if (arr[arr.length - 2] !== arr[arr.length - 1]) {
      console.log(arr[arr.length - 2]);
    }
  }
}

second(array);
