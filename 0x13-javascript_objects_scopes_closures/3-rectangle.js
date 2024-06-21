#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || w <= 0 || typeof h !== 'number' || h <= 0) {
      // Create an empty object
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
