#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      let line = '';
      for (let col = 0; col < this.width; col++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    const rot = this.width;
    this.width = this.height;
<<<<<<< HEAD
    this.height  = rot;	  
=======
    this.height  = rot;
>>>>>>> 6d53da6d54f2265d92508bafd5a90403c911a15f
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
<<<<<<< HEAD
=======
~
>>>>>>> 6d53da6d54f2265d92508bafd5a90403c911a15f
