#!/usr/bin/node
/* prints My number: <first argument converted in integer> */

if (parseInt(process.argv[2])){
	console.log('My number: ' + process.argv[2])
} else{
	console.log('Not a number')
}
