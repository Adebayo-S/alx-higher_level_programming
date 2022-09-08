#!/usr/bin/node
const Square = require('./5-square');

class Square extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let col = 0; col < this.width; col++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
