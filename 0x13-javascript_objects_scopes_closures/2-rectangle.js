#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === 0 || h === 0 || w < 0 || h < 0) {
      this.width = undefined;
      this.heigth = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
