#!/usr/bin/node

const size = process.argv[2];
let j;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (j = 0; j < size; j++) {
    console.log('X'.repeat(size));
  }
}
