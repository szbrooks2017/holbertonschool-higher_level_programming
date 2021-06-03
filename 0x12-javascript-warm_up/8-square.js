#!/usr/bin/node

let size = process.argv[2];
let no_arg = process.argv[1];
let i;
let j;

for (i = 0; i < size; i++) {
	for (j = 0; j < size; j++)
		if (size === no_arg){
			console.log("Missing size");
		}
		console.log("X".repeat(size));
}
