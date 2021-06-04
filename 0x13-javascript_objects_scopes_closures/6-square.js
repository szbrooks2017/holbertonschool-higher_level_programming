#!/usr/bin/node

const Square1 = require('./5-square');;
class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c == null) {
      this.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
