#!/usr/bin/node
const myVar1 = 'No argument';
const myVar2 = 'Argument found';
const myVar3 = 'Arguments found';

if (process.argv.length > 3) {
  console.log(myVar3);
} else if (process.argv.length === 3) {
  console.log(myVar2);
} else {
  console.log(myVar1);
}
