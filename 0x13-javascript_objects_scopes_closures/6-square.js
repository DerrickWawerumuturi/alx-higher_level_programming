#!/usr/bin/node

const Square1 = require('./5-square.js');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let row = 0; row < this.height; row++) {
      let line = '';
      for (let col = 0; col < this.width; col++) {
        line += c;
      }
      console.log(line);
    }
  }
}
module.exports = Square;
