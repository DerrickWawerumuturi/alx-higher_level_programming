#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h >0)) {	
      this.width = w;
      this.height = h;
    }
  }
  
  print () {
    for (let row = 0; row <= this.width; row++) {
      let line = '';
      for (let col = 0; col <= this.height; col++ {
        line += 'X';
      }
      console.log(line); 	
    }
  }

  rotate () {
    for (let row = 0; row <= this.height; row++) {
      let line = '';
      for (let col = 0; col <= this.width; col++) {
        line += 'X';
      }
      console.log(line);	    
    }
  }

  double () {
    let n = 2 * print();
    console.log(n);
  }
}

module.exports  = Rectangle;
